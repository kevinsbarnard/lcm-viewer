# VideoSelectionDialog.py (lcm-viewer)
# Stereo video selection dialog, report back two selected video paths
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QDialog, QFormLayout, QPushButton, QDialogButtonBox, QFileDialog


class VideoSelectionDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setModal(True)

        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

        self.left_select = QPushButton('Select a file')
        self.left_select.pressed.connect(self.left_select_slot)
        self.right_select = QPushButton('Select a file')
        self.right_select.pressed.connect(self.right_select_slot)

        self.left_video = None
        self.right_video = None

        self.form_layout.addRow('Left Stereo Video', self.left_select)
        self.form_layout.addRow('Right Stereo Video', self.right_select)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Open | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.form_layout.addWidget(self.button_box)

    def left_select_slot(self):
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   caption='Select left video',
                                                   directory=QDir.homePath(),
                                                   filter='Videos (*.mp4)')
        if file_name:
            self.left_select.setText(file_name)
            self.left_video = file_name

    def right_select_slot(self):
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   caption='Select right video',
                                                   directory=QDir.homePath(),
                                                   filter='Videos (*.mp4)')
        if file_name:
            self.right_select.setText(file_name)
            self.left_video = file_name
