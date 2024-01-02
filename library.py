def start():
    # Store the books
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]

    # Initiate a list for borrowed books
    borrowedISBNs = []

    # Start function for the menu
    def printMenu():
        print('\n######################')
        print('1: (A)dd a new book.')
        print('2: Bo(r)row books.')
        print('3: Re(t)urn a book.')
        print('4: (L)ist all books.')
        print('5: E(x)it.')
        print('######################\n')

    # Create a function to add a book
    def addBook(choice):
        print("Your selection> " + choice) # show what choice you picked

        # Make a while loop so the program keeps asking for a book name with no % or *
        while True:
            bookname = input("Book name> ")
            if "*" in bookname or "%" in bookname:
                print("Invalid book name!")
            else:
                break

        # Ask for the author's name
        authorname = input("Author name> ")

        # Create a while loop so the program keeps asking for an edition value with just whole numbers
        while True:
            edition = input("Edition> ")
            if not edition.isdigit():
                print("Invalid number!")
            else:
                break

        # Make a while loop to check the entered ISBN for multiple things, first of them to see if it is 13 digits exactly
        while True:
            isbn = input("ISBN> ")
            if isbn.isdigit() and len(isbn) == 13: # if it is 13 numbered digits do a test
                # create the weight factors
                weight_factors = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
                # now take the sum of the digits after they have been multiplies by the weight factors
                weighted_sum = sum(int(digit) * weight for digit, weight in zip(isbn, weight_factors))

                # check if they are a multiple of 10
                if weighted_sum % 10 == 0:
                    # if they are check if they already exit
                    isbn_exists = any(book[0] == isbn for book in allBooks)
                    if isbn_exists: # if it does skip it
                        print("This book already exists in the library. Skipping the entry.")
                    else: # if not add it
                        allBooks.append([isbn, bookname, authorname, edition, []])
                        print("New book is successfully added.")
                    break
                else:
                    break
            else:
                print("Invalid number!")

    # create function for borrowing book and ask the user for some input
    def borrowBook():
        borrowerName = input("Enter the borrower name> ")
        searchTerm = input("Search Term> ")

        # Start searching for books using a for loop
        booksFound = []  # Create a variable for books that are found
        for book in allBooks:
            book_name = book[1] # search for the term
            searchTerm

            # Check the user input for * and % and then, based on that, look at the letters, if they find the book, add it to booksFound
            if searchTerm.endswith('*') and book_name.find(searchTerm[:-1]) != -1:
                booksFound.append(book)
            elif searchTerm.endswith('%') and book_name.startswith(searchTerm[:-1]):
                booksFound.append(book)
            elif book_name == searchTerm:
                booksFound.append(book)

        # If the variable is empty, no books were found
        if not booksFound:
            print("No books were found with the search term.")
        else:
            for book in booksFound: # if book was found
                # add the name of the borrower to the list
                book[4].append(borrowerName)
                # Store book details in borrowedISBNs in the expected format
                borrowedISBNs.append([book[0], book[1], book[2], book[3],book[4] ,[borrowerName]]) # add the borrower's name
                print(f"-{book[1]} is borrowed!")

                # remove the book from the book list
                allBooks.remove(book)

    # create a function for returning a book
    def returnBook():
        while True: # start a while loop to check if isbn matches with a book
            isbnR = input("ISBN> ")

            for borrowedBook in borrowedISBNs:
                if isbnR == borrowedBook[0]:  # check if ISBN matches with a book in borrowed books
                    # add the book back to allBooks along with the borrower's name
                    allBooks.append(
                        [borrowedBook[0], borrowedBook[1], borrowedBook[2], borrowedBook[3], borrowedBook[4]])
                    borrowedISBNs.remove(borrowedBook)  # Remove it from borrowedISBNs
                    print(f"{borrowedBook[1]} has been returned")
                    return

            print("No book is found!") # if no book is found

   # create a function for displaying the list of books
    def displayBookList():
        for book in allBooks: # start a for loop in the allbooks list and print the info
            print("---------------")
            print("[Available]")
            print(f"{book[1]} - {book[2]}")
            print(f"E: {book[3]}, ISBN: {book[0]}")
            # if there is name for the borrower display it if not do nothing
            if book[4]:
                print(f"borrowed by: [{', '.join(book[4])}]")

        # display the books in borrowed books section with a for loop
        for borrowedBook in borrowedISBNs:
            print("---------------")
            print("[Unavailable]")
            print(f"{borrowedBook[1]} - {borrowedBook[2]}")
            print(f"E: {borrowedBook[3]}, ISBN: {borrowedBook[0]}")
            print(f"borrowed by: [{', '.join(borrowedBook[4])}]")

    # create a function for exiting the loop and displaying
    def exit():
        print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
        for book in allBooks:  # start a for loop in the allbooks list and print the info
            print("---------------")
            print("[Available]")
            print(f"{book[1]} - {book[2]}")
            print(f"E: {book[3]}, ISBN: {book[0]}")
            # if there is name for the borrower display it if not do nothing
            if book[4]:
                print(f"borrowed by: [{', '.join(book[4])}]")

        # display the books in borrowed books section with a for loop
        for borrowedBook in borrowedISBNs:
            print("---------------")
            print("[Unavailable]")
            print(f"{borrowedBook[1]} - {borrowedBook[2]}")
            print(f"E: {borrowedBook[3]}, ISBN: {borrowedBook[0]}")
            print(f"borrowed by: [{', '.join(borrowedBook[4])}]")

# start a loop so eveytime the user is done with a function the printMenu list appears again
    while True:
        # make a variable that asks for a choice
        printMenu()
        choice = input("Enter your choice: ")

        # based on what the user picks open the fucntion for it
        if choice in ('1', 'a', 'A'):
            addBook(choice)
        elif choice in ('2', 'r', 'R'):
            borrowBook()
        elif choice in ('3', 't', 'T'):
            returnBook()
        elif choice in ('4', 'l', 'L'):
            displayBookList()
        elif choice in ('5', 'x', 'X'):
            exit()
            break # break loop when they select exit
        else:
            print("Wrong selection! Please select a valid option.")

start()
