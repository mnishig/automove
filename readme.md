# Automove file

## What?
This application is monitoring a folder and new created file move to target folder.<br>
Microsoft Edge / Teams and more will download file to Download folder in User profile folder. <br>
But I want to store it other location. some application can customize to other location and some application can not change.
<br>
This app to automate moving file that Download folder to want location.

example:<br>
1. watch os default Download directory 
1. created file at watched directory then move to user-specific directory (eg: C:\my-docs)

## usage
```
$ python3 -m vev env
$ env/scripts/activate # windows
or
$ env/bin/activate  # Linux or MacOS 
$ python3  src\app.py
```
<br>

## configuration
config.json contains these Keyes. You must adjust your want

| Key | description |
|-----|-------------|
| source_dir | Directory watching by app |
| target_dir | File copied to this Directory |
<br>

## dependencies
- pypi watchdog
<br>

### TODOS:
- add logger
- add user friendly error handler
- packaging