# -*- mode: python -*-

block_cipher = None

added_files = [
         ( './templates/', 'templates' ),
         ( './static/', 'static' ),
         ]

a = Analysis(['app.py'],
             pathex=['./'],
             binaries=[],
             datas=added_files,
             hiddenimports=['wtforms', 'jinja2'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='app',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon='static/images/favicon.ico')
          
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='app')
