import random; # need the random integer to generate computer's moves

print # instructions
print ('Welcome to a little game called Rock, Paper, Scissors.');
print ('Or Roshambo, if you want to get fancy. We play like this:');
print ('Type 1 for Rock, 2 for Paper, and 3 for Scissors.');

print ('Type 0 to exit');

while 1: # gameplay
    z=random.randint(1,3);
    a=int(input("What'll it be? "));
    if a==z:
        print ('Tie!');

    if a==1 and z==2:
        print ('You are a rock covered in paper. Better luck next time.');

    if a==1 and z==3:
        print ('You have just smashed my scissors to pieces. Awesome.');

    if a==2 and z==3:
        print ('Scissor cuts paper. Sorry!');

    if a==2 and z==1:
        print ('Paper covers rock. Good work!');

    if a==3 and z==2:
        print ('Scissors cuts paper. Wahoo!');

    if a==3 and z==1:
        print ('Your scissors have been smashed to smithereens. Try again!');

    if a==0:
        break

# end message to user
print ('Thanks for playing the game. Go lick your wounds and come back as a more challenging opponent.')
