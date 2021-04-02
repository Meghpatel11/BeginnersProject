import random

win,lose,drow = 0,0,0
com = random.choice(['r','p','s'])

play_again = "y"

while play_again == 'y':

    user = input("Opt Rock(r), Paper(p) or Scissors(s)")
    com = random.choice(['r','p','s'])

    print(f'you opted: {user}')
    print(f'computer opted: {com}')

    if user == com:
        print("It's Draw")
        drow +=1
    elif (user == 'r' and com == 's') or (user == 'p' and com == 'r') or (user == 's' and com == 'p'):
        print("You Win!!")
        win +=1
    else:
        print("You lose!!")
        lose +=1
    
    play_again = input("Play Once again?[y/n]")

print('You Have: ' + str(win) + ' Wins '  + str(lose) + ' loses ' + str(drow) + ' drows ' )