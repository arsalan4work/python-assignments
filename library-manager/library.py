import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials"""
    
    def __init__(self):
        """Initialize an empty book collection and load saved data from file."""
        self.book_list = []  # List to store books
        self.storage_file = "books_data.json"  # File for storing book data
        self.read_from_file()


    def read_from_file(self):
        """Load books from a JSON file if available, otherwise start fresh."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file is missing or has invalid data, start with an empty list
            self.book_list = []


    def save_to_file(self):
        """Save the current book collection to a JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)  # Save with indentation for readability


    def create_new_book(self):
        """Add a new book to the collection with user input."""
        book_title = input("📖 Enter book title: ")
        book_author = input("✍️ Enter author: ")
        publication_year = input("📅 Enter publication year: ")
        book_genre = input("🎭 Enter genre: ")
        is_book_read = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read
        }

        self.book_list.append(new_book)  # Add book to the list
        self.save_to_file()  # Save updated list to file
        print("🎉 Book added successfully!\n")


    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("❌ Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():  # Case-insensitive comparison
                self.book_list.remove(book)  # Remove the matched book
                self.save_to_file()
                print("✅ Book removed successfully!\n")
                return
        
        print("⚠️ Book not found!\n")  # Message if book is not found


    def find_book(self):
        """Search for books by title or author."""
        search_text = input("🔍 Enter search term: ").lower()  # Convert input to lowercase for comparison
        
        # Find books that match the search term in title or author (case insensitive)
        found_books = [
            book for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]

        if found_books:
            print("📚 Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "✅ Read" if book["read"] else "📖 Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        else:
            print("❌ No matching books found.\n")


    def update_book(self):
        """Update details of an existing book by searching with the title."""
        book_title = input("✏️ Enter the title of the book you want to edit: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():  # Case-insensitive title match
                print("🔄 Leave blank to keep existing value.")

                # Allow users to update fields while keeping old values if left blank
                book["title"] = input(f"📖 New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"✍️ New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"📅 New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"🎭 New genre ({book['genre']}): ") or book["genre"]
                book["read"] = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"

                self.save_to_file()  # Save updated details
                print("✅ Book updated successfully!\n")
                return
        
        print("⚠️ Book not found!\n")


    def show_all_books(self):
        """Display all books in the collection with details."""
        if not self.book_list:
            print("📭 Your collection is empty.\n")  # Message if no books are stored
            return

        print("📚 Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "✅ Read" if book["read"] else "📖 Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}\n")


    def show_reading_progress(self):
        """Calculate and display reading progress statistics."""
        total_books = len(self.book_list)  # Total books in collection
        completed_books = sum(1 for book in self.book_list if book["read"])  # Count of books marked as read

        # Prevent division by zero if no books exist
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0

        print(f"📚 Total books in collection: {total_books}")
        print(f"📊 Reading progress: {completion_rate:.2f}%\n")


    def start_application(self):
        """Run the Library Manager application with a menu-driven interface."""
        while True:
            print("\n📚 Welcome to Library Manager 📚")
            print("1️⃣  Add a new book")
            print("2️⃣  Remove a book")
            print("3️⃣  Search for books")
            print("4️⃣  Update book details")
            print("5️⃣  View all books")
            print("6️⃣  View reading progress")
            print("7️⃣  Exit")

            user_choice = input("➡️  Please choose an option (1-7): ")

            # Process user choice and call the corresponding function
            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()  # Ensure data is saved before exit
                print("🙏 Thank you for using Library Manager! 📚 Goodbye! 👋")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")  # Handle invalid input

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
