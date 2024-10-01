# from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def onProgress(stream, chunk, remains):
    total = stream.filesize                     # get file size
    percent = (total-remains) / total * 100     # calculate the remain percentage
    print(f'Downloading… {percent:05.2f}%')  


class DownloadYoutube():
    def __init__(self, link, format='mp4', file_name=None, resolution='highest', default_folder='downloaded_files'):
        self.link = link
        self.format = format
        self.file_name = file_name
        self.resolution = resolution
        self.default_folder = default_folder
        self.is_error = False
        self.error_msg = ""

        if not os.path.isdir(self.default_folder):
            os.mkdir(self.default_folder)

        self.yt = YouTube(self.link, on_progress_callback=on_progress)

        print(f"title: {self.yt.title}")
        print(f"length of the video: {self.yt.length}") 
        print(f"author: {self.yt.author}") 
        # print(self.yt.channel_url)     # 影片作者頻道網址
        # print(self.yt.thumbnail_url)   # 影片縮圖網址
        # print(self.yt.views)           # 影片觀看數

    def check_default_value(self):
        if self.link is None or self.link == "":
            self.is_error = True
            self.error_msg = 'link is empty'

        allowede_format_list = ["highest", "1080p", "720p", "360p", "240p", "120p"]
        if self.format not in allowede_format_list:
            self.is_error = True
            self.error_msg = f'format should be one of options: {",".join(allowede_format_list)}. Find {self.format}' 

        if self.file_name

    def download(self):
        print('Start downloading!')
        filename = f'./{self.default_folder}/{self.yt.title}.{self.format}'
        try:
            if format == 'mp3':
                self.yt.streams.filter(only_audio=True)\
                    .download(filename=filename)
            elif self.resolution == 'highest':
                self.yt.streams.filter(file_extension=self.format)\
                    .get_highest_resolution()\
                    .download(filename=filename)
            else: 
                # self.resolution could be 720p、480p、360p、240p if the video supports
                self.yt.streams.filter(file_extension=self.format)\
                    .get_by_resolution(self.resolution)\
                    .download(filename=filename)
                
            print('Done!')
            print('-'*50)
        except Exception as e:
            raise SystemError(e)


if __name__ == "__main__":
    # run python ./youtube.py
    # https://www.youtube.com/watch?v=asU8O_R5V6w&ab_channel=JunSeong
    link = 'https://www.youtube.com/watch?v=2Mo0Zq8ORoE&ab_channel=%E5%92%AA%E8%95%BE%EB%AF%B8%EB%9E%98'
    dy = DownloadYoutube(link=link)
    dy.download()
