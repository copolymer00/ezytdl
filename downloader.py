import yt_dlp


def download_song(url):
	ydl_opts = {
	    'format': 'bestaudio',
	    'noplaylist': True,
	    'postprocessors': [{
		   'key': 'FFmpegExtractAudio',
		   'preferredcodec': 'opus',
		   'preferredquality': '192',
	    }],
	    'outtmpl': '~/music/%(title)s.%(ext)s',
	}
	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		return 0
	except:
		return 1

