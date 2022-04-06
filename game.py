def Gen():
    
    import random #Library for random numbers
    
    cards = [2,3,4,5,6,7,8,9,10,'J','K','Q','A'] #Create a list 
    
    # Player 1

    #Pick 2 random cards for player one
    card1 = random.choice(cards)
    card2 = random.choice(cards)

    #card1 and card2 are classes of str? the answer is a boolean 
    check1 = isinstance(card1,str)
    check2 = isinstance(card2,str)

    #Interaction with the user
    Player1 = input("What\'s your name?")
    print(Player1, "Your cards are: ",card1,card2)

    """Check for a string -and- the type of character it is. If is a string "A", "K"
     "Q" or "J"and it will be converted to an integer (11 or 10)"""
    
    if check1 == True and card1 == 'A':
        card1 = int(11)
        
    elif check1 == True:
        card1 = int(10)


    if check2 == True and card2 == 'A':
        card2 = int(11)
        
    elif check2 == True:
        card2 = int(10)

   #If they were not strings, then it will skip the if statements because they were integer (2-10)
    
   #The sum of the cards   
    Sum1 = card1 + card2

   #Print the result    
    print('Your score is: ',Sum1)

    More0 = input("Press H for Hit me or S for Stand")
    while More0 == "H":
     card6 = random.choice(cards)
     check6 = isinstance(card6,str)
     print(Player1, "Your card is: ",card6)
     if check6 == True and card6 == 'A':
        card6 = int(11)
     elif check6== True:
        card6 = int(10)
     Sum1 = Sum1 + card6
     print('Your scoresss is: ',Sum1)
     More0 = input("Press H for Hit me or S for Stand")
        
    # Player 2, repeats the whole process

    Player2 = input("What\'s your name?")

    # cards was already defined at the begining no need to create it twice

    card3 = random.choice(cards)
    card4 = random.choice(cards)
    
    check3 = isinstance(card3,str)
    check4 = isinstance(card4,str)
    
    print(Player2, "Your cards are: ",card3,card4)
    
    if check3 == True and card3 == 'A':
        card3 = int(11)
        
    elif check3 == True:
        card3 = int(10)
    
    if check4 == True and card4 == 'A':
        card4 = int(11)
        
    elif check4 == True:
        card4 = int(10)
        
    Sum2 = card3 + card4
    
    print('Your score is: ',Sum2)

    More = input("Press H for Hit me or S for Stand")
    while More == "H":
     card5 = random.choice(cards)
     check5 = isinstance(card5,str)
     print(Player2, "Your card is: ",card5)
     if check5 == True and card5 == 'A':
        card5 = int(11)
     elif check5 == True:
        card5 = int(10)
     Sum2 = Sum2 + card5
     print('Your scoresss is: ',Sum2)
     More = input("Press H for Hit me or S for Stand")
  
    # Who is winner
    
    if Sum1 < 22 and Sum2 <22 and Sum1 > Sum2:
        print(Player1 , "Won")
        
    elif Sum1 < 22 and Sum2 <22 and Sum1 < Sum2:
        print(Player2 , "Won")

    elif Sum1 > 21 and Sum2 <22: 
        print(Player2 , "Won", Player1, "Over the top")

    elif Sum1 < 22 and Sum2 > 21:
        print(Player1 , "Won", Player2, "Over the top")
    else:
        print("Both when over the top")
        
            
Gen() 
