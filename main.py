import os
import shutil
import send2trash
import datetime

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

print('\n\n\n‣Exercising with datetime module')

print('\n‣Hello!')
print('\n->Trying time object<-')
hour = int(input('\n‣Give me an hour: '))
minute = int(input('\n‣Give me some minutes: '))
seconds = int(input('\n‣Give me some seconds: '))
print('\n‣You can give me even milliseconds ;). If you want. If not, press enter x')
milliseconds = input('\n‣Enter milliseconds: ')
if milliseconds in ['x', 'X']:
    time = datetime.time(hour, minute, seconds)
else:
    time = datetime.time(hour, minute, seconds, int(milliseconds))
print('\n‣Hi, I am a time object: ')
print(f'\n‣Hour is: {time.hour}')
print(f'\n‣Minutes are: {time.minute}')
print(f'\n‣Seconds are: {time.second}')
print(f'\n‣Milliseconds are: {time.microsecond}')
print(f'\n‣Min value is: {time.min}')
print(f'\n‣Max value is: {time.max}')


print('\n->Trying date object<-')

date = datetime.date
print('\n‣Taking date automatically')
date = date.today()
print(f'\n‣Date is: {date}')
print('\n‣But you can give me a date also: ')
year = int(input('\n‣Enter year: '))
month = int(input('\n‣Enter month(number between 1 and 12): '))
day = int(input('\n‣Enter day(number between 1 and 31): '))
date2 = datetime.date(year, month, day)
print(f'\n‣Date is: {date2}')
print(f'\n‣Min value is: {date2.min}')
print(f'\n‣Max value is: {date2.max}')
print('\n‣You can change the year for example')
new_year = int(input('\n‣Enter a new year: '))
date2 = date.replace(year=new_year)
print(f'\n‣New date is: {date2}')
print(f'\n‣Another way to print date: {date2.ctime()}')


print('\n->Trying datetime object<-')

print('\n‣Taking date and time automatically')
datetime1 = datetime.datetime.today()
print(f'\n‣First method: {datetime1}')
datetime2 = datetime.datetime.now()
print(f'\n‣Second method: {datetime1}')
print(f'\n‣Min value is: {datetime2.min}')
print(f'\n‣Max value is: {datetime2.max}')
print(f'\n‣Printing with ctime(): {datetime2.ctime()}')
datetime3 = datetime.datetime(2021, 5, 12, 22, 5, 45)
datetime4 = datetime.datetime(2020, 5, 12, 12, 5, 45)
print(f'\n‣Difference between dates is: {datetime3 - datetime4}')
datetime5 = datetime.datetime(2022, 4, 5, 21, 5, 6)
print('\n‣', datetime5)

print('That is all. Goodbye! ;)')
