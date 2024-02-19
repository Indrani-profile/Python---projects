import random

def problem():

  while True:

    x = random.randint(0,9)

    y = random.randint(0,9)

    print("How much is " + str(x) + " times " + str(y) + "?")

    answer = int(input("What is the answer? "))

    if answer == (x * y):

      correct = ['Very good!']

      response = random.choice(correct)

      print(response)

    while answer != (x * y):

      incorrect = ['No. Keep trying']

      response1 = random.choice(incorrect)

      print(response1)

      print("How much is " + str(x) + " times " + str(y) + "?")

      answer = int(input("What is the answer? "))

      if answer == (x * y):

        print(response)

def main():

  problem()
main()