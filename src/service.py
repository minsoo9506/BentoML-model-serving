import bentoml
import numpy as np
import pandas as pd
from bentoml.io import JSON, NumpyNdarray

# Load processors and model


class scalerRunnable(bentoml.Runnable):
    """_summary_

    Parameters
    ----------
    bentoml : _type_
        _description_
    """

    def __init__(self):
        self.model = bentoml.sklearn.load_model("scaler:latest")

    @bentoml.Runnable.method(batchable=False)
    def transform(self, input_data) -> np.ndarray:
        """_summary_

        Parameters
        ----------
        input_data : _type_
            _description_

        Returns
        -------
        np.ndarray
            _description_
        """
        return self.model.transform(input_data)


scaler = bentoml.Runner(scalerRunnable)
classifier = bentoml.sklearn.get("model:latest").to_runner()

# Create service
service = bentoml.Service("fraud_detection", runners=[scaler, classifier])


@service.api(input=JSON(), output=NumpyNdarray())
def predict(input_json: JSON) -> np.ndarray:
    """_summary_

    Parameters
    ----------
    input_json : JSON
        _description_

    Returns
    -------
    np.ndarray
        _description_
    """

    df = pd.DataFrame(input_json, index=[0])

    # Process data
    scaled_df = pd.DataFrame(scaler.run(df), columns=df.columns)

    # Predict
    result = classifier.run(scaled_df)
    return np.array(result)
