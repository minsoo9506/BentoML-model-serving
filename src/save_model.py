import os

import bentoml

from config.core import DATASET_PATH, config
from process import load_data, process_data
from train import get_logistic_model

if __name__ == "__main__":
    # data load
    train_data_path = os.path.join(DATASET_PATH, config.app_config.train_data_file)
    df = load_data(train_data_path)
    # preprocessing
    scaler, scaled_X_train, y_train = process_data(df, config.model_config.features)
    # save scaler
    bentoml.sklearn.save_model("scaler", scaler)
    # model fit
    logit_model = get_logistic_model(scaled_X_train, y_train)
    # save logistic model
    bentoml.sklearn.save_model("model", logit_model)
