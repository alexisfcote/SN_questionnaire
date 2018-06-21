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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SN Journal de bord',
          debug=False,
          strip=False,
          upx=False,
          console=False,
          icon='static/images/favicon.ico' )
