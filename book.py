class Publisher:
    def __init__(self,name):
        self.publisher = name
    def display(self):
        print(f"Publisher: {self.publisher}")
class Book(Publisher):
    def __init__(self, name,title,author):
        super().__init__(name)
        self.title = title
        self.author = author
    def display(self):
        print(f"{self.title}, written by {self.author}")
        super().display()
class Python(Book):
    def __init__(self, name, title, author,price,NOP):
        super().__init__(name, title, author)
        self.pages = NOP
        self.price = price
    def display(self):
        super().display()
        print(f"Price: {self.price}\nNo of pages: {self.pages}")
book = Python("CET","Python Programming","Student",299,200)
book.display()
