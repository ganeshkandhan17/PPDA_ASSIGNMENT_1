import os
from datetime import datetime
BOOKS_FILE = 'books.txt'
USERS_FILE = 'users.txt'
TRANSACTIONS_FILE = 'transactions.txt'

def load_file(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return file.readlines()

def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.writelines(data)

def add_book(title, author):
    books = load_file(BOOKS_FILE)
    books.append(f"{title},{author},available\n")
    save_to_file(BOOKS_FILE, books)
    print(f"Book '{title}' by {author} added successfully.")

def view_books():
    books = load_file(BOOKS_FILE)
    if not books:
        print("No books available.")
        return
    for book in books:
        title, author, status = book.strip().split(',')
        print(f"Title: {title}, Author: {author}, Status: {status}")

def add_user(name):
    users = load_file(USERS_FILE)
    users.append(f"{name}\n")
    save_to_file(USERS_FILE, users)
    print(f"User '{name}' registered successfully.")

def view_users():
    users = load_file(USERS_FILE)
    if not users:
        print("No users registered.")
        return
    for user in users:
        print(f"User: {user.strip()}")

def borrow_book(user_name, book_title):
        books = load_file(BOOKS_FILE)
    transactions = load_file(TRANSACTIONS_FILE)
    
    for i, book in enumerate(books):
        title, author, status = book.strip().split(',')
        if title == book_title and status == 'available':
            books[i] = f"{title},{author},borrowed\n"
            save_to_file(BOOKS_FILE, books)
            transactions.append(f"{user_name} borrowed '{book_title}' on {datetime.now()}\n")
            save_to_file(TRANSACTIONS_FILE, transactions)
            print(f"Book '{book_title}' borrowed by {user_name}.")
            return
    
    print(f"Book '{book_title}' is not available or not found.")

def return_book(user_name, book_title):
    """ Allow a user to return a borrowed book. """
    books = load_file(BOOKS_FILE)
    transactions = load_file(TRANSACTIONS_FILE)
    
    for i, book in enumerate(books):
        title, author, status = book.strip().split(',')
        if title == book_title and status == 'borrowed':
            books[i] = f"{title},{author},available\n"
            save_to_file(BOOKS_FILE, books)
            transactions.append(f"{user_name} returned '{book_title}' on {datetime.now()}\n")
            save_to_file(TRANSACTIONS_FILE, transactions)
            print(f"Book '{book_title}' returned by {user_name}.")
            return
    
    print(f"Book '{book_title}' was not borrowed or not found.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Register User")
        print("4. View Users")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == '2':
            view_books()
        elif choice == '3':
            name = input("Enter user name: ")
            add_user(name)
        elif choice == '4':
            view_users()
        elif choice == '5':
            user_name = input("Enter user name: ")
            book_title = input("Enter book title: ")
            borrow_book(user_name, book_title)
        elif choice == '6':
            user_name = input("Enter user name: ")
            book_title = input("Enter book title: ")
            return_book(user_name, book_title)
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
