#list = [1, 2, 3, 4, 5]

# for i in list:
   # print(i)
    
#x = list[0]
#print(x)
#a=0

#while a < len(list):
  #  print(list[0])
   # a = a + 1
    
#dict1 = {"a":1, "b":2, "c":3}
#for key, value in dict1.items():
    #print(key,value)
    
# a + b

#def add(a, b):
   # return a + b

#sum =  add(2, 3)
#print(sum) 

class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:
    
    def __init__(self):   
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        return [book.title for book in self.books]
    
if __name__ == "__main__":
    library = Library()
    
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To kill a Mockingbird", "Harper Lee"))     
    
    print("Books in the library:")
    for book in library.list_books():
        print(book)
        
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    print(book.title)
    print(book.author)