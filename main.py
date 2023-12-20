from collections.abc import Mapping
from src.video_to_audio import video_to_audio
from src.audio_to_chunks import audio_to_chunks
from src.prediction import ensure_prediction_completion, start_prediction
from src.write_file import write_file
from src.user_input import user_input
from src.prediction_to_subs import prediction_to_subs


predictions: Mapping[str, ] = {}

def main():
    video_path, answers = user_input()
    if answers is None or video_path is None:
        return
    
    min_chunk_length = int(answers['size'])*1000
    silence_threshold = int(answers['volume'])
    min_silence_len = int(answers['silence'])

    audio_path = video_to_audio(video_path)
    if audio_path is None:
        return
    
    chunk_count = audio_to_chunks(min_chunk_length, audio_path, silence_threshold, min_silence_len)
    if chunk_count is None or chunk_count == 0:
        return
    
    print(f"Starting Prediction Process")
    for i in range(0,chunk_count):
        id = start_prediction(f'./chunks/chunk{i}.mp3')
        predictions[id] = {
            "status": 'processing',
            "prediction": ""
        }
        print(f"Started Prediction for Chunk #{i}")

    if len(predictions) == 0:
        print("Error: Couldn't make predictions")
        return
    
    ensure_prediction_completion(predictions)
    print("✅ All Predictions completed")
    subs = prediction_to_subs(predictions)
    write_file(subs, answers['format'])
    print("✅ Subtitles created successfully")


if __name__ == '__main__':
    main()