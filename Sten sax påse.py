import random  #  importerar random för att datorn ska göra slumpmässiga val

def game():   #  definer game för att senare skriva in koderna i definitionen
    choices = ['sten', 'sax', 'påse']  #sätter upp vilka val datorn kommer att ha att välja mellan
    user_choice = input("Välj sten, sax eller påse: ").lower() #ber spelaren att välja ett utav tre alternativen och att skriva in
    computer_choice = random.choice(choices)  #datorn väljer ett av de tre valen slumpmässigt

    print(f"Datorn valde: {computer_choice}") #skriver vad datorn valt

    if user_choice == computer_choice: #kontrollerar ifall spelaren och datorn valt samma
        print("Oavgjort!")  #skriver oavgjort
    elif (user_choice == 'sten' and computer_choice == 'sax') or \
         (user_choice == 'sax' and computer_choice == 'påse') or \
         (user_choice == 'påse' and computer_choice == 'sten'):  # #skriver alla vinnandekombinatoner
        print("Grattis, du vann!") #skriver att användaren vunnit
    else: #ifall spelaren inte vinner
        print("Tyvärr, du förlorade!") #skriver ifall spelaren förlorat

while True: #skapar en loop så att spelet fortsätter tills spelaren väljer att avsluta
    game() #anropar funktionen game för att spela
    play_again = input("Vill du spela igen? (ja/nej): ").lower() # frågar ifall spelaren vill fortsätta spela
    if play_again != 'ja':   #  ifall spelaren väljer ja i åvan fråga så fortsätt
        break # annars breakgit .