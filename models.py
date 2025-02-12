from typing import List

class ToDo:
    id_counter =1

    def __init__(self, title:str):
        self.id= ToDo.id_counter
        self.title= title
        self.is_completed = False
        ToDo.id_counter +=1

todos: List[ToDo]=[]
