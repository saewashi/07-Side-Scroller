#!/usr/bin/python
import pygame,os

class Sound:
	def __init__(self):
		self.SONG_END = pygame.USEREVENT + 1
		pygame.mixer.music.set_endevent(self.SONG_END)
		self.soundtrack = []
		self.current_track = -1
		self.sound_library = {}
	
	def add_music(self,track):
		'''
    sound.add_music('Ambient_Blues_Joe_ID_773.mp3')


		Adds a music to the soundtrack list. Assumes the music is in the mp3 folder
		'''
		self.soundtrack.append(track)
	
	def add_sound(self,label,sound):
		'''
		sound.play_music()
		Adds a sound to the sound_library dictionary. Assumes the sound is in the mp3 folder
		Pygame (version 2.9 at least) doesn't support 32-bit float WAVs. If you have trouble with a WAV file, you will need to choose another one or recode it
		'''
		self.sound_library[label] = pygame.mixer.Sound(os.path.join('mp3', sound))
	
	def play_music(self):
		if len(self.soundtrack):
			self.current_track += 1 % len(self.soundtrack)
			pygame.mixer.music.load(os.path.join('mp3', self.soundtrack[self.current_track]))
			pygame.mixer.music.play()
	
	def play_sound(self,label):
		print(self.sound_library)
		if label in self.sound_library:
			self.sound_library[label].play()

	def event(self):
		return self.SONG_END