from collections.abc import Mapping
from src.json_to_srt import convert_json_to_srt

def prediction_to_subs(predictions: Mapping[str, ]):
    """ 
    Converts predictions received from Replicate to SRT/VTT file format

    Parameters
    ---
    predictions: Mapping[str, ]
        The map of prediction ID to its object

    Returns
    ---
    str
        The subtitles in SRT/VTT format
    """
    subs = ''
    current_index = 0
    current_time = 0
    for prediction in predictions.values():
        response = convert_json_to_srt(
            prediction['prediction'],
            startTime=current_time,
            startId=current_index
        )
        subs = subs + response[0] +'\n'
        current_index+=response[1]
        current_time=response[2]+0.1
    return subs
