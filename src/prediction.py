import replicate
from collections.abc import Mapping
import time

def ensure_prediction_completion(predictions: Mapping[str, ]):
    """ 
    Makes recursive API calls with a 5 second delay to ensure all predictions are completed

    Parameters
    ---
    predictions: Mapping[str,]
        The map of prediction ID to its object
    """
    all_completed = True

    for i in predictions.keys():
        response = replicate.predictions.get(i)
        predictions[i]['status'] = response.status
        if(response.status == "processing" or response.status == 'starting'):
            all_completed = False
        else:
            predictions[i]['prediction'] = response.output

    if not all_completed:
        time.sleep(5)
        ensure_prediction_completion(predictions)


def start_prediction(path:str):
    """ 
    Starts transcription prediction for given path

    Parameters
    ---
    path: str
        The path of the audio file

    Returns
    ---
    str
        Prediction ID
    """
    res = replicate.predictions.create(
        version="4d50797290df275329f202e48c76360b3f22b08d28c196cbc54600319435f8d2",
        input={
            "audio": open(path, "rb"),
            "translate": True,
            "transctiption":"vtt",
        },
    )
    return res.id
