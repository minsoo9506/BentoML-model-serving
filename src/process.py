from typing import List, Tuple

import pandas as pd
from sklearn.preprocessing import StandardScaler

from config.core import config


def load_data(data_name: str) -> pd.DataFrame:
    """load data

    Parameters
    ----------
    data_name : str
        path of data

    Returns
    -------
    pd.DataFrame
        _description_
    """
    data = pd.read_csv(data_name)
    return data


# 여기에 config.feature 추가
def get_scaler(
    df: pd.DataFrame, features: List[str] = config.model_config.features
) -> StandardScaler:
    """fit StandardScaler and return it

    Parameters
    ----------
    df : pd.DataFrame
        _description_
    features : List[str], optional
        list of train features, by default config.model_config.features

    Returns
    -------
    StandardScaler
        _description_
    """

    scaler = StandardScaler()
    scaler.fit(df[features])

    return scaler


def scale_features(
    df: pd.DataFrame,
    scaler: StandardScaler,
    features: List[str] = config.model_config.features,
) -> pd.DataFrame:
    """scale data

    Parameters
    ----------
    df : pd.DataFrame
        _description_
    scaler : StandardScaler
        _description_
    features : List[str], optional
        list of train features, by default config.model_config.features

    Returns
    -------
    pd.DataFrame
        scaled data
    """
    return pd.DataFrame(scaler.transform(df[features]), columns=features)


def process_data(
    df: pd.DataFrame, features: List[str] = config.model_config.features
) -> Tuple[StandardScaler, pd.DataFrame, pd.Series]:
    """from data load to scaled data

    Parameters
    ----------
    df : pd.DataFrame
        _description_
    features : List[str], optional
        _description_, by default config.model_config.features

    Returns
    -------
    Tuple[StandardScaler, pd.DataFrame, pd.Series]
        _description_
    """
    scaler = get_scaler(df, features)
    scaled_X_train = scale_features(df, scaler, features)
    y_train = df[config.model_config.target]
    return scaler, scaled_X_train, y_train
