import random
# this is a code to play rock paper scissors with a computer
def rps():
    print ("Lets Play Rock Paper Scissors")
    RPS = ["rock","paper", "scissors"]
    aa =str(random.choice(RPS))
# the computer would pick randomly between R P and S
    Choice =input("pick either rock , paper or scissors (this exact spelling):")
    choice = Choice.lower()
# makes the text all small letter (RoCK = rock)
    print ("Rock smashes scissors, Scissors cut paper, Paper wraps rock")
    if choice == aa:
        print("The compuater choose "+ aa + " and you choose " + choice)
        print("its a draw")
    
    elif choice == "rock":
        if aa == "scissors":
            print("The compuater choose "+ aa + " and you choose " + choice)
            print("CONGRATULATIONS you win")
        else:
            print("The compuater choose "+ aa + " and you choose " + choice)
            print('you lose')
    
    elif choice == "scissors":
        if aa == "paper":
            print("The compuater choose "+ aa + " and you choose " + choice)
            print("CONGRATULATIONS you win")
        else:
            print("The compuater choose "+ aa + " and you choose " + choice)
            print('you lose')
    elif choice == "paper":
        if aa == "rock":
            print("The compuater choose "+ aa + " and you choose " + choice)
            print("CONGRATULATIONS you win")
        else:
            print("The compuater choose "+ aa + " and you choose " + choice)
            print('you lose')
    elif choice != "paper" or"scissors" or "rock":
        print("choose a proper option to play the game")
rps()        



