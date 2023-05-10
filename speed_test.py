import subprocess

returned_text = subprocess.check_output('speedtest-cli', shell=True, universal_newlines=True)
print('The Result Speed Test')
print(returned_text)