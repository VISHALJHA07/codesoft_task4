import random

def play_again():
  
  while True:
    choice = input("Do you want to play again? (yes/no) ").lower()
    if choice in ("yes", "no"):
      return choice == "yes"
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")

def determine_winner(user_choice, computer_choice):
  
  choices = ["rock", "paper", "scissors"]
  win_index = (choices.index(user_choice) + 1) % 3  # Offset for win condition
  if computer_choice == choices[win_index]:
    return "Computer"
  elif computer_choice == user_choice:
    return "Tie"
  else:
    return "User"

def play_game():
  
  user_score = 0
  computer_score = 0
  while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice in ("rock", "paper", "scissors"):
      computer_choice = random.choice(["rock", "paper", "scissors"])
      print(f"You chose {user_choice}, computer chose {computer_choice}.")
      winner = determine_winner(user_choice, computer_choice)
      if winner == "User":
        user_score += 1
        print("You win!")
      elif winner == "Computer":
        computer_score += 1
        print("You lose.")
      else:
        print("It's a tie!")
      print(f"Current score: User - {user_score}, Computer - {computer_score}")
      if not play_again():
        break
    else:
      print("Invalid input. Please enter rock, paper, or scissors.")

if __name__ == "__main__":
  print("Welcome to Rock-Paper-Scissors!")
  play_game()
  print("Thanks for playing!")
