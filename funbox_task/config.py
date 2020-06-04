import yaml


class RedisConfig(object):
    def __init__(self, config_path='../redis_config.yaml'):
        self._config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        with open(self._config_path) as f:
            yaml_config = yaml.safe_load(f)
            return yaml_config

    def get_config(self):
        return self.config
