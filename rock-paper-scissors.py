#the way I would do it
import random, sys
print("A game of Rock, Paper, Scissors")
wins = 0
losses = 0
ties = 0

while True: #game loops
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #Player input loop
        print('What do you choose?' + ' '+ 'r for rock p for paper or s for scissors?' + ' ' + 'You may enter q to quit the game.')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quits game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #exits player input loop
        print('Type one of the action keys r, p, s, or q.')

            # Display what player chose:
    if playerMove == 'r':
        print ('Rock buldges its muscles preparring to smash ')
    elif playerMove == 'p':
            print ("Paper pulls out a knife's edge from another demension")
    elif playerMove == 's':
        print('Scissors summons its ancesstors')
            
        # Display what the computer chose:
        randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('AI poops out a Rockslide')
    elif randomNumber == 2:
        computerMove = 'p'
        print('AI chooses to summon Ryan Renolds who gives you a paper cut!')
    elif randomNumber == 3:
        computerMove = 's'
        print('AI throws up scissors with the blades pointing in your direction...')
        
    # Records and shows wins, losses, ties:
    if playerMove == computerMove:
        print('Both attacks are ineffective... Tie.)
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You slaugter your enimes well young one.')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Your preformance of interdemsional space-shifting succeeds')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('The Scissors ancesstors smile upon you this day. You earned a win.')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print(' You dishonor your family with failure you know...')
        losses = losses +1
    elif playerMove == 'p' and computerMove == 's':
        print("AI's blades cut your chances of being a winner...Loser")
    elif playerMove == 's' and computerMove == 'r':
        print('You have poop all over you from that rockslide you know...')
        losses = losses + 1
        
#this is just practice on python for me
