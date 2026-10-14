# GUSSSEING NUMBER GAME:
import random as number
number=number.randrange(1,100)
input1=int(input("ENTER YOUR NUMBER:"))
for i in range(0,5):
    print("PROCESSING...")
if input1<number:
    print("THE NUMBER",input1,"LESS THEN",number,'PLEASE TRY AGAIN:')
    enter_user1=str(input("ENTER Y IF YOU WANT TO PLAY OR IF NOT SO ENTER N:"))
    # if user want play again 
    if enter_user1=="Y":
        user_input1=int(input("ENTER YOUR NUMBER:"))
        # IF USER PLAY AGAIN AND ANSWER IS LESS THEN NUMBER
        if user_input1<number:
            print("YOU GET AGAIN LESS THEN",number)
            # IF USER TELLING TO PLAY ONE LAST TIME
            enter_user_input1=str(input("NOW TELL US YOU WANT TO PLAY OR NOT AND THIS IS THE LAST TIME \nIF ANSWER WRONG SO YOU ARE OUT Y/N:" ))
            if enter_user_input1=="Y":
                # ITS HAPPEN WHEN USER SAID HE WANT TO PLAY ONE LAST TIME
                number_enter_user_input1=int(input("ENTER YOUR NUMBER:"))
                if number_enter_user_input1<number:
                    print("YOU GET AGAIN LESS THEN",number)
                    print("YOU ARE OUT:")
                elif number_enter_user_input1>number:
                    print("THIS TIME YOU GET GREATER THEN",number,"\nBUT YOU ARE OUT:")
                elif number_enter_user_input1==number:
                    print('THIS TIME YOU GET LUCK AND YOU WON',number_enter_user_input1,"AND",number,"BOTH ARE SAME WELL DONE:")
            # ITS HAPPEN WHEN USER SAID HE DOES'NT WANT TO PLAY one last time
            elif enter_user_input1=="N":
                print("OK AS YOU WISH GAME END NOW :")
                 # THIS CONDITION WILL BE WORK WHEN  LINE 14 TO 29 WILL BE False
        elif user_input1>number:
            print("YOU GET GREATER THEN",number,"TRY AGAIN:")
            enter2_user_input1=str(input("NOW TELL US YOU WANT TO PLAY OR NOT AND THIS IS THE LAST TIME \nIF ANSWER WRONG SO YOU ARE OUT Y/N:" ))
            # IF USER SAY YES SO THIS WILL BE RUN AND ITS ALL COME
            if (enter2_user_input1=="Y"):
                user_ask=int(input("PLEASE ENTER YOUR NUMBER:"))
                if user_ask<number:
                    print("YOU GET AGAIN LESS THEN",number)
                    print("YOU ARE OUT!")
                elif user_ask>number:
                    print("YOU GET AGAIN GREATER THEN:",number)
                    print("YOU ARE OUT!")
                elif user_ask==number:
                    print("YOU WIN WELL DONE:")
                    print("YOUR NUMBER:",user_ask,"\n AND SYSTEM NUMBER:",number)
                    print("BOTH ARE EQUAL")
            elif enter2_user_input1=="N":
                print("OK AS YOU WISH GAME END NOW :")
        elif user_input1==number:
            print("WELL DONE YOU WON THE GAME:")
            print("YOUR NUMBER:",user_input1,"\n AND SYSTEM NUMBER:",number)
            print("BOTH ARE EQUAL")
    elif enter_user1=="N":
        print("AS YOU WISH:")
    # THIS ONE IS WORK WHEN USER FIRST TIME  WRITTEN A LARGE NUMBER
elif input1>number:
    print("YOU GET AGAIN GREATER THEN:",number)
    enter2=str(input("NOW TELL US YOU WANT TO PLAY OR NOT AND THIS IS THE LAST TIME \nIF ANSWER WRONG SO YOU ARE OUT Y/N:"))
    if enter2=="Y":
        enter_input=int(input("ENTER YOUR NUMBER:"))
        if enter_input<number:
            print("YOUR NUMBER LESS THEN:",number)
            enter_ask=str(input("NOW TELL US YOU WANT TO PLAY OR NOT AND THIS IS THE LAST TIME \nIF ANSWER WRONG SO YOU ARE OUT Y/N:"))
            if enter_ask=="Y":
                enter_input=int(input("ENTER YOUR NUMBER:"))
                if enter_input<number:
                     print("YOU GET AGAIN LESS THEN",number)
                     print("YOU ARE OUT!")
                elif enter_input>number:
                     print("YOU GET GREATER THEN",number)
                     print("YOU ARE OUT!")
                elif enter_input==number:
                    print("YOU WIN WELL DONE:")
            elif enter_ask=="N":
                print("OK AS YOU WISH GAME END NOW :")
        # SECOND CONDITION START HERE
        elif enter_input>number:
            print("YOUR NUMBER GREATER THEN :",number)
            enter_last=str(input("NOW TELL US YOU WANT TO PLAY OR NOT AND THIS IS THE LAST TIME \nIF ANSWER WRONG SO YOU ARE OUT Y/N:"))
            if enter_last=="Y"or enter_last=="y":
                int_input=int(input("ENTER YOUR NUMBER:"))
                if int_input<number:
                    print("YOU GET GREATER THEN",number)
                    print("YOU ARE OUT!")  
                elif int_input>number:
                    print("YOU GET GREATER THEN",number)
                    print("YOU ARE OUT!")
                elif int_input==number:
                    print("WELL DONE YOU WON THE GAME:")
            elif enter_last=="N":
                print("OK AS YOU WISH:")
        elif enter_input==number:
            print("WELL DONE YOU WON THE GAME:")
elif input1==number:
    print("WELL DONE YOU WON THE AT FIRST TIME:")
