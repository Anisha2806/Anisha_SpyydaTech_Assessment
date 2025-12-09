**calculator.py**
    This program continually loops through a menu of options. When an option is selected, you enter two numbers which the program then computes and displays the result, storing details of the calculation into a history list. When choosing to view history, you will be able to see the details of all previous calculations. Exiting the program stops the loop from running.

**library.py**
    The Library program has a dictionary called library that maps all of the titles of the books to the author and the availability of that book. The menu will continue to run until you add new books, search for them, borrow them, or return them. If you add a book, it enters into the dictionary, If you search for a book, it searches to see if it exists and whether or not it is available, When you borrow a book, it gets marked as unavailable for the time period you are borrowing it, When you return a book, it gets marked available again, If you select to quit, the program loop will end.

**link shortner.py**

  Creating a Shortener object with s = pyshorteners.Shortener() allows the user to interact with different URL shortening websites.
When using the Shortener object, the user selects the URL shortening website by using an attribute of the Shortener object to access the method for shortening a given URL.
The code s.isgd tells the library that you are using the is.gd service, while short(long_url) sends the long URL to is.gd and receives back a shortened URL.
If there are no errors, the output will include a shortened URL that is easy to read and remember.
If you do encounter an error, it will be caught by the try/except block and instead of throwing an exception, it will return an error message.

**validating brackets.py**
  This program validates if a series of parentheses are balanced. The way this program works is by scanning each character in the input and utilizing a stack data structure to store any open parentheses that were added to the stack. When an open parenthesis is encountered, it is pushed onto the top of the stack. If a closing parenthesis  is encountered, the program verifies that it corresponds to the open parenthesis located at the top of the stack. If both parentheses agree, then the top open parenthesis will be popped from the stack. If there is no corresponding open parenthesis at the top of the stacks, then false is printed. After processing all the parentheses, if the stack is empty, then the parentheses being evaluated are indeed balanced, otherwise not.

**word frequency.py**
  The program makes use of the NLTK libraries for text analysis. In order to use the tokenizer to split into sentences and words, the punkt_tab dataset must be downloaded. When you enter your text into the application, it will first use the word_tokenize() function to break down the input into single words. FreqDist will then count how many times each word appears and print out all the word frequencies in a loop.
