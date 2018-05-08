from context import wild_bee_watch

# https://docs.python.org/3/library/unittest.html

import unittest
import os


class TestConfigMethods(unittest.TestCase):

    def test_default_config(self):
        """
        Make sure that the default config is valid
        """
        config_loader = wild_bee_watch.config_loader.ConfigLoader()
        config = config_loader.load(os.path.dirname(
            __file__) + "/../config/config.yaml")
        self.assertIsNotNone(config)


if __name__ == '__main__':
    unittest.main()
