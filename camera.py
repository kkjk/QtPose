import sys
from PyQt5 import  QtWidgets, QtMultimedia, QtMultimediaWidgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.online_webcams = QtMultimedia.QCameraInfo.availableCameras()
        if not self.online_webcams:
            pass #quit
        self.exist = QtMultimediaWidgets.QCameraViewfinder()
        self.exist.show()
        self.setCentralWidget(self.exist)

        # set the default webcam.
        self.get_webcam(0)
        self.setWindowTitle("WebCam")
        self.show()

    def get_webcam(self, i):
        self.my_webcam = QtMultimedia.QCamera(self.online_webcams[i])
        self.my_webcam.setViewfinder(self.exist)
        self.my_webcam.setCaptureMode(QtMultimedia.QCamera.CaptureStillImage)
        self.my_webcam.error.connect(lambda: self.alert(self.my_webcam.errorString()))
        self.my_webcam.start()

    def alert(self, s):
        """
        This handle errors and displaying alerts.
        """
        err = QtWidgets.QErrorMessage(self)
        err.showMessage(s)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("WebCam")

    window = MainWindow()
    app.exec_()
