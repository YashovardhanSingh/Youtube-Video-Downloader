try:
	from pytube import YouTube, Playlist
	from tkinter import filedialog, Tk
	import os
except:
	print('Some Modules are missing...')
	quit()


def edit_link(link):
	if link[:5] == 'https':
		return link[8:]
	else:
		return link

def clear_screen():
	os.system('cls')

def check_q(query):
	if query.lower() == 'q':
		clear_screen()
		system()

def download_video():
	try:
		clear_screen()
		url = input('Link of the video (q to quit): ')
		check_q(url)
		url = edit_link(url)
		videos = YouTube(url)
		video_types = videos.streams.order_by('resolution')

		for index, value in enumerate(video_types):
				if value.resolution is not None:
						print(f'{index + 1} -> Resolution: {value.resolution}, FileType: {value.mime_type[6:]}')
		index = int(input('\nEnter index: '))

		window = Tk()
		print('\nWhere to Save the video: ')
		path = filedialog.asksaveasfilename(filetypes=(('Video files', ('*.mp4', '*.webm')), ('All files', '*.*')))
		window.destroy()

		video = video_types[index - 1]
		print("Video is Downloading...")
		video.download(path)
		print("Video Downloaded")
		play_video(path, video.mime_type[6:])
		system()
	except:
		clear_screen()
		print('Sorry, your Video cannot be Downloaded\n')
		system()

def download_multiple_videos():
	try:
		num = int(input("How many videos to download: "))
		for i in range(num):
			download_video()
		clear_screen()
		system()
	except:
		clear_screen()
		print("Sorry, It does not works right now.")
		system()

def play_video(path, vtype):
	try:
		q = input('Do you want to play the video (y or n): ').lower()
		if q == 'y':
			clear_screen()
			os.system(path + '\\' + 'YouTube.' + vtype)
		else:
			system()
	except:
		pass

def download_playlist():
	try:
		clear_screen()
		url = input('Link of the Playlist (q to quit): ')
		check_q(url)
		url = edit_link(url)
		pl = Playlist(url)

		window = Tk()
		print('\nWhere to Save the Playlist: ')
		path = filedialog.asksaveasfilename(filetypes=(('Video files', ('*.mp4', '*.webm')), ('All files', '*.*')))
		window.destroy()
	
		pl.download_all(path)
		system()
	except:
		clear_screen()
		print('Sorry, your Playlist cannot be Downloaded\n')
		system()

def system():
	print(" v - Download a Single Video \n m - Download Multiple videos \n p - Download entire Playlist \n q - quit")
	query = input('> ').lower()

	if query == 'v':
		download_video()
	elif query == 'p':
		download_playlist()
	elif query == 'q':
		clear_screen()
		quit()
	elif query == 'm':
		download_multiple_videos()
	else:
		system()

clear_screen()
system()
