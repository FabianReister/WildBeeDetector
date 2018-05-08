import cv2


class Preprocessing:
    def __init__(config):
        self.__config = config

    def _normalize(self, img):
        pass

    def _warp(self, img):
        pass

    def process(self, img):
        img_color_warped = self._warp(img)
        img_gray_warped = cv2.cvtColor(img_color_warped, cv2.COLOR_RGB2GRAY)
        img_normalized = self._normalize(img_gray_warped)

        return img_normalized, img_color_warped
