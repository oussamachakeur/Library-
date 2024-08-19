
class Book :

    def __init__(self , name , code , author):
        self.name = name
        self.code = code
        self.author= author
        self.borrowed = False


    def __str__(self):
        return f"Book name: {self.name} , from the author: {self.author} , code : {self.code}"
    