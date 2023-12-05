class GameData:
    def __init__(self, game: str):
        # Split the input string into game number and hands data
        game_number, self.hands_data = map(str.strip, game.replace("Game ", "").split(":", 1))

        self.game_number = int(game_number)
        self.max_hand = self.parse_hands()

    def parse_hands(self) -> dict:
        # Split the hands data and initialize max_hand dictionary
        hand_values = self.hands_data.replace(";", ",").split(", ")

        max_hand = {"red": 0, "green": 0, "blue": 0}

        # Update max_hand dictionary based on hand values
        for hand in hand_values:
            value, color = hand.split()

            max_hand[color] = max(max_hand[color], int(value))

        return max_hand

    def compare_hands(self, goal: dict) -> bool:
        for key in self.max_hand:
            if self.max_hand[key] > goal.get(key, 0):
                print(f"{key}: {self.max_hand[key]} is greater than {goal.get(key, 0)}")
                return False
        return True

    def get_game_number(self) -> int:
        return self.game_number


goal_hand = {
    "red": 12,
    "green": 13,
    "blue": 14
}

winning_hands = []

# with open('input.txt', 'r') as file:
#     for line in file:
#         new_game = GameData(line)
#         is_winning = new_game.compare_hands(goal_hand)
#
#         if is_winning:
#             winning_hands.append(int(new_game.get_game_number()))


products = []

with open('input.txt', 'r') as file:
    for line in file:
        new_game = GameData(line)
        min_required = new_game.parse_hands()

        lst_nums = list(min_required.values())

        product = 1

        for num in lst_nums:
            product *= num

        products.append(product)

print(sum(products))



