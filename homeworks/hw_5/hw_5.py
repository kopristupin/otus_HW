import os
from pathlib import Path
from enum import Enum
from copy import deepcopy
import datetime

class BaseDriver(self):
    def __init__(self):

    def open(self):

    def create(self, path: str):

class FileLocalDriver(BaseDriver):
    def __init__(self):
        super().__init__(file_dir)

    def open(self, path: str):

    def create (self, path: str):

class FileRemoteDriver(BaseDriver):
    def __init__(self):
        super().__init__(file_dir)

    def open(self, path: str):

    def create(self, path: str):


class BaseFile:
    def __init__(self, file_path: str, driver_for_file ) -> None:
        self.file_driver = driver_for_file
        #self.file_byte - byte representaition of file
        try:
            self.file_byte = self.file_driver.open(file_path)
        except FileNotFoundError:
            try:
                self.file_byte = self.file_driver.create(file_path)
            except ErrorInCreation:
                raise ErrorInCreation

        self.file_path = file_path
        self.extension = file_path.suffix
        self.size = os.path.getsize(self.file_dir)
        self.temp_file = deepcopy(self.file_byte)
        self.time_creation = self.file_byte.parse_time_creation()

    def __str__(self):

    def __deepcopy__(self, memodict={}):

    def __copy__(self):

    def move(self, new_path):
        pass

    def remove(self):
        pass

    def rename(self, new_name: str):
        pass

    @property
    def time_creation(self):
        return self.time_creation

    def save(self):
        pass

    @property
    def extension(self):
        return self.extension.lower()

class PhotoFile(BaseFile):
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def show(self):

    def resize(self, width_new, height_new):

    def zoom(self, coefficient: float):

    def cut_rectangle(self, start_cut_x, start_cut_y, end_cut_x, end_cut_y) -> Image:

    def remove_rectangle(self, start_cut_x, start_cut_y, end_cut_x, end_cut_y)


class MediaFileWithAudio(BaseFile):
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def play(self):

    def stop(self):

    def edit(self, start_edit_milisec, end_edit_milisec):

    def cut(self, start_cut_milisec, end_cut_milisec):

    def insert(self, milisec_to_insert, audio_to_insert: MediaFileWithAudio):

class AudioFile(MediaFileWithAudio):
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def play(self):
        """Play audio file by some api"""

    def stop(self):

    def edit(self, start_edit_milisec, end_edit_milisec):

    def cut(self, start_cat_milisec, end_cut_milisec):

    def insert(self, milisec_to_insert, audio_to_insert: AudioFile):

class VideoFile(MediaFileWithAudio):
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def play(self):
        """Play audio file by some api"""

    def stop(self):

    def edit(self, start_edit_milisec, end_edit_milisec):

    def cut(self, start_cat_milisec, end_cut_milisec):

    def insert(self, milisec_to_insert, audio_to_insert: AudioFile):


