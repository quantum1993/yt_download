# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['run_main.py'],
    pathex=[],
    binaries=[],
    datas=[
            (".venv/Lib/site-packages/altair/vegalite/v5/schema/vega-lite-schema.json",
            "./altair/vegalite/v5/schema/"),
            (".venv/Lib/site-packages/streamlit/static",
            "./streamlit/static"),
            (".venv/Lib/site-packages/streamlit/runtime",
            "./streamlit/runtime"),
        ],
    hiddenimports=['pytubefix'],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
