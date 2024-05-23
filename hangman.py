import random

word_list= ["ardvark","baboon","camel"]
HANGMANPICS = [r"""
  +---+
  |   |
      |
      |
      |
      |
=========""", r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(r''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                  ''')
randoWord= random.choice(word_list)
#randoWordList=list(randoWord)
guessWord = []
fail = 0
findLetter = False

for l in randoWord:
    guessWord.append("_")
while fail<6:
    letter = input("guess a letter: ").lower()
    index=0
    for l in randoWord:
        if l==letter:
            findLetter=True
            guessWord[index]=letter
        index+=1
    if findLetter==True:
        findLetter=False

    else:
        fail+=1

    print(guessWord)
    print(f"You had {fail} wrong guess!!")
    print(HANGMANPICS[fail])

    if "_" not in guessWord:
        fail=7


if "_" in guessWord:
    print("Game Over")
else:
    print("You win!!!")
