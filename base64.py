#!/usr/bin/env python3
import sublime, sublime_plugin
import base64
import tempfile
import string
import random

class Base64DecodeCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		if self.has_selection():
			selection = ""
			for region in self.view.sel():
				# Concatenate selected regions together.
				selection += self.view.substr(region)

			# try to decode text
			try:
				bData = base64.b64decode(selection)

				text = bData.decode("utf-8")
				view = sublime.active_window().new_file()
		
				view.insert(edit, 0, text)
				view.set_name("base64")
				view.set_read_only(False)
				view.set_scratch(True)

			except UnicodeDecodeError:
				# cannot decode string, try to open in hex
				# self.load_temp_file(bData)
				pass


	def description(self): 
		return "Base64 decodes selected text into new buffer."

	def has_selection(self):
		has_selection = False

		# Only enable menu option if at least one region contains selected text.
		for region in self.view.sel():
			if not region.empty():
				has_selection = True

		return has_selection


