rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

from random import randint


def main():
    
    rps = {0: rock, 1: paper, 2: scissors}
    input_ = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    print(rps[input_])
    comp = randint(0,2)
    print(f"Computer chose:\n{rps[comp]}")
    
    if input_ == comp:
        print("Draw")
    elif (input_ == 0 and comp == 2) or (input_ == 1 and comp == 0) or (input_ == 2 and comp == 1):
        print("You win")
    else:
        print("You lose") 
    
    
    
if __name__ == "__main__":
    main()