# 15/02/2022

def main():
    print("Hello user! Welcome to the Band Name Generator.")
    city = str(input("In what city do you grew up?\n"))
    pet = str(input("What do you think is a nice name for a pet?\n"))
    print(f"Here is your new band name: {city} {pet}")
    
if __name__ == "__main__":
    main()