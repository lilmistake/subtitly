from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

def audio_to_chunks(min_chunk_length: int, path: str, silence_thresh: int = -40, min_silence_len: int = 500) -> None:
    """
    Split an audio file into chunks at points of silence.

    This function takes an audio file and splits it into smaller chunks based on the presence of silence. The chunks are saved as separate audio files.

    Parameters
    ---
    min_chunk_length: int
        Minimum length of chunk in milliseconds
    path: str
        Path to audio file.
    silence_thresh: int
        Silence threshold in dB. Default is -40.
    min_silence_len: int
        Minimum length of silence in milliseconds. Default is 500.

    Returns
    ---
    None
    """
    print(f"Dividing Audio into chunks")
    audio = AudioSegment.from_file(path)

    chunks = split_on_silence(
        audio,
        keep_silence=True,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh    # Silence threshold in dB
    )

    """Merge small chunks to ensure minimum chunk length."""
    merged_chunks = []
    temp_chunk = None

    for chunk in chunks:
        if temp_chunk is None:
            temp_chunk = chunk
        else:
            temp_chunk += chunk

        if len(temp_chunk) >= min_chunk_length:
            merged_chunks.append(temp_chunk)
            temp_chunk = None

    # Add the last chunk if it's not empty
    if temp_chunk is not None:
        merged_chunks.append(temp_chunk)
    

    try:
        for i, chunk in enumerate(merged_chunks):
            chunk.export(f"./chunks/chunk{i}.mp3", format="mp3")
    except Exception as e:
        print("An error occured while writing audio chunks: "+str(e))
        return 0

    print(f"✅ Converted and saved audio in {len(merged_chunks)} chunks")
    return len(merged_chunks)