import os
import yt_dlp


def get_list_of_videos(file_path: str = 'list_of_videos.txt') -> list:
    video_list = []
    with open(file_path, 'r') as file:
        for line in file:
            video_list.append(line.strip())

    return video_list


def download_video(video_list: list):
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(video_list)


def main() -> None:
    video_list = get_list_of_videos()

    videos_path = os.path.join(os.getcwd(), 'videos')
    if not os.path.exists(videos_path):
        os.makedirs(videos_path)
    os.chdir(videos_path)

    download_video(video_list)


if __name__ == '__main__':
    main()
