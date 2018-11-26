print('Rock Paper Scissors')
player1_choice=input('Please Player 1,Enter one matching one of these three words: ')
player2_choice=input('Please Player 2,Enter one matching one of these three words: ')
if player1_choice=='Rock' and player2_choice=='Scissors' or player1_choice=='Scissors' and player2_choice=='Paper' or player1_choice=='Paper' and player2_choice=='Rock' :
    winner='Player 1'
else :
    winner='Player 2'
print(winner + ' wins,, Congratulations')
