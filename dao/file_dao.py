from abc import ABC


class BaseFileDaoABC(ABC): 
    file_path = None
    def __init__(self , file_path: str) -> None:
        super().__init__()
        self.file_path = file_path

    def read_file(self):
        file = open(self.file_path)
        file_contents = file.read()
        file.close()
        return file_contents
    
    def write_file(self, str_json:str): 
        file = open(self.file_path, mode= "w")
        file.write(str_json)
        file.close
    
