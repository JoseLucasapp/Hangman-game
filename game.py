from random_word import RandomWords

class Game:
  def __init__(self):
    rand_word = RandomWords()
    self.secret_word = rand_word.get_random_word().lower()
    self.secret_word_length = len(self.secret_word)
    self.hash = f'_' * self.secret_word_length

  def check_word(self, word):
    if word == self.secret_word:
      return True
    else:
      return False
    
  def check_letter(self, letter):
    if letter in self.secret_word:
      return self.secret_word.index(letter)
    else:
      return None
    
  def change_hash(self, index, letter):

    new_hash = list(self.hash)
    letters_amount = 0
    for i in range(0, self.secret_word_length):
      if letter == self.secret_word[i]:
        new_hash.pop(i)
        new_hash.insert(i, letter)
        letters_amount += 1
      
    self.hash = ''.join(new_hash)
    return letters_amount

  def check_won(self, correct_letters):
    if self.secret_word_length == correct_letters:
      return True
    else:
      return False
    
  def show_user_try(self):
    print(' ')
    print(" ".join(self.hash))
    print('')

  def default_print(self, text):
    print(' ')
    print(text)
    print(' ')