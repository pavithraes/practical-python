# bounce.py
#
# Exercise 1.5

def bounce():
    height = 100
    for n in range(1,11):
        height *= 3/5
        print (n, round(height, 4))
    return 0

if __name__ == "__main__":
    bounce()
