import os
import shutil
import send2trash

print('Working with OS, shutil and send2trash modules')
print('\n‣Hello!')
print('\n‣I will create a file and I will show what can I do with it')
print('\n‣Name of the file will be \'test.txt\' ')
file = open('test.txt', 'w')
file.close()
print(f'\n‣The file\'s location is: {os.getcwd()}')
print(f'\n‣Other files from this location are: {os.listdir()}')
print('\n‣Now I will move this file to D directory')
shutil.move('test.txt', 'D:\\')
print(f'\n‣Files from D directory are {os.listdir("D:")}')
print('\n‣Now I will send the \'text.txt\' file to trash')
send2trash.send2trash('D:\\test.txt')
print('\n‣Done! Look, there is no \'test.txt\' file. Look in recycle bin.')
print(f'\n‣Files from D directory now: {os.listdir("D:")}')
print('\n‣I can also do another interesting things like deleting files completely')
print('\n‣I will create another file called \'text2.txt\' file in this directory')
file = open('test2.txt', 'w')
file.close()
print('\n‣Look! It is here.')
print(os.listdir())
os.unlink('test2.txt')
print('\n‣I just deleted it:')
print(os.listdir())
print('\n‣See? It is not here neither, nor in the recycle bin.')
print('\n‣I want to show you one more thing. I can list everything inside a folder.'
      '\n‣But don\'t give me a big folder because the output will be a completely mess. Yhank you! ;)')

print('\n‣Create a file on your desktop and put some things there, you can also create folders')

folder_name = input('\n‣Copy and paste the location of folder here: ')
for dirpath, dirnames, files in os.walk(folder_name):
    print(f'Looking at: {dirpath}')
    print(f'\t Directories are: {dirnames}')
    print(f'\t Files are: {files}')

print('That is all. Goodbye! ;)')
