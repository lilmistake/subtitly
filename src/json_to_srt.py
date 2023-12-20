def convert_json_to_srt(json_data, startId:int = 0, startTime: int = 0):
    """
    Converts a JSON object containing segmented audio data into SRT (SubRip Text) format.

    This function takes a JSON object with audio segments, each containing start and end times and text, and converts them into SRT format.

    Parameters
    ---
    json_data: dict
        JSON object containing audio segment data.
    startId: int
        Starting ID for the SRT segments. Default is 0.
    startTime: int
        Starting time offset for the SRT segments in seconds. Default is 0.

    Returns
    ---
    str
        The SRT formatted string.
    """
    end_time = 0
    def format_time(seconds):
        """Converts time in seconds to SRT time format."""
        ms = int((seconds % 1) * 1000)
        s = int(seconds)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return f'{h:02}:{m:02}:{s:02},{ms:03}'

    srt_output = []

    for segment in json_data['segments']:
        start = format_time(segment['start']+startTime)
        end = format_time(segment['end']+startTime)
        end_time= segment['end']+startTime
        text = segment['text'].strip()
        srt_output.append(f"{segment['id'] + 1 + startId}\n{start} --> {end}\n{text}\n")

    return ['\n'.join(srt_output), len(srt_output), end_time]
