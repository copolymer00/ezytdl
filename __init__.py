import gi
import downloader
print(downloader.download_song)


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Window(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="")
		
		self.set_border_width(10)
		self.set_default_size(500,400)

		self.grid = Gtk.Grid()
		self.add(self.grid)

		self.label = Gtk.Label(label = "Youtube Downloader")

		self.grid.add(self.label)

		self.urlbox = Gtk.Box(spacing=10)
		self.urllabel = Gtk.Label(label="Paste Link Here")
		self.urlentry = Gtk.Entry()
		self.submit = Gtk.Button(label="Download")
		self.submit.connect("clicked", self.text_submit)
		self.urlbox.pack_start(self.urllabel, True, True, 0)
		self.urlbox.pack_start(self.urlentry, True, True, 0)
		self.urlbox.pack_start(self.submit, True, True, 0)
		#                  widget,  col, row, width, height
		self.grid.attach(self.urlbox, 0, 2, 1, 1)


	def button_clicked(self, widget):
		print(widget.get_properties("label")[0])
	def text_submit(self, widget):
		link = self.urlentry.get_text()
		if link.find("youtube.com") == -1:
			# print("Must be youtube link")
			self.show_error_popup("Must be a youtube link")
		else:
			result = downloader.download_song(link)
			if result == 1:
				self.show_error_popup("Video unavailable")
			elif result == 0:
				self.show_info_popup("Download complete")
	def show_error_popup(self, message: str):
		dialog = Gtk.MessageDialog(
			transient_for=self,
			flags=0,
			message_type=Gtk.MessageType.ERROR,
			buttons=Gtk.ButtonsType.OK,
			text="Error",
		)
		dialog.format_secondary_text(message)
		dialog.run()
		dialog.destroy()

	def show_info_popup(self, message: str):
		dialog = Gtk.MessageDialog(
			transient_for=self,
			flags=0,
			message_type=Gtk.MessageType.INFO,
			buttons=Gtk.ButtonsType.OK,
			text="Info",
		)
		dialog.format_secondary_text(message)
		dialog.run()
		dialog.destroy()

window = Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
