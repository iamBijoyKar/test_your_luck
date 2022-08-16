from random import randint
<<<<<<< HEAD
score=open('score.txt','a+')
total_point,upper_limit,lose,level,chance=0,5,False,1,5
while True:
    print('You want to store your name and score :(y/n)')
    save_score=False
    ch=input()
    if(ch=='y' or ch=='Y'):
        save_score=True
    print(f"Guess The Number Between 1 and {upper_limit} , You Have {chance} Chances")
=======
from rich.console import Console
from rich.progress import track
from rich.text import Text
import time
console=Console()
total_point,upper_limit,lose,level,chance=0,5,False,1,5
while True:
    console.print(f"Guess The Number Between 1 and {upper_limit} , You Have {chance} Chances",style='bold yellow italic')
>>>>>>> f30fefd1505540c65743fcec658af73a8c20560d
    wrong_answer_count,level_point=0,0
    while(True):
        if(wrong_answer_count>=chance):
            lose=True
            break
        console.print('Guess Your Number :',style='bold magenta',end="")
        guess_number=input()
        rand_val=randint(1,upper_limit)
        with console.status ("[bold green]Generatin...") as status:
            for i in range(1,11):
                time.sleep(.1)
        
        console.print(f'Random Generated Value is {rand_val}',style='bold green ')
        time.sleep(.5)

        if(str(rand_val) == guess_number):
            level_point+=100
            total_point+=level_point
            console.print(f' ** You Won ** \n Level {level} Completed',style='blink blue')
            time.sleep(.5)

            console.print(f'Total Point is {total_point} and Level Point is {level_point}',style='yellow bold')
            time.sleep(.5)
            level+=1
            console.print(f' Advance to Level {level}',style='green italic')
            time.sleep(.5)

            break
        else:
            wrong_answer_count+=1
            level_point-=10
    if(lose):
        time.sleep(.5)
        console.print(f'  -- You Lose -- \n Total Point is {total_point} and Level Point is {level_point}',style='red on black bold')
        break
    upper_limit+=5
    chance+=1