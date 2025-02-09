import yt_dlp
import os


def download_and_convert_to_mp3(video_url, keepvideo):
    """Download the MP3 file from a Youtube URL.

    Args:
        video_url (str): URL of the video to download.
    """
    vals = {
        "format": "bestaudio/best",  # Choose the file format, bestaudio/best is generally ".webm or .m4a"
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",  # Extract audio from video
                "preferredcodec": "mp3",  # Convert it to mp3
                "preferredquality": "192",  # Set the quality to 192 kbps (balanced)
            }
        ],
        "outtmpl": os.path.expanduser(
            "~/Downloads/Mp3Converts/%(title)s.%(ext)s"
        ),  # Output path, currently: /home/_user_/Downloads/Mp3Converts/_file_
        "keepvideo": keepvideo,
    }
    ytdl = yt_dlp.YoutubeDL(vals)
    try:
        ytdl.download([video_url])
    except Exception as e:
        print(f"Error while downloading the video: {e}")


def main():
    video_url = input("Enter a valid URL: ").strip()

    while True:
        prompt = (
            input("Do you wish to keep both files after post-processing? (y/n): ")
            .lower()
            .strip()
        )
        if prompt in ["y", "yes", "yup", "ye", "yeah"]:
            keepvideo = True
            break
        elif prompt in ["n", "no", "nop", "nope", "nah"]:
            keepvideo = False
            break
        else:
            print("Try Again!")

    download_and_convert_to_mp3(video_url, keepvideo)


if __name__ == "__main__":
    main()
