import streamlit as st
from youtube import DownloadYoutube
 
st.write("Youtube Downloader")
link = st.text_input("Enter the link:")
resolution = st.text_input("Resolution:", value='highest')
format = st.text_input("Format:", value='mp4')
folder_path = st.text_input("Folder path:", value='downloaded_files')
file_name = st.text_input("File name (leave it empty if you'd like to use default file name):")

def trigger_download():
    dy = DownloadYoutube(link=link, format=format.lower(), file_name=file_name, resolution=resolution.lower(), default_folder=folder_path)
    st.text_area('Result : ', 
                 f"""title: {dy.yt.title} \n length of the video: {st.yt.length} \n""")
    # dy.download()
    print(link, resolution, format, folder_path, file_name)

st.button(label='Download', on_click=trigger_download)

# run command "streamlit run main.py"
