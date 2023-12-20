import subprocess

def video_to_audio(videoPath:str):
    """
    Converts a video file to an audio file

    Parameters
    ---
    videoPath: str
        Path to the video file

    Returns
    ---
    str
        Path to the audio file
    """
    print("Converting video to audio")
    outputPath = videoPath.rsplit('.', 1)[0] + '.mp3'
    try:
        output = subprocess.run(
            ["ffmpeg", "-i", videoPath, outputPath],
        )
        if output.returncode == 0:
            print("✅ Conversion successful. Audio saved to:", outputPath)
            return outputPath
        else:
            print("Conversion failed:", output.stderr)
    except Exception as error:
        print("Error during conversion:", error)
