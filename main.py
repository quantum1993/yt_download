from pytube import YouTube

def onProgress(stream, chunk, remains):
    total = stream.filesize                     # 取得完整尺寸
    percent = (total-remains) / total * 100     # 減去剩餘尺寸 ( 剩餘尺寸會抓取存取的檔案大小 )
    print(f'Downloading… {percent:05.2f}%')  # 顯示進度，\r 表示不換行，在同一行更新

yt_link = 'https://www.youtube.com/watch?v=asU8O_R5V6w&ab_channel=JunSeong'
yt = YouTube(yt_link, on_progress_callback=onProgress)
print(yt.title)           # 影片標題
print(yt.length)          # 影片長度 ( 秒 )
print(yt.author)          # 影片作者
print(yt.channel_url)     # 影片作者頻道網址
print(yt.thumbnail_url)   # 影片縮圖網址
print(yt.views)           # 影片觀看數



print('download...')
yt.streams.filter().get_highest_resolution().download(filename=f'./downloaded_files/{yt.title}.mp4') #./downloaded_files/
# 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
print('ok!')