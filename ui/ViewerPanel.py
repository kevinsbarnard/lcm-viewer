# ViewerPanel.py (lcm-viewer)
# Viewer panel widget
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class ViewerPanel(QWidget):
    VIDEO_H, VIDEO_W = 772, 1032

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setLayout(QHBoxLayout())

        self.setMinimumSize(ViewerPanel.VIDEO_W * 2 // 2, ViewerPanel.VIDEO_H // 2)

        # Set up video widgets
        self.mp_left = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.vw_left = QVideoWidget()
        self.mp_left.setVideoOutput(self.vw_left)

        self.mp_right = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.vw_right = QVideoWidget()
        self.mp_right.setVideoOutput(self.vw_right)

        self.layout().addWidget(self.vw_left)
        self.layout().addWidget(self.vw_right)

    def load_videos(self, video_left: str, video_right: str):
        self.mp_left.setMedia(QMediaContent(QUrl.fromLocalFile(video_left)))
        self.mp_right.setMedia(QMediaContent(QUrl.fromLocalFile(video_right)))
