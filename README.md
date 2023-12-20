# Video Subtitle Generator

## Description
This Python project automates the process of adding subtitles to videos. It includes various scripts to convert videos to audio, split audio into chunks, perform speech recognition, and generate subtitles in SRT/VTT format.

## Installation

### Prerequisites
- **FFmpeg**: This project requires FFmpeg for video to audio conversion. 
  - **Windows**: Download and install from [FFmpeg's official website](https://ffmpeg.org/download.html).
  - **macOS**: Install using Homebrew with `brew install ffmpeg`.
  - **Linux**: Install using your distribution's package manager, for example `sudo apt-get install ffmpeg` for Debian/Ubuntu.
### Python Dependencies

To install the necessary dependencies, run the following command in your terminal:
```bash
pip install -r requirements.txt
```

## Setting Up the Environment

Before running the script, you need to set up the `REPLICATE_API_TOKEN`. Get your API token from the [Replicate website](https://replicate.com/), and then set it as an environment variable. 

On Unix-based systems, you can set the environment variable like this:
```bash
export REPLICATE_API_TOKEN='your_token_here'
```
For Windows, use the following command in Command Prompt:
```cmd
set REPLICATE_API_TOKEN=your_token_here
```

## Usage
To use this tool, simply run the `main.py` script:
```bash
python main.py
```
Follow the on-screen instructions to select a video file and specify any required settings or options.

## Acknowledgments
This project utilizes several external libraries including `pydub`, `replicate`, and `tkinter`. Thanks to the developers and contributors of these libraries.

## License
This project is released under the MIT License.