import os
from pathlib import Path
from enum import Enum
from copy import deepcopy
import datetime

class BaseDriver(self):
    """Base driver class
        Driver is used to interact with various sources of files
    """
    def __init__(self):

    def open(self):
        """
        Open file with driver.
        """

    def create(self, path: str):
        """
        Create file with driver
        """

class FileLocalDriver(BaseDriver):
    def __init__(self):
        """
        Driver to interact with local files
        """
        super().__init__(file_dir)

    def open(self, path: str):
        """Try to open file in url"""

    def create (self, path: str):
        """Try to create file in remote server"""

class FileRemoteDriver(BaseDriver):
    """
    Driver to interact with remote files
    """
    def __init__(self):
        super().__init__(file_dir)

    def open(self, url: str):
        """Try open local file"""

    def create(self, url: str):
        """Try to create local file"""


class BaseFile:
    """Base class for media file"""
    def __init__(self, file_path: str, driver_for_file ) -> None:
        self.file_driver = driver_for_file
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
        """Short definition of file"""

    def __deepcopy__(self, memodict={}):
        """Make deep copy of file"""

    def __copy__(self):

    def move(self, new_path):
        """Move file to new path.
        Uses driver"""
        pass

    def remove(self):
        """Remove file.
        Uses driver"""
        pass

    def rename(self, new_name: str):
        """Rename file.
        Uses driver"""
        pass

    @property
    def time_creation(self):
        return self.time_creation

    def save(self):
        """Try to save temp copy with changes.
        If ok - remove old copy
        """
        pass

    @property
    def extension(self):
        return self.extension.lower()

class PhotoFile(BaseFile):
    """Class for photo mefia files"""
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def show(self):
        """Show photo file in window"""

    def resize(self, width_new, height_new):
        """Try to resize photo to new width and height.
        Saves to temp copy"""

    def zoom(self, coefficient: float, x: float, y: float):
        """try to zoom photo to x,y with coefficient"""

    def cut_rectangle(self, start_cut_x, start_cut_y, end_cut_x, end_cut_y):
        """Try to cut photo by corresponding coordinates.
        Saves to temp copy"""

    def remove_rectangle(self, start_cut_x, start_cut_y, end_cut_x, end_cut_y)
        """Try to remove photo.
        Saves to temp copy"""


class MediaFileWithAudio(BaseFile):
    """Base class for media file with audio"""
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def play(self):
        """Play file"""

    def stop(self):
        """Stop playing"""

    def edit(self, start_edit_milisec, end_edit_milisec):
        """Open window for editting"""

    def cut(self, start_cut_milisec, end_cut_milisec):
        """Try to cut file by corresponding time points"""

    def insert(self, milisec_to_insert, audio_to_insert: MediaFileWithAudio):
        """Try to insert to corresponding time point"""

class AudioFile(MediaFileWithAudio):
    """Class for audio files"""
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def play(self):
        """Play audio file"""

    def stop(self):
        """Stop playing"""

    def edit(self, start_edit_milisec, end_edit_milisec):
        """Open window for editting of audio file"""

    def cut(self, start_cat_milisec, end_cut_milisec):
        """Try to cut audio file by corresponding time points"""

    def insert(self, milisec_to_insert, audio_to_insert: AudioFile):
        """Try to insert to corresponding time audio_to_insert"""

class VideoFile(MediaFileWithAudio):
    """Class for video files"""
    def __init__(self, file_dir):
        super().__init__(file_dir)

    def play(self):
        """Play video file by some api"""

    def stop(self):
        """Stop playing video file"""

    def edit(self, start_edit_milisec, end_edit_milisec):
        """Open window for video editting"""

    def cut(self, start_cat_milisec, end_cut_milisec):
        """Try to cut video file by corresponding time points"""

    def insert(self, milisec_to_insert, video_to_insert: VideoFile):
        """Try to insert video_to_insert to corresponding time point"""


