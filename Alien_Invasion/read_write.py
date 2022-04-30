from ctypes import c_char
from ctypes.wintypes import CHAR
import json
from my_settings import MySettings
import os


class read_write_game():
    """Class for managing the read and writing instruction for the game"""
    
    def __init__(self, my_settings : MySettings) -> None:
        
        self.my_settings = my_settings
        self.path = os.path.join(self.my_settings.subfolder_name \
            ,self.my_settings.subfolder_name,self.my_settings.file_name_json)


    def read_json(self, atribute : str = 'r') -> dict :
        """function for reading from the file"""
        return self.__write_read(atribute)

    def write_json(self, game_stats : dict, atribute : str = 'w') -> None :
        """function for writing to the file"""
        self.__write_read(atribute,game_stats)

    def __write_read(self, atribute : str, game_stats : dict =  {}) -> dict :
        """Function for reading and writing files"""
        """in read mode it returns a dict of the data read """
        """in write mode it returns a dict of data wrote"""
        json_data = game_stats 
        if atribute == 'r' or atribute == 'w':
            try: 
                with open(self.path,atribute) as file:
                    if atribute == 'r':
                        json_data = json.load(file)
                    elif atribute == 'w':
                        json.dump(json_data,file)
            except FileNotFoundError:
                pass
            
        return json_data