import os
from typing import List

import yaml
from pydantic import BaseModel, Field

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_PATH = os.path.join(
    ROOT_DIR, '../', 'config.yaml')


class AppConfig(BaseModel):
    addr: str = Field(alias="addr", default="0.0.0.0")
    port: int = Field(alias="port", default=9000)
    nodes: List[str] = Field(alias="nodes", default=[])


def read(file_name):
    try:
        with open(file_name, "r") as f:
            yamlConfig: AppConfig = yaml.load(f, Loader=yaml.FullLoader) or {}

            config = AppConfig(**yamlConfig)

            return config

    except:

        return AppConfig()


def get_app_config():
    return read(CONFIG_PATH)
