from random import randint
total_point,upper_limit,lose,level,chance=0,5,False,1,5
while True:
    print(f"Guess The Number Between 1 and {upper_limit} , You Have {chance} Chances")
    wrong_answer_count,level_point=0,0
    while(True):
        if(wrong_answer_count>=chance):
            lose=True
            break
        guess_number=int(input('Guess Your Number :'))
        rand_val=randint(1,upper_limit)
        print(f'Random Generated Value is {rand_val}')
        if(rand_val == guess_number):
            level_point+=100
            total_point+=level_point
            print(f' ** You Won ** \n Level {level} Completed')
            print(f'Total Point is {total_point} and Level Point is {level_point}')
            level+=1
            print(f' Advance to Level {level}')
            break
        else:
            wrong_answer_count+=1
            level_point-=10
    if(lose):
        print(f'  -- You Lose -- \n Total Point is {total_point} and Level Point is {level_point}')
        break
    upper_limit+=5
    chance+=1