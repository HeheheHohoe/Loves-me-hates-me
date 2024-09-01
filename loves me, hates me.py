import random
import time

loveme = ["loves me,", "adores me,", "admires me,", "cherishes me,", "treasures me,"]
hateme = ["hates me,", "detests me,", "despises me,", "loathes me,", "dislikes me,"]
petalcountchoices = [5, 6, 7, 8, 9, 10, 11, 12]
count = random.choice(petalcountchoices)
either = 0

thething = input("I decided to see if my: ")
print("loves me or hates me using this flower!. I'll pluck the petals until the answer is revealed...")
time.sleep(1)

while count > 0:
    if either == 0:
        print(random.choice(loveme))
        either = 1
    else:
        print(random.choice(hateme))
        either = 0
    time.sleep(1)
    count -= 1

print("I have plucked the last petal!")
time.sleep(1)

if either == 0:
    resultL = random.choice(loveme)
    print("Turns out", thething, resultL.upper(), "amazing!")
else:
    resultH = random.choice(hateme)
    print("Unfortunately,", thething, resultH.upper(), "):")
