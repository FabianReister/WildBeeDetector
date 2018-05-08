import unittest
import cv2
import numpy as np

from context import wild_bee_watch


class TestPreprocessingMethods(unittest.TestCase):

    def test_default_config(self):
        """
        Make sure that the default config is valid
        """
        config_loader = wild_bee_watch.config_loader.ConfigLoader()
        config = config_loader.load()
        self.assertIsNotNone(config)

        perprocessing = wild_bee_watch.preprocessing.Preprocessing(
            config['preprocessing'])

    def test_preprocessing(self):
        config_loader = wild_bee_watch.config_loader.ConfigLoader()
        config = config_loader.load("./data/config.yaml")
        self.assertIsNotNone(config)

        preprocessing = wild_bee_watch.preprocessing.Preprocessing(
            config['preprocessing'])

        img = cv2.imread('./data/background.jpg')
        img_black = np.zeros_like(img)

        img_normalized, img_color = preprocessing.process(img)
        img_black_normalized, img_black_color = preprocessing.process(
            img_black)

        def preprocessed_image(img):

            img_normalized, img_color = preprocessing.process(img)

            self.assertIsNotNone(img)
            self.assertEqual(2, len(img_normalized.shape))
            self.assertEqual(3, len(img_color.shape))

            self.assertEqual(img_normalized.shape, img_color.shape[0:2])

        preprocessed_image(img)
        preprocessed_image(img_black)


if __name__ == '__main__':
    unittest.main()
