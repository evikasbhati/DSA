class Book:
    def __init__(self,title,author,isbn):
        self.title=title;
        self.author=author;
        self.isbn=isbn;
        self.status=True;

class Keeper:
    def __init__(self):
        self.collection=[];

    def addBook(self,book):
        self.collection.append(book);

    def removeBook(self,title):
        for i in self.collection:
            print(i.title,"s",title)
            if i.title==title :
                value=i;
                break;
        if value:
            self.collection.remove(value);
        else:
            print("book doesn't exist")

    def findBook(self,value):
        dump=None;
        for i in self.collection:
            if i.title or i.author or i.isbn == value :
                dump=i;
                break;
        if dump :
            print(f"Title: {dump.title}, Author: {dump.author}, ISBN: {dump.isbn}");
        else:
            print("book doesn't exist");

    def showAll(self):
        for i in self.collection:
            print(f"Title: {i.title}, Author: {i.author}, ISBN: {i.isbn}\n");


coll=Keeper()

def main(choice):
    
    if choice==1:
        bookTitle=input("Enter title \n");
        bookAuthor=input("Enter author \n");
        bookIsbn=input("Enter isbn \n");
        coll.addBook(Book(bookTitle,bookAuthor,bookIsbn))

    if choice==2:
        bookRInput=input("Enter title to delete book: \n ")
        coll.removeBook(bookRInput);

    if choice==3:
        bookSInput=input("Enter title or author name to search: \n")
        coll.findBook(bookSInput)

    if choice==5:
        coll.showAll()

while True:

    print("1: Add book");
    print("2: Remove book");
    print("3: Search book");
    print("4: Exit");
    choice=int(input("Enter your choice: "))
    if choice==4 :
        break;
    else: main(choice);
