import unittest
import cv2
import os

from context import wild_bee_watch


class TestBeeDetectorMethods(unittest.TestCase):

    def test_bee_detector(self):
        """
        Make sure that the default config is valid
        """

        config_loader = wild_bee_watch.config_loader.ConfigLoader()
        config = config_loader.load(
            os.path.dirname(__file__) + "/data/config.yaml")
        self.assertIsNotNone(config)

        preprocessing = wild_bee_watch.preprocessing.Preprocessing(
            config['preprocessing'])
        detector = wild_bee_watch.bee_detector.BeeDetector(
            config['bee_detector'], preprocessing)

        im_background = cv2.imread(os.path.dirname(
            __file__) + "/data/background.jpg")
        im_single_bee = cv2.imread(os.path.dirname(
            __file__) + "/data/single_bee.jpg")

        detector.initialize(im_background)

        bboxes = detector.detect(im_single_bee)

        self.assertEqual(1, len(bboxes))


if __name__ == '__main__':
    unittest.main()
