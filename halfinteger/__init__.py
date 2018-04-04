import os
import halfinteger.index
import halfinteger.slide
import halfinteger.blog
import yaml
from flask import Flask as BaseFlask, Config as BaseConfig


class Config(BaseConfig):

    def from_yaml(self, config_file):
        env = os.environ.get('FLASK_ENV', 'development')
        self['ENVIRONMENT'] = env.lower()

        with open(config_file) as f:
            c = yaml.load(f)

        c = c.get(env, c)

        for key in c:
            self[key.upper()] = c[key]


class Fine(BaseFlask):

    def load_config(self, filename='config.yml'):
        root_path = self.root_path
        config_path = os.path.join(root_path, filename)
        if not os.path.isfile(config_path):
            return
        self.config.from_yaml(config_path)

    def make_config(self, instance_relative=False):
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return Config(root_path, self.default_config)


app = Fine(__name__)
app.load_config()
app.register_blueprint(halfinteger.index.blueprint)
app.register_blueprint(halfinteger.slide.blueprint, url_prefix='/slides')
app.register_blueprint(halfinteger.blog.blueprint, url_prefix='/blog')
