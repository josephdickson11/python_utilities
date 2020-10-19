import os.path
from datetime import datetime, date
from pathlib import Path
import beepy

# create variables to use
today = datetime.date(datetime.now())
path = Path(input("please type in directory path:  "))
log_extension = ".log"


# create success alert tone
def success_alert():
    beepy.beep(6)


# create error alert tone
def error_alert():
    beepy.beep(2)


# create a function to check if log_directory path exists
def check_path(path):
    if os.path.exists(path):
        print("file path exists")
    else:
        error_alert()
        print(f'{path} does not exist')


# create function to check if path is a directory
def confirm_directory(path):
    if os.path.isdir(path):
        print(f'{path} is a directory, we are good to go')
    else:
        error_alert()
        print(f'{path} is not a directory, change path and try again')


# check for sub folders and iterate through them to create file_path and delete all log files created today
def create_file_path(path):
    for base_folder, folder, files in os.walk(path):
        # check for files
        for file in files:
            # create file_path
            file_path = os.path.join(base_folder, file)

            # getting file extension
            file_extension = os.path.splitext(file_path)[1]

            # compare file extension with log_extension
            if log_extension == file_extension:
                # check file properties for set condition
                # get date file was last modified
                timestamp = date.fromtimestamp(path.stat().st_ctime)

                if date.today() == timestamp:
                    if not os.remove(file_path):
                        success_alert()
                        print(f'{file_path} removed successfully')
                    else:
                        print(f'Unable to delete {file_path}')
            else:
                print(f'{file_path} is not a log file')


def main():
    check_path(path)

    confirm_directory(path)

    create_file_path(path)


# call main function
if __name__ == '__main__':
    main()
