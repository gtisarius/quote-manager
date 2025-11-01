import csv
import time
from classes.tools import Tools
from classes.newquote import newQuote

fieldnames = ["quote", "speaker", "date", "tags"] 

class Quotes:
    def initialize(quotesheet, arr, mainFunc):
        Tools.clearScreen()
        """
        Function to import quotes or create a new comma-separated values (CSV) file.
        """
        Tools.header("Quote Database v.1.0")
        try: # If the specified filepath from quotesheet exists:
            with open(quotesheet, "r") as f:
                print(f"Importing quotes from {quotesheet}")
                for quote in csv.DictReader(f): # Convert every line in the CSV to a dictionary
                    arr.append(quote)
                    print(f"Quote {quote} appended!")
        except FileNotFoundError: # Create new csv file if the specified filepath doesn't exist.
            print(f"Creating {quotesheet}")
            with open(quotesheet, "w", newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader() # Write the fieldnames in every created CSV file.
        except:
            Tools.error("An error occurred with the initialization!")
        Tools.success("Done!")
        time.sleep(1)
        return mainFunc
    
    def view(arr):
        Tools.clearScreen()
        if len(arr) > 0:
            Tools.view(arr)
        else:
            print("There are no quotes in the library.")
        input(Tools.prompt("Press enter to continue to menu..."))

    def addQuotes(arr, quotesheet):
        Tools.clearScreen()
        quoteTags = [] # Used to categorize quotes.
        quoteInput = input(Tools.prompt("Write the quote (CASE SENSITIVE):> "))
        speakerInput = input(Tools.prompt("Speaker? (CASE SENSITIVE):> "))
        dateInput = Tools.inputDate()
        Tools.inputTags(quoteTags) 
        addedQuote = newQuote(quoteInput, speakerInput, dateInput, quoteTags).toDict() # Creates a newQuote object and converts it into a dict
        arr.append(addedQuote) # Add to rawQuotes to be sorted later in menu()
        try: # Write the newQuote dict to the CSV file
            with open(quotesheet, "a", newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(addedQuote)
            Tools.success("Quote added successfully!")
        except Exception as e:
            Tools.error(f"An error occurred!: {e}")
        time.sleep(1)