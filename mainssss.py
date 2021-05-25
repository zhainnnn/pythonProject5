import subprocess
import os,sys


subprocess.call(args='ipconfig')
os.system('ipconfig')
python_file_path=sys.executable
pythonw_file_path = '\\'.join(python_file_path.split('\\')[:-1] + ['pythonw.exe'])
print(python_file_path)
print(pythonw_file_path)
def mains():

    pass