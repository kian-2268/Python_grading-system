class Book:
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.isAvailable = True

    def is_Available(self):
        return self.isAvailable
    
    def borrow_book(self):
        if self.isAvailable:
            self.isAvailable = False
            print("Successfully borrowed a book!")
        else:
            print("Error! This book is already borrowed.")

    def return_book(self):
        if not self.isAvailable:
            self.isAvailable = True
            print("Book was successfully returned!")
        else:
            print("Error! Book is already available.")

    def display_info(self):
        status = "Available" if self.isAvailable else "Unavailable"

        print("\nBook Information")
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Publication Year: ", self.pub_year)
        print("Status: ", status)

def Main():
    try:
        title = input("Enter the title of the book: ")
        author = input("Enter the name of the author: ")

        while True:
            try:
                year = input("Enter the publication year: ")
                break
            except ValueError:
                print("Error: Please enter a valid(numbers only).")

        book = Book(title, author, year)

        while True:
            print("\nChoose an action: ")
            print("[1] Borrow book")
            print("[2] Return book")
            print("[3] Display book information")
            print("[4] Exit")

            Choice = input("Enter your choice(1-4): ")

            if Choice == "1":
                book.borrow_book()
            elif Choice == "2":
                book.return_book()
            elif Choice == "3":
                book.display_info()
            elif Choice == "4":
                print("Exiting program. Thank you for using us!")
                break
            else:
                print("Error. Invalid choice. Please only select from 1 to 4.")

    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    Main()
