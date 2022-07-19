n = int(input())

cards = ["1", "2", "3", "4", "5", "6"]

res = n // 5 % 6
mod = n % 5

new_cards = cards[res:] + cards[:res]

copy_cards = new_cards[1 : mod + 1] + [new_cards[0]] + new_cards[mod + 1 :]
print("".join(copy_cards))