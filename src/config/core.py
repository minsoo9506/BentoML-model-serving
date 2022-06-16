import os
from typing import List

from pydantic import BaseModel
from strictyaml import YAML, load

ROOT = os.path.abspath(os.curdir)
SRC_PATH = os.path.join(ROOT, "src")
CONFIG_FILE_PATH = os.path.join(SRC_PATH, "config.yml")
DATASET_PATH = os.path.join(ROOT, "data")


class AppConfig(BaseModel):
    """App config

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    train_data_file: str
    test_data_file: str


class ModelConfig(BaseModel):
    """Model config

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    target: str
    features: List[str]
    test_size: float
    random_state: int


class Config(BaseModel):
    """Config (app_config, model_config)

    Parameters
    ----------
    BaseModel : _type_
        _description_
    """

    app_config: AppConfig
    model_config: ModelConfig


def fetch_config_from_yaml(cfg_path: str = CONFIG_FILE_PATH) -> YAML:
    """parse config.yml

    Parameters
    ----------
    cfg_path : str, optional
        path of config.yml, by default CONFIG_FILE_PATH

    Returns
    -------
    YAML
        _description_

    Raises
    ------
    OSError
        raised when config file not found at path
    """
    if not cfg_path:
        cfg_path = CONFIG_FILE_PATH

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def creat_and_validate_config(parsed_config: YAML = None) -> Config:
    """creat config and validata config with pydantic

    Parameters
    ----------
    parsed_config : YAML, optional
        _description_, by default None

    Returns
    -------
    Config
        _description_
    """
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    _config = Config(
        app_config=AppConfig(**parsed_config.data), model_config=ModelConfig(**parsed_config.data)
    )

    return _config


config = creat_and_validate_config()

print(config)
