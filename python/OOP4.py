class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        
        return f'The title is {self.title}, and the author is {self.author}'

    def __len__(self):
        return self.pages

mybook = Book('Python','Jose',250)

print(mybook)
print(len(mybook))