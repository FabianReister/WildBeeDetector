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

        img_normalized, _ = self._preprocessing.process(image)

        activity = np.abs(img_normalized - self._bg)

        # correlation filter
        th_corr = self._config['th_corr']

        activity_corr = cv2.filter2D(activity, cv2.CV_32F, self.__k)
        act_bin = (activity_corr > th_corr).astype(np.uint8)

        # find bees in the binary activation image
        _, contours, _ = cv2.findContours(
            act_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        bounding_rects = list(map(cv2.boundingRect, contours))

        return bounding_rects
