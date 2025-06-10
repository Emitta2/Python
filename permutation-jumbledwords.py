import random                     # Importing random module to use for random word selection and shuffling

def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics',
             'player', 'condition', 'reverse', 'water', 'board'] 
    pick = random.choice(words)   # in random library there is a function for choice which will pick some element from list
    return pick  

# eg.string tokenizer,counting no of words in a sentence,done by counting the no of blank spaces
def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))  
    return jumbled 

def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is :', p1)  
    print(p2n, 'Your score is :', p2)  
    print('Thanks for playing')        
    print('Have a nice day')           

def play():
    p1name = input('Player 1, Please enter your name: ') 
    p2name = input('Player 2, Please enter your name: ') 
    pp1 = 0                                  # Points for Player 1
    pp2 = 0                                  # Points for Player 2
    turn = 0                                 #to keep track of turns(alternate turns)
    p1_active = True                         # True if Player 1 has not quit
    p2_active = True                         # True if Player 2 has not quit
    max_turns = 5                            # Maximum allowed turns per player
    p1_turns = 0  
    p2_turns = 0  

    while p1_turns < max_turns or p2_turns < max_turns:
        # Computer's task
        picked_word = choose()               # choose a word from the list
        qn = jumble(picked_word)             # Jumbling 
        print("\nJumbled word is:", qn)  

        # Player 1 (even turns)
        if turn % 2 == 0 and p1_turns < max_turns:  
            if p1_active:  
                print(p1name, 'Your turn.')  
                ans = input('What is on my mind? ')  
                if ans == picked_word:  
                    pp1 += 1  
                    print('Your score is :', pp1)  
                else:
                    print('Better luck next time. I thought :', picked_word)  
                c = int(input('Press 1 to continue and 0 to quit: '))  
                if c == 0:
                    p1_active = False       # Mark Player 1 as inactive if they choose to quit
            else:
                print(p1name, 'has quit.')  # Skip turn if Player 1 has quit
            p1_turns += 1                   # Count the turn whether Player 1 played or skipped

        # Player 2 (odd turns)
        elif turn % 2 == 1 and p2_turns < max_turns:  
            if p2_active:  
                print(p2name, 'Your turn.')  
                ans = input('What is on my mind? ')  
                if ans == picked_word:  
                    pp2 += 1  
                    print('Your score is :', pp2) 
                else:
                    print('Better luck next time. I thought :', picked_word)  
                c = int(input('Press 1 to continue and 0 to quit: '))  
                if c == 0:
                    p2_active = False       # Mark Player 2 as inactive if they choose to quit
            else:
                print(p2name, 'has quit.')  # Skip turn if Player 2 has quit
            p2_turns += 1                   # Count the turn whether Player 2 played or skipped

        turn += 1                           # Increment overall turn counter to alternate between players
    
    thank(p1name, p2name, pp1, pp2)  

play()

"""
sample output1:
Player 1, Please enter your name: a
Player 2, Please enter your name: b

Jumbled word is: svrreee
a Your turn.
What is on my mind? reverse
Your score is : 1
Press 1 to continue and 0 to quit: 1

Jumbled word is: lryaep
b Your turn.
What is on my mind? rayelp
Better luck next time. I thought : player
Press 1 to continue and 0 to quit: 0

Jumbled word is: rdaob
a Your turn.
What is on my mind? board
Your score is : 2
Press 1 to continue and 0 to quit: 1

Jumbled word is: erevsre
b has quit.

Jumbled word is: rlpyae
a Your turn.
What is on my mind? player
Your score is : 3
Press 1 to continue and 0 to quit: 0

Jumbled word is: pigorngammr
b has quit.

Jumbled word is: sniceec
a has quit.

Jumbled word is: mhieamscatt
b has quit.

Jumbled word is: gpormgmanir
a has quit.

Jumbled word is: elarpy
a Your score is : 3
b Your score is : 0
Thanks for playing
Have a nice day

sample output2:
Player 1, Please enter your name: as
Player 2, Please enter your name: df

Jumbled word is: erreves
as Your turn.
What is on my mind? reverse
Your score is : 1
Press 1 to continue and 0 to quit: 1

Jumbled word is: aorbinw
df Your turn.
What is on my mind? rainbow
Your score is : 1
Press 1 to continue and 0 to quit: 1

Jumbled word is: toincoind
as Your turn.
What is on my mind? dffe
Better luck next time. I thought : condition
Press 1 to continue and 0 to quit: 1

Jumbled word is: taerw
df Your turn.
What is on my mind? dfd
Better luck next time. I thought : water
Press 1 to continue and 0 to quit: 1

Jumbled word is: cmroupet
as Your turn.
What is on my mind? computer
Your score is : 2
Press 1 to continue and 0 to quit: 1

Jumbled word is: seniecc
df Your turn.
What is on my mind? ffg
Better luck next time. I thought : science
Press 1 to continue and 0 to quit: 1

Jumbled word is: codoinnti
as Your turn.
What is on my mind? fggfgf
Better luck next time. I thought : condition
Press 1 to continue and 0 to quit: 1

Jumbled word is: trewa
df Your turn.
What is on my mind? water
Your score is : 2
Press 1 to continue and 0 to quit: 1

Jumbled word is: tware
as Your turn.
What is on my mind?
Better luck next time. I thought : water
Press 1 to continue and 0 to quit: 1

Jumbled word is: aorbd
df Your turn.
What is on my mind? eege
Better luck next time. I thought : board
Press 1 to continue and 0 to quit: 1
as Your score is : 2
df Your score is : 2
Thanks for playing
Have a nice day

"""