from art import logo, vs
from game_data import data
import random

print(logo)
import random

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },

]

import random


def format(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"


def check(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
B = random.choice(data)
end_game = True
while end_game:

    A = B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)

    print(f"Compare A:{format(A)} \n")
    print(vs, '\n')
    print(f"Against B:{format(B)} \n")
    # Ask user for a Guess
    guess = input("Who has more followers A or B:").lower()
    # Getting Count
    followers_a = A['follower_count']
    followers_b = B['follower_count']
    # store the function in a variable to make use of it
    count = check(guess, followers_a, followers_b)

    if count:
        score += 1
        print(f"you are right.your score is {score}")
    else:
        end_game = False
        print(f"you are wrong.your score is {score}")


