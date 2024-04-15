import random

def game():
    choices = ['sten', 'sax', 'påse']
    user_choice = input("Välj sten, sax eller påse: ").lower()
    computer_choice = random.choice(choices)

    print(f"Datorn valde: {computer_choice}")

    if user_choice == computer_choice:
        print("Oavgjort!")
    elif (user_choice == 'sten' and computer_choice == 'sax') or \
         (user_choice == 'sax' and computer_choice == 'påse') or \
         (user_choice == 'påse' and computer_choice == 'sten'):
        print("Grattis, du vann!")
    else:
        print("Tyvärr, du förlorade!")

while True:
    game()
    play_again = input("Vill du spela igen? (ja/nej): ").lower()
    if play_again != 'ja':
        break