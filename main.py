import csv
import time
from classes.newquote import newQuote
from classes.tools import Tools
from classes.quotes import Quotes

rawQuotes = [] # Quotes as they appear from the csv file
quotes = []
quoteLists = []
quotesheet = "quotesheets/demonstration2.csv" # Source CSV file
logfile = "logs/searchdump.txt"

# def initialize():
#     Tools.clearScreen()
#     """
#     Function to import quotes or create a new comma-separated values (CSV) file.
#     """
#     Tools.header("Quote Database v.1.0")
#     try: # If the specified filepath from quotesheet exists:
#         with open(quotesheet, "r") as f:
#             print(f"Importing quotes from {quotesheet}")
#             for quote in csv.DictReader(f): # Convert every line in the CSV to a dictionary
#                 rawQuotes.append(quote)
#     except FileNotFoundError: # Create new csv file if the specified filepath doesn't exist.
#         print(f"Creating {quotesheet}")
#         with open(quotesheet, "w", newline='') as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader() # Write the fieldnames in every created CSV file.
#     except:
#         Tools.error("An error occurred with the initialization!")
#     finally:
#         Tools.success("Done!")
#         time.sleep(1)
#         menu()

def menu():
    """
    This function makes up the core functionality of the program, allowing features like adding quotes and searching.
    """
    quotes = Tools.sortDates(rawQuotes) # Takes the raw quotes list and sorts it. See exact functionality in tools.py
    quoteLists = Tools.quoteParse(quotes, logfile)
    Tools.clearScreen()
    Tools.header("CONTROLS: ")
    print("- V: View all quotes")
    print("- A: Add quotes")
    print("- D: Delete quotes")
    print("- S: Search quotes (general)")
    print("- SS: Search quotes by speaker")
    print("- ST: Search quotes by tag")
    print("- SD: Search quotes by date")
    print("- Q: Quit program")
    userInput = input(Tools.prompt("Please input an action:> ")).lower() # lower() to ensure user input sanitization
    match userInput:
        case "v": # View quotes only if there are entries in the specified CSV file
            Quotes.view(quotes)
            menu()
        case "a":
            # Add quotes
            Quotes.addQuotes(rawQuotes, quotesheet)
            menu()
        case "d":
            # Search quotes to delete
            Tools.clearScreen()
            quotesToBeDeleted = []
            searchTerms = input(Tools.prompt("Please search for the quote you wish to delete:> ")).lower()
            results = 0
            for i in range(len(quoteLists)):
                if searchTerms in quoteLists[i]:
                    results += 1
                    quotesToBeDeleted.append
                    print(f"{results}. {quotes[i]["quote"]} (said by {quotes[i]["speaker"]} on {quotes[i]["date"]})")
            if results == 0:
                Tools.error(f"No quotes found with these search terms.")
            elif results == 1:
                Tools.success(f"{results} quote(s) found.") 
                quoteToDelete = input(Tools.prompt("Pleas"))
            else:
                Tools.success(f"{results} quote(s) found.")
                deleteSelection = input(Tools.prompt(f"Please select a quote to delete (1-{results}):> "))

            input(Tools.prompt("Press enter to continue to menu..."))
            menu()           
        case "s":
            # Search quotes by word
            Tools.clearScreen()
            searchTerms = input(Tools.prompt("Please input the search terms you wish to use:> ")).lower()
            results = 0
            for i in range(len(quoteLists)):
                if searchTerms in quoteLists[i]:
                    results += 1
                    print(f"- {quotes[i]["quote"]} (said by {quotes[i]["speaker"]} on {quotes[i]["date"]})")
            if results == 0:
                Tools.error(f"No quotes found with these search terms.")
            else:
                Tools.success(f"{results} quote(s) found.") 
            input(Tools.prompt("Press enter to continue to menu..."))
            menu()
        case "ss":
            # Search quotes by speaker
            Tools.clearScreen()
            speakerSearch = input(Tools.prompt("Please input the speaker you wish to search (CASE SENSITIVE):> "))
            results = 0
            for q in quotes:
                if q["speaker"] == speakerSearch:
                    results += 1
                    print(f"- {q["quote"]} (said by {q["speaker"]} on {q["date"]})")
            if results == 0:
                Tools.error(f"No quotes found by {speakerSearch}")
            else:
                Tools.success(f"{results} quote(s) found.") 
            input(Tools.prompt("Press enter to continue to menu..."))
            menu()
        case "st":
            # Search quotes by tag
            Tools.clearScreen()
            tagSearch = input(Tools.prompt("Please input the tag you wish to search by:> ")).lower()
            results = 0
            for q in quotes:
                if tagSearch in q["tags"]:
                    results += 1
                    print(f"- {q["quote"]} (said by {q["speaker"]} on {q["date"]})")
            if results == 0:
                Tools.error(f"No quotes found with the tag '{tagSearch}'")
            else:
                Tools.success(f"{results} quote(s) found with the tag '{tagSearch}'.") 
            input(Tools.prompt("Press enter to continue to menu..."))
            menu()
        case "sd":
            # Search quotes by date
            dateSearch = Tools.formatDate(input(Tools.prompt("Please input the date you wish to search by:> ")))
            results = 0
            for q in quotes:
                if dateSearch in q["date"]:
                    results += 1
                    print(f"- {q["quote"]} (said by {q["speaker"]} on {q["date"]})")
            if results == 0:
                Tools.error(f"No quotes found with the date '{dateSearch}'")
            else:
                Tools.success(f"{results} quote(s) found with the tag '{dateSearch}'.") 
            input(Tools.prompt("Press enter to continue to menu..."))
            menu()
        case "q":
            exit() # Exit program
        case _:
            Tools.error("Bad command or quote!")
            time.sleep(1)
            menu()

Quotes.initialize(quotesheet, rawQuotes, menu())