# Deployment Process
Note that the official way to use streamlit is to launch your app in a server and share the URL.  
There is no official way to build an one-click executable out of my code.
Here is a workaround I found in this [website](https://discuss.streamlit.io/t/using-pyinstaller-or-similar-to-create-an-executable/902), and this [repo](https://github.com/jvcss/PyInstallerStreamlit).


Here I'd like to log how I deploy my code based on their experiences.  
1. Build the main.py and youtube.py. Normally we execute "streamlit run main.py" to launch the app. Now we wrap the main script:
    - Make a wrapper script `run_main.py`
     
            from streamlit.web import cli
            if __name__ == '__main__':
                cli._main_run_clExplicit('main.py', args=['run'])

    - Add the magic function in the `.venv/lib/site-packages/streamlit/web/cli.py` file.

            def _main_run_clExplicit(file, is_hello=False, args=[], flag_options={}):
                bootstrap.run(file, is_hello, args, flag_options) 

2. Create `./hooks/hook-streamlit.py`:

        from PyInstaller.utils.hooks import copy_metadata
        datas = copy_metadata('streamlit')

3. Create `./.streamlit/config.toml`:  

        [global]
        developmentMode = false

        [server]
        port = 8501

4. Compile the app `pyinstaller --onefile --additional-hooks-dir=./hooks run_main.py --clean`
5. Edit `run_main.spec`:

        ...
        a = Analysis(
            ...
            datas=[
                (".env/Lib/site-packages/altair/vegalite/v5/schema/vega-lite-schema.json",
                "./altair/vegalite/v5/schema/"),
                (".env/Lib/site-packages/streamlit/static",
                "./streamlit/static"),
                (".env/Lib/site-packages/streamlit/runtime",
                "./streamlit/runtime"),
            ],
            hiddenimports=['pytubefix'],
            ...
        )
        ...

6. Build the executable `pyinstaller run_app.spec --clean`
7. The executable file `run_main.exe` in the `dist` folder created above does not work alone.
You should copy `.streamlit`, `main.py` and `youtube,py` into the `dist` directory.