import streamlit as st
from youtube import DownloadYoutube
 
# init variables and create placeholder
st.set_page_config(page_title="Youtube Downloader")
st.write("Youtube Downloader")
link = st.text_input("Enter the link:")
resolution = st.text_input("Resolution:", value='highest')
format = st.text_input("Format:", value='mp4')
folder_path = st.text_input("Folder path:", value='downloaded_files')
file_name = st.text_input("File name (leave it empty if you'd like to use default file name):")

if "text_area" not in st.session_state:
    st.session_state["text_area"] = ""

st.text_area("Result", value=st.session_state["text_area"], height=200)
bar = st.progress(0)

# define on_click function
def trigger_download():
    st.session_state["text_area"] = ""
    dy = DownloadYoutube(link=link, format=format.lower(), file_name=file_name, resolution=resolution.lower(), default_folder=folder_path, progress_bar=bar)
    if dy.is_error:
        st.session_state["text_area"] = f"Error: {dy.error_msg}"
    else:
        dy.connect_yt()
        if dy.is_error:
            st.session_state["text_area"] = f"Error: {dy.error_msg}"
        else:
            st.session_state["text_area"] = f"{dy.display_msg}"
            dy.download()
            if dy.is_error:
                st.session_state["text_area"] = f"Error: {dy.error_msg}"
            else:
                st.session_state["text_area"] = f"{dy.display_msg}"

def trigger_test():
    st.session_state["text_area"] = ""
    dy = DownloadYoutube(link=link, format=format.lower(), file_name=file_name, resolution=resolution.lower(), default_folder=folder_path, progress_bar=bar)
    if dy.is_error:
        st.session_state["text_area"] = f"Error: {dy.error_msg}"
    else:
        dy.connect_yt()
        if dy.is_error:
            st.session_state["text_area"] = f"Error: {dy.error_msg}" 
        else:
            st.session_state["text_area"] = f"{dy.display_msg}\n Test Successfully!"


col1, col2, _, _, _ = st.columns([1,1, 1, 1, 0.5])
with col1:
    st.button(label="Test Connection", on_click=trigger_test)
with col2:
    st.button(label='Download', on_click=trigger_download)

  # run command "streamlit run main.py" to launch the app in your local server
  # plz refer to the deployment.md if you'd like to deploy as a executable
