import yaml


class ConfigLoader:
    def __init__(self):
        pass

    def load(self, config_filename='../config/config.yaml'):

        with open(config_filename, 'r') as config_file:
            # https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
            try:
                config = yaml.load(config_file)
                return config
            except yaml.YAMLError as exc:
                print(exc)
