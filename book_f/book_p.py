class Book:
    total_books = 0
    def __init__(self,name,author,available):
        if available <0:
            raise ValueError("copies must be at least 1")
        self.name=name
        self.available =available 
        self.total_books += 1
        self.author=author

    def borrow(self):
        if self.available >0 :
            self.available -= 1
        else:
            raise ValueError ("no copies available")
        

    def return_book(self,return_book):
        if return_book == self.available:
            raise ValueError("all copies are already in")
        return return_book 

    def is_available(self):
        if self.available <= 1:
            return True
    def __str__(self):
        return f"neme is book {self.name} + The number of copies is {self.available}"




