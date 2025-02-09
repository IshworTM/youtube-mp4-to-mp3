# Youtube MP4 to MP3 converter

This script allows you to download audio from YouTube videos and convert them into MP3 files without having to watch a billion ads or be redirected to malicious websites (not targeting any websites btw). The downloaded MP3 file will be stored in the `~/Downloads/Mp3Converts/` directory.

## Features (what makes it different from the standard yt-dlp)

- Clear and straight forward implementation of the standard library.
- Direct and clear prompts.
- Specifically made for Youtube but works for other websites too (standard library function).
- Minimal setup, simply install the two dependencies and run the script.
- Automatically converts to MP3 with specified bitrate (192 kbps), no extra configuration required.
- Saves directly to your downloads folder.
- Option to keep the original video file after post-processing.

## Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (a YouTube video downloader)
- [FFmpeg](https://ffmpeg.org/) (for audio conversion)

You can install the required dependencies using the following commands or by visiting the link above:

```bash
pip install yt-dlp
```

``` bash
sudo apt install ffmpeg
```

## How to Use

1. Clone or download this repository.

2. Run the script with the following command:

    ``` bash
    python3 main.py
    ```

3. When prompted, enter a valid YouTube video URL.

4. Choose whether or not to keep both files after post-processing (y or n).

5. The MP3 file will be saved in the ~/Downloads/Mp3Converts/ directory.

## Customization

You can modify the output directory and the quality of the MP3 file or essentially anything you want directly from the script.
The default output path is set to `~/Downloads/Mp3Converts/filename.ext`.

## License

This project is licensed under The Unlicense. See the LICENSE file for more information.
