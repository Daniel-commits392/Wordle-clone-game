Word='board'
word_length=len(Word)
Attempts=6

for attempt in range(1,Attempts+1):
   print(f'Attempt {attempt} out of {Attempts} attempts')
   players_guess=input('Enter your guess : ')
   lower_guess=players_guess.lower()
   if len(lower_guess)!=word_length:
      print(f'Error! Guess has to be {word_length} letters long')
      continue #this skips the current round ofthe game and asks for a new one
   if lower_guess==Word:
      print('👏Congrats🎉.YOU WIN!!')
      break
   
   Feedback=[]
   for i in range(word_length):
     if lower_guess[i]==Word[i]:
      Feedback.append('🟩') 
     elif lower_guess[i] in Word:
       Feedback.append('🟨')
     else:
       Feedback.append('⬜')
   print(''.join(Feedback))

   
   

      
      