# --- Define your functions below! ---

def status():
    input("\nI'm well! How are you?: ")
    print("\nThanks for letting me know!\n")

def goodbye():
    print("\nAre you sure you want to leave?\n")
    return input("Enter yes or no: ").lower()

def greeting(greet):
    print("\nWell, {grt} to you too!\n".format(grt=greet))

def compliment():
    print("\nAw, thanks!\n")

def yert():
    print("\nYERT!\n")

def yeet():
    print("\nYEET!\n")

greetings = ["hey", "hi", "hello"]
farewells = ["quit", "goodbye", "leave", "exit", "bye", "farewell"]
compliments = ["you're cool", "i love you", "you are awesome", "you are dope"]

def process_input(ans):
    if ans in greetings:
        greeting(ans)
    elif ans in "what's up?" or ans in "how are you":
        status()
    elif ans in compliments:
        compliment()
    elif ans == "yeet":
        yert()
    elif ans == "yert":
        yeet()
    else:
        print("\nI didn't quite get that.\n")

# --- Put your main program below! ---
def main():
  while True:
    answer = input("\n(What will you say?) ").lower()
    if answer not in farewells:
        process_input(answer)
    else:
        response = goodbye()
        if response == "yes":
            print("\nGoodbye!\n")
            return False




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
