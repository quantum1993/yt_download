# from pytube import YouTube
from pytubefix import YouTube
# from pytubefix.cli import on_progress
import streamlit as st
import os


class DownloadYoutube():
    def __init__(self, link, format='mp4', file_name=None, resolution='highest', default_folder='downloaded_files', progress_bar=None):
        self.link = link
        self.format = format
        self.file_name = file_name
        self.resolution = resolution
        self.default_folder = default_folder
        self.progress_bar = progress_bar
        self.is_error = False
        self.error_msg = ""
        self.display_msg = ""

        self.check_default_value()


    def check_default_value(self):
        # check if the link is valid
        if self.link is None or self.link == "":
            self.is_error = True
            self.error_msg += 'link is empty'

        # check if the format is valid
        allowed_format_list = ["mp4", "mp3"]
        if self.format not in allowed_format_list:
            self.is_error = True
            self.error_msg += f'format should be one of options: {",".join(allowed_format_list)}. Find {self.format}' 

        # check if the default_folder exists
        if not os.path.isdir(self.default_folder):
            os.mkdir(self.default_folder)

        # check if the resolution is valid
        allowed_resolution_list = ["highest", "1080p", "720p", "360p", "240p", "120p"]
        if self.resolution not in allowed_resolution_list:
            self.is_error = True
            self.error_msg = f'resolution should be one of options: {",".join(allowed_resolution_list)}. Find {self.format}' 


    def reset_file_name(self):
        if self.file_name is None or self.file_name == "":
            self.file_name = self.yt.title


    def onProgress(self, stream, chunk, remains):
        total = stream.filesize                     # get file size
        percent = (total-remains) / total * 100     # calculate the remain percentage
        msg = f'Downloading… {percent:05.2f}%'
        print(msg)
        # self.display_msg += f"{msg}\n"
        # st.session_state["text_area"] = f"{self.display_msg}"
        if self.progress_bar is not None:
            self.progress_bar.progress((total-remains) / total, text=msg)


    def connect_yt(self):
        try:
            self.yt = YouTube(self.link, on_progress_callback=self.onProgress)
            self.reset_file_name()

            self.display_msg += f"Title: {self.yt.title} \nlength of the video: {self.yt.length} s \nAuthor: {self.yt.author} \n"
            print(f"title: {self.yt.title}")
            print(f"length of the video: {self.yt.length}") 
            print(f"author: {self.yt.author}") 
            # print(self.yt.channel_url)     # 影片作者頻道網址
            # print(self.yt.thumbnail_url)   # 影片縮圖網址
            # print(self.yt.views)           # 影片觀看數
        except Exception as e:
            self.is_error = True
            self.error_msg = e
            print(e)


    def download(self):
        filename = f'./{self.default_folder}/{self.file_name}.{self.format}'
        msg = f"Download to {filename}"
        print(msg)
        self.display_msg += f"{msg}\n"
        
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
            self.display_msg += "Done!\n"
            print('-'*50)
        except Exception as e:
            self.is_error = True
            self.error_msg = e
            print(e)


if __name__ == "__main__":
    # run python ./youtube.py
    # https://www.youtube.com/watch?v=asU8O_R5V6w&ab_channel=JunSeong
    link = 'https://www.youtube.com/watch?v=2Mo0Zq8ORoE&ab_channel=%E5%92%AA%E8%95%BE%EB%AF%B8%EB%9E%98'
    dy = DownloadYoutube(link=link)
    dy.download()
