#Exercise: Home Federal Savings Bank
#Create greeting ignored any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
def main():
    greeting = input("Greeting: ")
    print(value(greeting))

#conditionals by greetings
def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()