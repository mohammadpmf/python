from tkinter import *
from tkinter import filedialog
import pygame
DEFAULT_VOLUME = 30

class MyMusicPlayer():
    def __init__(self, root, btn_colors='light blue', voice_color='dark cyan', volume_color = 'cyan', active_color='orange'):
        self.player = pygame.mixer
        self.player.init()
        self.root = root
        self.frame_up = Frame(self.root)
        self.frame_down = Frame(self.root)
        Button(self.frame_up, bg=btn_colors, activebackground=active_color, text='load file', command=self.load_file).pack(side='left', expand=1, fill='x')
        Button(self.frame_up, bg=btn_colors, activebackground=active_color, text='start', command=self.start).pack(side='left', expand=1, fill='x')
        Button(self.frame_up, bg=btn_colors, activebackground=active_color, text='pause', command=self.pause).pack(side='left', expand=1, fill='x')
        Button(self.frame_up, bg=btn_colors, activebackground=active_color, text='resume', command=self.resume).pack(side='left', expand=1, fill='x')
        Button(self.frame_up, bg=btn_colors, activebackground=active_color, text='stop', command=self.stop).pack(side='left', expand=1, fill='x')
        Button(self.frame_up, bg=btn_colors, activebackground=active_color, text='exit', command=self.root.destroy).pack(side='left', expand=1, fill='x')
        self.volume = Scale(self.frame_down, orient=HORIZONTAL, from_=0, to=100, command=self.change_volume, bg=voice_color, fg=volume_color, activebackground=active_color)
        self.volume.set(DEFAULT_VOLUME)
        self.volume.pack(expand=1, fill='x')
    def pack(self, *args, **kwargs):
        self.frame_up.pack(expand=1, fill='x')
        self.frame_down.pack(expand=1, fill='x')
    def load_file(self):
        self.res = filedialog.askopenfilename()
        self.player.music.load(self.res)
        self.player.music.set_volume(DEFAULT_VOLUME/100)

    def start(self):
        self.player.music.play()
    def pause(self):
        self.player.music.pause()
    def resume(self):
        self.player.music.unpause()
    def stop(self):
        self.player.music.stop()
    def change_volume(self, n):
        self.player.music.set_volume(int(n)/100)

if __name__ == '__main__':
    root = Tk()
    my_player = MyMusicPlayer(root)
    my_player.pack()
    mainloop()