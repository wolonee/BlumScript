# -*- mode: python -*-
options = [ ('v', None, 'OPTION')]
block_cipher = None


a = Analysis(['TonscoB3.py'],
             pathex=['f:\\Python\\Blum\\BlumScrpt', 'D:\\py36envtest\\venv_py36\\Lib\\site-packages\\scipy\\extra-dll' ],
             binaries=[],
             datas=[],
             hiddenimports=['psutil'],
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
          name='Tonsco_Helloween',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True,
          icon='B5.ico')