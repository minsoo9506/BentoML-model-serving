import os

import pandas as pd
import requests

from config.core import DATASET_PATH, config

path = os.path.join(DATASET_PATH, config.app_config.test_data_file)
sample_data = (
    pd.read_csv(path, usecols=config.model_config.features).iloc[0, :].to_json()
)

print(sample_data)

requests.post(
    "http://localhost:3000/predict",
    headers={"content-type": "application/json"},
    data=sample_data,
).text
