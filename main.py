from game import Game
from game_settings import Game_settings


class Main:
    def __init__(self):
        game = Game()
        self.is_correct = False
        self.is_correct_letter = False
        self.has_chances = 5
        self.correct_letters = 0
        self.already_used_letters = []

        Game_settings.check_os()
        game.show_user_try()

        while self.is_correct == False and self.has_chances > 0:
            print(100 * '_')
            user_try = input('Choose a letter or type 1 to guess: ').lower()
            while len(user_try) == 0:
                user_try = input(
                    'Choose a letter or type 1 to guess: ').lower()

            user_try = user_try[0]

            if user_try == '1':
                user_try = input('What is the word : ').lower()
                word_check = game.check_word(user_try)
                game.show_user_try()
                if word_check == True:
                    self.is_correct = True
                    break
            else:
                if user_try in self.already_used_letters:
                    game.default_print('Letter already used...')
                    continue
                else:
                    self.already_used_letters.append(user_try)
                    letter_check = game.check_letter(user_try)
                    if letter_check is not None:
                        correct_letters_amount = game.change_hash(
                            letter_check, user_try)
                        self.is_correct_letter = True
                        self.correct_letters += correct_letters_amount
                    else:
                        self.is_correct_letter = False

                    if self.correct_letters == game.secret_word_length:
                        self.is_correct = True

            if self.is_correct_letter == False:
                self.has_chances -= 1

            game.show_user_try()
            game.default_print(f"Chances left: {self.has_chances}")

        if self.is_correct == True and self.has_chances > 0:
            game.default_print(
                f'You Win, the word was {game.secret_word.capitalize()}, congratulations!!!')
        else:
            game.default_print(
                f'You Lost, the word was "{game.secret_word.capitalize()}", good luck next time!')


if __name__ == '__main__':
    main = Main()
