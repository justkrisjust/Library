"""library management system
4 functions 1: display all books
            2: lend a book (from lib to person)
            3: add a book(to lib)
            4: return book
take a dict where the key will be book and value will be name of the person who took the book
we try to take while loop in main function """

class Library:
    def __init__(self, books, book, name, ):
        self.books = books
        self.book = book
        self.name = name



    def Display(self):
        return f"the available books are \n {[self.books]} "



    def Lend(self):

        f=open("bookstaken.txt" , "a")
        n=int(input("enter the book number you want to take correctly \n"))
        print(f" \n {self.name} took the book {self.book[n]} from Library \n")
        matter =input("please enter the book name you took and your name with  : \n")

        f.write(matter +"\n")
        f.close()
        #print(f" \n {self.name} took the book {self.book[n]} from Library \n")


    def add(self):
        f =open("booksadded.txt" ,"a")
        adding=input("enter the book name you want to add into Library  : ")

        self.books.append(adding)
        f.write(adding + f" : {self.name}")
        f.close()
        print( f" A new book is successfully  added into Library by  {self.name} .")


    def returning(self):
        t=int(input("enter the book number to return the book (enter the number correctly)  : "))

        print(f"the person {self.name} is returning the book {self.book[t]} \n")
        verify_the_book = input("please verify the name of the book :")
        if verify_the_book == self.book[t]:
            print("verification successful ")
        else:print("verification unsuccessful please try again !")


books = [" ", "onepeice", "naruto",  "harry potter", "the Me ", "the Goal of a GoalKeeper", "Crazy fingers",
         "Love Death Robots", "Game Of Thrones ", "House Of Dragons", "riverdale", "The Vampire Diaries",
         "deadly flash", "Dead by Dawn", " HELL",
         "Hungry ghost", "the Keeper", "The looter", "Drugs and Herbs", "Lessons of Failure", "The work of Eagle", "The Trip"]


book = books
name = input("enter your name ")
kris = Library(books, book, name)

while True:
  choice = int(input("enter the choice 1:display books 2:lend a book 3:add a book 4:return a book \n"))

  if choice == 1:

   print(kris.Display())

  elif choice == 2:
      print(kris.Lend())

  elif choice ==3:
     print(kris.add())

  elif choice ==4:
      print(kris.returning())

  else:break






