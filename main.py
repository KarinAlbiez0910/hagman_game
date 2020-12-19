import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
  display.append('_')

print(display)

lives = 6

end_of_game = False
while not end_of_game:

  guess = input("Guess a letter: ").lower()
    
  if guess in display:
    print(f'You have already guessed the letter "{guess}" previously.')
 
  for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
      display[letter] = guess
  
  if guess not in chosen_word:
    lives = lives - 1
    print(f'The letter "{guess}" is not in the chosen word.')
  
  print(display)
  print(hangman_art.stages[lives])

  if '_' not in display:
    end_of_game = True
    print( 'You win.')

  if lives == 0:
    end_of_game = True
    print('You lose.')