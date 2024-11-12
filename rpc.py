def main():
      print("Welcome to Rock Paper Scissors!")
      print("Rules: Rock beats scissors, scissors beats paper, paper beats rock.")

      choices = ["rock", "paper", "scissors"]
      while True:
          user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
          computer_choice = random.choice(choices)
          print(f"Computer chose: {computer_choice}")

          if user_choice == computer_choice:
              print("It's a tie! Let's play again.")
          elif (user_choice == "rock" and computer_choice == "scissors") or \
               (user_choice == "scissors" and computer_choice == "paper") or \
               (user_choice == "paper" and computer_choice == "rock"):
              print("You win!")
              break
          else:
              print("You lose!")
              break