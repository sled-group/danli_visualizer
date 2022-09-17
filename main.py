import json
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLabel, QTextBrowser
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui

from PyQt5 import uic
import sys

# custom label to display image: https://stackoverflow.com/questions/21041941/how-to-autoresize-qlabel-pixmap-keeping-ratio-without-using-classes
class ScaledLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self)
        self._original_pixmap = None

    def setPixmap(self, img):
        super().setPixmap(img)

        # when pixmap is updated by anything other than resizeEvent,
        # we want to store an original copy of that image so that later it can be used for resizing
        self._original_pixmap = img

    def resizeEvent(self, event):
        # calling the setPixmap from super() here
        # cuz we dont want to update the _original_pixmap
        # when the setPixmap() is triggered by a resize event
        super().setPixmap(self._original_pixmap.scaled(
            self.width(), self.height(),
            QtCore.Qt.KeepAspectRatio))


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("mainwindow.ui", self)

        self.current_step = 1

        # find the widgets in the xml file
        self.rawObservationDisplay = self.findChild(QLabel, "rawObservationDisplay")
        # self.panopticDisplay = self.findChild(QLabel, "panopticDisplay")
        self.voxelSideViewDisplay = self.findChild(QLabel, "voxelSideViewDisplay")
        self.voxelTopViewDisplay = self.findChild(QLabel, "voxelTopViewDisplay")

        self.step_label = self.findChild(QLabel, "step_label")
        self.stage_label = self.findChild(QLabel, "stage_label")

        self.dialog_textBrowser = self.findChild(QTextBrowser, "dialog_textBrowser")
        self.subgoal_textBrowser = self.findChild(QTextBrowser, "subgoal_textBrowser")

        self.events_textBrowser = self.findChild(QTextBrowser, "events_textBrowser")
        self.plan_textBrowser = self.findChild(QTextBrowser, "plan_textBrowser")

        self.last_action_textBrowser = self.findChild(QTextBrowser, "last_action_textBrowser")
        self.action_to_take_textBrowser = self.findChild(QTextBrowser, "action_to_take_textBrowser")

        self.events_label = self.findChild(QLabel, "events_label")

        self.previous_button = self.findChild(QPushButton, "previous_button")
        self.next_button = self.findChild(QPushButton, "next_button")

        self.previous_button.clicked.connect(self.clicked_previous_button)
        self.next_button.clicked.connect(self.clicked_next_button)

        # self.label.installEventFilter(self)



        self.update_gui()




    def clicked_previous_button(self):
        self.current_step = max(0, self.current_step - 1)
        self.update_gui()

    def clicked_next_button(self):
        self.current_step = max(0, self.current_step + 1)
        self.update_gui()

    def _set_image_to_display(self, q_label, image_path):
        img = QPixmap(image_path)
        # img = img.scaledToHeight(150)
        # q_label.setScaledContents(True)
        # q_label.setPixmap(img)
        q_label.setPixmap(img.scaled(
            q_label.width(), q_label.height(),
            QtCore.Qt.KeepAspectRatio))

    def _set_text_to_text_browser(self, q_text_browser, text_path):
        print(text_path)
        with open(text_path) as f:
            contents = '\n'.join(f.readlines())
        q_text_browser.setMarkdown(contents)

    def _process_dialogs_data(self, dialogs):
        result = ''
        for dialog in dialogs:
            prefix = 'USR' if dialog[0] == 'Commander' else 'BOT'
            result += f'{prefix}: {dialog[1]}\n\n'
        return result

    def _process_subgoals_data(self, subgoals):
        result = ''
        for subgoal in subgoals:
            result += f'{subgoal[0]} {subgoal[1]} {subgoal[2]}\n\n'
        return result

    def update_gui(self):

        base_dir = '/data/simbot/teach-eval/neural_symbolic/viz_new/meta/a0ccd363ffb0ee94_c237_edh0'
        with open(os.path.join(base_dir, 'meta_data.json'), 'r') as meta_data_file:
            meta_data = json.load(meta_data_file)

        dialogs_data = meta_data['dialogs']
        subgoals_data = meta_data['subgoals']

        self.dialog_textBrowser.setMarkdown(self._process_dialogs_data(dialogs_data))
        self.subgoal_textBrowser.setMarkdown(self._process_subgoals_data(subgoals_data))

        step_data = meta_data['steps'][self.current_step]

        img_idx = step_data['img_idx']

        self.step_label.setText(str(step_data['step_idx']))
        self.stage_label.setText(str(step_data['stage']))


        self._set_image_to_display(self.rawObservationDisplay, os.path.join(base_dir, 'observation', '{}.jpg'.format(img_idx)))
        # self._set_image_to_display(self.panopticDisplay, os.path.join(base_dir, 'panoptic', '{}.jpg'.format(img_idx)))
        self._set_image_to_display(self.voxelSideViewDisplay, os.path.join(base_dir, 'sideview_map', '{}.jpg'.format(img_idx)))
        self._set_image_to_display(self.voxelTopViewDisplay, os.path.join(base_dir, 'topdown_map', '{}.jpg'.format(img_idx)))

        # self._set_text_to_text_browser(self.subgoal_textBrowser, base_dir.format('subgoal/' + str(self.current_step)))
        # self._set_text_to_text_browser(self.plan_textBrowser, step_data['status']['plan'])
        if step_data['status'] is not None:
            self.plan_textBrowser.setMarkdown('\n'.join([str(d) for d in step_data['status']['plan']]))
            self.events_textBrowser.setMarkdown('\n'.join([str(d) for d in step_data['status']['events']]))

        self.last_action_textBrowser.setText('{} {} {}'.format(step_data['last_action']['action_type'], step_data['last_action'].get('instance_id', ''), ": Succeeded" if step_data['last_action'].get('last_action_success') in (True,None) else ': Failed'))
        self.action_to_take_textBrowser.setText('{} {}'.format(step_data['action_to_take']['action_type'], step_data['last_action'].get('instance_id', '')))


if __name__ == "__main__":
    app = QApplication([])
    widget = GUI()
    widget.show()
    sys.exit(app.exec_())
