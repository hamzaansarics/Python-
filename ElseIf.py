play=38
s=int(input("Put a Number to Guess"))
if s==play:
    print("Well Done You Win the Game!!")
elif s > play:
    print("Too High")
elif s<play:
    print("Too Low")

