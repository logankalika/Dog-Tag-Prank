#Dog Tagging 
#Ha. ha.. ha... that was not a very funny prank LMAO
#use the default path to test System/system_background.py'

#brings the pathlib module and imports the Path module
from pathlib import Path

#creates a variable for the system_background.py file inside the System directory 
print('A "Dog Tag" in this program is a message you would like to leave in a file. This erases Everything else in the file.')
print('What file would you like to "Dog Tag"? BE SPECIFIC. Example System/system_background.py')
path_input = input()
system_path = Path(path_input)

#if the system_background.py file inside the System directory exists then
if system_path.exists(): 
    print('Type the "Dog Tag" you would you like to leave?')
    dog_tag = input()
    print('All data currently inside ', (system_path), ' will be deleted.')
    print('Are you sure you want to continue? Type yes to continue.')
    yes_or_break = input()
    if yes_or_break == 'yes':
        #creates a variable to open the system_background.py file inside the System Directory using UTF-8 compatibility MacOS and Linux
        opened_file = system_path.open(encoding='UTF-8')
        #creates a variable to write text inside the opened file trunicating all old data
        write_file = system_path.write_text(dog_tag)
        #creates  a variable to close the opened file
        close_file = opened_file.close()
        print(''''File successfully "Dog Tagged", trunicating all old information''')
    else:
        print('Operation has been cancelled')
