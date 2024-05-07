# Write your code here
def card_value(string):
    if string <= 10 and string > 0:
        return int(string)
    elif string == "Jack":
        return 11
    elif string == "Queen":
        return 12
    elif string == "King":
        return 13
    elif string == "Ace":
        return 1
