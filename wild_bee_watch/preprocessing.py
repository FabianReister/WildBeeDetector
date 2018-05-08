import cv2
import numpy as np


class Preprocessing:
    def __init__(self, config):
        self.__config = config

        self.__perspective_transform = self.__create_perspective_transform()

    def _normalize(self, img):
        """
        Performs a normalization of a gray scale image to remove local lighting inhomogenity

        For more information about the algorithm, read

        Beyerer, Jürgen, Puente León, Fernando, Frese, Christian: Automatische Sichtprüfung - Grundlagen, Methoden und Praxis der Bildgewinnung und Bildauswertung

        """
        img = img.astype(np.float32)

        k_size = self.__config['kernel_size']

        mean = cv2.GaussianBlur(img, k_size, 0)
        stddev = np.sqrt(cv2.GaussianBlur((img - mean)**2, k_size, 0))

        # prevent division by zero
        # if stddev is zero, there is no contrast at all -> set to 0
        mask = stddev < 1
        stddev[mask] = 1

        n = (img - mean) / stddev
        n[mask] = 0
        return n

    def __create_perspective_transform(self):
        width = height = self.__config['img_size']

        # the corner points where they actually are
        distorted_rect = np.asarray(
            self.__config['corner_points'], dtype=np.float32)

        assert(distorted_rect.shape == (4, 2))

        # the corner points where they should be
        upper_left = [0, 0]
        lower_left = [0, height - 1]
        upper_right = [width - 1, 0]
        lower_right = [width - 1, height - 1]

        dst = np.asarray([upper_left, lower_left, upper_right,
                          lower_right], dtype=np.float32)

        perspective_transform = cv2.getPerspectiveTransform(
            distorted_rect, dst)

        assert(not np.isnan(perspective_transform).any())

        return perspective_transform

    def _warp_perspective(self, img):
        width = height = self.__config['img_size']
        return cv2.warpPerspective(img, self.__perspective_transform, (width, height))

    def process(self, img: np.ndarray):
        if(len(img.shape) is not 3):
            pass

        img_color_warped = self._warp_perspective(img)
        img_gray_warped = cv2.cvtColor(img_color_warped, cv2.COLOR_RGB2GRAY)
        img_normalized = self._normalize(img_gray_warped)

        return img_normalized, img_color_warped
