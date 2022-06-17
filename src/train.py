import pandas as pd
from sklearn.linear_model import LogisticRegression

from config.core import config


def get_logistic_model(
    scaled_X_train: pd.DataFrame, y_train: pd.Series
) -> LogisticRegression:
    """fitting logistic model and return it

    Parameters
    ----------
    scaled_X_train : pd.DataFrame
        _description_
    y_train : pd.Series
        _description_

    Returns
    -------
    LogisticRegression
        _description_
    """
    clf = LogisticRegression(random_state=config.model_config.random_state)
    clf.fit(scaled_X_train, y_train)
    return clf
