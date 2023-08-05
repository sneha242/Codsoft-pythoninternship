
#Asking user if they want to play 

print('Welcome to my computer quiz')
playing = input("\n Do you want to play?\n").lower()
if playing !='yes' :
    quit()
else:
    #The game begins here, The score will be displayed at the end.
    print('Okay,Lets play!!\n')
    cor=0

    answer= input('What does CPU stands for?\n').lower()
    if answer== 'central processing unit':
        print('Correct!\n')
        cor+=1
    else :
        print('Incorrect!\n')
        print('The correct answer is Central Processing Unit \n')
        

    answer= input('What does RAM stands for?\n').lower()
    if answer== 'random access memory':
        print('Correct!\n')
        cor+=1
    else :
        print('Incorrect!\n')
        print('The correct answer is Random Access Memory')

    answer= input('What does GPU stands for?\n').lower()
    if answer == 'graphics processing unit': 
        print('Correct!\n')
        cor+=1
    else :
        print('Incorrect!\n')
        print('The correct answer is Graphics Processing Unit')
    print('Congrats..! you got' +   str(cor)   +  '  questions correct\n')
   


