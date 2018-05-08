import numpy as np
import cv2

from wild_bee_watch import Preprocessing


class BeeDetector:
    def __init__(self, config, preprocessing):
        self.__initialized = False
        self._config = config

        self._preprocessing = preprocessing
        self._bg = None

        self.__k = self.__create_correlation_kernel()

    def __create_correlation_kernel(self):
        k_size = tuple(self._config['k_size'])

        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, k_size)
        k = k / np.mean(k.ravel())

        return k

    def initialize(self, image):
        self._bg, _ = self._preprocessing.process(image)
        self.__initialized = True

    def __update_background(self, image, mask):
        pass

    def detect(self, image):
        assert(self.__initialized)

        activity = np.abs(image - self._bg)

        # correlation filter

        activity_corr = cv2.filter2D(activity, cv2.CV_32F, k)
        act_bin = (act > 260).astype(np.uint8)
