from context import wild_bee_watch

import unittest


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


if __name__ == '__main__':
    unittest.main()
