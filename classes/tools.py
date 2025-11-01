from dateutil import parser
from datetime import datetime
from termcolor import colored, cprint
import os

class Tools:
    """
    The tools class is used to incorporate various functions for organizational purposes.
    """
    def formatDate(date):
        """
        Format every date into mm/dd/yyyy for later sorting purposes.
        """
        try:
            finalDate = parser.parse(date).date() # Turn datestr into a datetime object
            return finalDate.strftime("%m/%d/%Y") # Format datetime object into the proper format
        except:
            print("Invalid date! Please try again.") 

    def sortDates(arr):
        """
        This function is used to sort the dates for the quotes array, for better user experience.
        """
        unknownArr = [] # All the quotes with an unknown or blank date.
        sortedUnknownArr = [] # Unknown quotes sorted by speaker
        validArr = [] # All the quotes with a date that can be turned into a datetime object (unsorted)
        newArr = [] # The final array combining unknownArr and validArr
        sortedArr = [] # Same as validArr but sorted
        for q in arr: # Take the provided arr (rawQuotes) and sort it between the first two arrays
            if q["date"] == "Unknown date" or q["date"] == "":
                unknownArr.append(q)
            else:
                validArr.append(q)
        try: # Try to sort validArr items by date key.
            sortedArr = sorted(validArr, key=lambda q: datetime.strptime(q["date"], "%m/%d/%Y"))
        except ValueError as e:
            Tools.error(f"An error occured!: {e}")
        try: # Try to sort unknownArr items by Speaker.
            sortedUnknownArr = sorted(unknownArr, key=lambda q: q["speaker"])
        except ValueError as e:
            Tools.error(f"An error occured!: {e}")
        newArr = sortedUnknownArr + sortedArr # Avengers: Assemble!
        return newArr
    
    def inputDate():
        """
        Used to help the user input a proper date.
        """
        while True:
            dateInput = input(Tools.prompt("Quote date? (Any format, leave blank for none):> "))
            if dateInput == "": # If left blank, fill with "Unknown date"
                return "Unknown date"
            else:
                return Tools.formatDate(dateInput)
            
    def inputTags(array):
        """
        A looping function to add as many tags to each quote as possible for organizational purposes
        """
        while True: # While the function is active, do all this
            print(f"Tags: {array}")
            quoteTag = input(Tools.prompt("Enter a tag to categorize this quote. Type 'back' to delete the last and leave blank when done:> ")).lower()
            if quoteTag == "": # If left empty, no more tags! (Break the loop)
                if len(array) == 0:
                    array.append("No tags")
                break
            elif quoteTag == "back": # If "back", delete the last tag
                try:
                    array.pop()
                except:
                    Tools.error("No tags to delete!")
            else:
                array.append(quoteTag) # Every other tag is to be applied to the quote

    def view(arr): 
        """
        View all sorted quotes.
        """
        for i in range(len(arr)): # Sort by index, not by object.
            print(f"- {arr[i]["quote"]} (said by {arr[i]["speaker"]} on {arr[i]["date"]})")
    
    def clearScreen():
        """
        Clear the screen depending on OS (pending).
        """
        if os.name == "nt": # Windows NT, so everything XP and onwards
           _ = os.system("cls")
        else: # Linux and MacOS
           _ = os.system("clear")

    def quoteParse(arr, logfile):
        """
        This function is used to parse each quote into alphanumeric words for both the search and delete features.
        """
        parsedArr = []
        for q in arr: 
            goodChars = []
            for char in list(q["quote"].lower()):
                if char.isalnum() == True or char == " ":
                    goodChars.append(char)
            parsedArr.append("".join(goodChars).split())
        with open(logfile, "w") as file:
            file.write("# THIS FILE IS INTENDED TO KEEP A LOG OF QUOTES FOR TROUBLESHOOTING REGARDING SEARCHTERMS.\n\n")
            file.write(str(parsedArr))
        return parsedArr
    
    def header(str):
        cprint(str, "white", attrs=["bold"])

    def error(str):
        cprint(str, "red", attrs=["bold"])

    def success(str):
        cprint(str, "green")
    
    def prompt(str):
        return colored(str, "yellow")