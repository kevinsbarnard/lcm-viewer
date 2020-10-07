# run.py (lcm-viewer)

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QAction
import ui


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("LCM Video Viewer")

        # Central widget, top-level items added to this layout
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        # Viewer panel
        self.viewer_panel = ui.ViewerPanel()
        self.central_layout.addWidget(self.viewer_panel, stretch=1)

        # Menu
        self.file_menu = self.menuBar().addMenu('&File')
        self.open_videos_action = QAction('&Load videos', self)
        self.open_videos_action.setShortcut('Ctrl+O')
        self.open_videos_action.setStatusTip('Load stereo videos for playback')
        self.open_videos_action.triggered.connect(self.open_videos_slot)
        self.file_menu.addAction(self.open_videos_action)

        self.show()

    def open_videos_slot(self):
        dialog = ui.VideoSelectionDialog()
        status = dialog.exec_()
        if status and dialog.left_video and dialog.right_video:
            self.viewer_panel.load_videos(dialog.left_video, dialog.right_video)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("LCM Video Viewer")

    window = MainWindow()
    sys.exit(app.exec_())
