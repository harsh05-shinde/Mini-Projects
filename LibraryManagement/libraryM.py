class library:
    def __init__(self):
        self.book_list = []
        self.borrowed_books = {}
        self.user_names = []
        
    def display_books(self):
        print(f"These books currently we have in our library {self.book_list}")
        print(f"These books are borrowed Not returned Yet {self.borrowed_books}")
    
    def add_book(self,*args):
            for book in args:  
              self.book_list.append(book)
            

    def borrow_book(self):
           user_name = input("please enter your name:")
           self.user_names.append(user_name)        

           book_name = str(input("please enter the book which you want:"))
           if book_name in self.book_list:
             self.book_list.remove(book_name)
             self.borrowed_books[user_name]  = book_name
             return "Yes book found, You can take the book"
           else:
             return "Sorry this currently is not available"
          
    def return_book(self):
         user_name = input("please enter Your name:")
         if user_name in self.borrowed_books:
            #self.user_names.append(name)
            book_name = input("please Enter book name:")

            if self.borrowed_books[user_name] == book_name:
                self.book_list.append(book_name)
                self.borrowed_books.pop(user_name)
            else:
                return "Sorry,the book name was not found in our Record Please Try again"
         else:
             return "Sorry,your name was Not found in our records Please try again"
    def history(self):
        print(f"Borrowed books History {self.borrowed_books}")
        print(f"user Entry History {self.user_names}")
        

l = library()
l.add_book("zero to one","Elon musk","hard things about hard things","white nights")
running=True
while running:
    print("1.display books")
    print("2.borrow books")
    print("3.return book")
    print("4.history")
    print("5.Exit")
    try:
      choice = int(input("Please Enter Your choice:"))
      if choice==1:
         l.display_books()
      elif choice==2:
         print(l.borrow_book())
      elif choice==3:
         l.return_book()
      elif choice==4:
         l.history()
      elif choice==5:
          print("Thank you to visit")
          running = False
      else:
         print("please enter the correct choice")
    except ValueError:
        print("Please enter the integer Value")
    
    
    







