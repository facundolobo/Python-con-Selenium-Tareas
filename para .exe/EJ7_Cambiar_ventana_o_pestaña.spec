# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['EJ7_Cambiar_ventana_o_pestaña.py'],
             pathex=['C:\\Users\\ARMAGEDOM\\Desktop\\CURSO SELENIOM CON PYTHON\\ejemplos python selenium\\para .exe'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='EJ7_Cambiar_ventana_o_pestaña',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='EJ7_Cambiar_ventana_o_pestaña')
