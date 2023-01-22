import shutil
from tkinter import filedialog
import pywhatkit as pwk  # pip install pywhatkit
from pytube import YouTube  # pip install pytube
import os
import webbrowser as wb  # pip install webbrowser
from googletrans import Translator  # pip install googletrans==4.0.0-rc1 (run on terminal + check inherit global packages)
from time import sleep
from pytube.cli import on_progress
from datetime import datetime


user = os.getlogin()
now = datetime.now()
hour = now.strftime('%H:%M')

time = now.strftime('%d/%m/%Y %H:%M')

if '06:00:00' < hour < '11:59:00':
    print(f'Bom Dia, {user}!')

elif '12:00:00' < hour < '17:59:00':
    print(f'Boa Tarde, {user}!')

elif '18:00:00' < hour < '23:59:00':
    print(f'Boa Noite, {user}!')

elif '00:00:00' < hour < '05:59:00':
    print(f'Boa Madrugada, {user}!')


while True:
    command = input('> ')

    if '!p' in command:
        search = command.replace('!p', '').strip()
        print(f'Searching {search} on YouTube...')
        pwk.playonyt(search)

    elif '!dlvideo' in command:
        link = command.replace('!dlvideo', '').strip()
        yt = YouTube(link, on_progress_callback=on_progress)

        path = filedialog.askdirectory()

        print(f'Selected path: {path}')

        sleep(0.5)

        file = yt.title + '.mp4'

        print('Searching video...')

        print(f'Starting download of {yt.title}...')

        ys = yt.streams.get_highest_resolution().download()

        shutil.move(file, path)

        print(yt.title + ' successfully downloaded!')

    elif '!dlaudio' in command:
        link = command.replace('!dlvideo', '').strip()  # remove the !dlaudio from the input
        yt = YouTube(link)  # get the video link

        path = filedialog.askdirectory()  # ask the folder to store the file

        print(f'Selected path: {path}')  # print the selected path

        sleep(0.5)

        # path = os.getcwd()  # folder to store the file

        print('Searching video...')  # notify the user

        print(f'Starting download of {yt.title}.mp3...')  # notify the user

        ys = yt.streams.filter(only_audio=True).first().download()  # download the file

        name = yt.title + '.mp4'  # specify the file name

        new_name = yt.title + '.mp3'  # specify the new file name

        os.rename(name, new_name)  # rename the file

        shutil.move(new_name, path)  # move the file to the selected path

        print(f'{yt.title}.mp3 successfully downloaded!')  # notify the user

    elif '!instapost' in command:

        post_link = command.replace('!instapost', '').strip()

        print('Note: To download photo from instagram, make sure you have '

              'instaloader installed. If not, on terminal paste "pip install instaloader"!')

        link_remove = post_link.replace('https://www.instagram.com/p/', '').strip()

        post_id = link_remove.split('/')
        download_link = f'instaloader -- -{post_id[0]}'

        # print(f'Paste on terminal: {download_link}')

        os.system(download_link)

        print('Photo downloaded successfully!')

    elif '!instareel' in command:

        reel_link = command.replace('!instareel', '').strip()

        print('Note: To download reel from instagram, make sure you have '

              'instaloader installed. If not, on terminal paste "pip install instaloader"!')

        link_remove = reel_link.replace('https://www.instagram.com/reel/',
                                        '').strip()

        reel_id = link_remove.split('/')

        download_link = f'instaloader -- -{reel_id[0]}'

        # print(f'Paste on terminal: {download_link}')

        os.system(download_link)

        print('Reel downloaded successfully!')

    elif '!google' in command:
        search = command.replace('!google', '').strip()
        pwk.search(search)
        print(f'Searching {search} on Google.')

    elif '!get' in command:
        link = command.replace('!get', '').strip()
        wb.open(link)

    elif '!bye' in command:
        exit()

    elif '!controls' in command:
        print('#############')
        print('COMMAND LIST:\n'
              'Play a Video on YouTube = !p + "VIDEO NAME"\n'
              'Download YouTube Video = !dlvideo + "VIDEO URL"\n'
              'Download YouTube Audio = !dlaudio + "VIDEO URL"\n'
              'Open a Website = !get + "SITE URL"\n'
              'Close = !bye\n'
              'Download Instagram Post = !instapost + "POST URL"\n'
              'Download Instagram Reel = !instareel + "REEL URL"\n'
              'Search Somethin on Google = !google + "TOPIC"\n'
              'Bring Information About Something = !info + "TOPIC"\n'
              'Start Cmd = !cmd')
