import random
def three_empty_stacks():
    three_empty_stacks.one=[]
    three_empty_stacks.one_size=3
    three_empty_stacks.two=[]
    three_empty_stacks.two_size=2
    three_empty_stacks.three=[]
    three_empty_stacks.three_size=3
def three_stacks_with_random_numbers():
    list1=[1,2,3,4,5]
    for i in range(three_empty_stacks.one_size):
        num=random.randint(1,5)
        if num not in three_empty_stacks.one: 
           three_empty_stacks.one.append(num) 
           list1.remove(num)      
    if len(three_empty_stacks.one)!=three_empty_stacks.one_size:
        emp1=three_empty_stacks.one_size-len(three_empty_stacks.one)
        for g in range(emp1):
            three_empty_stacks.one.append(" ")
    for j in range(three_empty_stacks.two_size):        
        num2=random.randint(1,5)
        if num2 not in three_empty_stacks.one and num2 not in three_empty_stacks.two:
            three_empty_stacks.two.append(num2)   
            list1.remove(num2)                   
    if len(three_empty_stacks.two)!=three_empty_stacks.two_size:
        emp2=three_empty_stacks.two_size-len(three_empty_stacks.two)
        for g in range(emp2):
            three_empty_stacks.two.append(" ")
    for k in range(len(list1)):                 
            three_empty_stacks.three.append(list1[k])                
    if len(three_empty_stacks.three)!=three_empty_stacks.three_size:
        emp3=three_empty_stacks.three_size-len(three_empty_stacks.three)
        for g in range(emp3):
            three_empty_stacks.three.append(" ")
def three_empty_stacks_player():
    three_empty_stacks_player.one=[]
    three_empty_stacks_player.one_size=3
    three_empty_stacks_player.two=[]
    three_empty_stacks_player.two_size=2
    three_empty_stacks_player.three=[]
    three_empty_stacks_player.three_size=3
def three_stacks_with_random_numbers_player():
    list2=[1,2,3,4,5]
    for i in range(three_empty_stacks_player.one_size):
        numm=random.randint(1,5)     
        if numm not in three_empty_stacks_player.one:
           three_empty_stacks_player.one.append(numm)
        if numm in list2:
            list2.remove(numm)             
    if len(three_empty_stacks_player.one)!=three_empty_stacks_player.one_size:
        empp1=three_empty_stacks_player.one_size-len(three_empty_stacks_player.one)
        for g in range(empp1):
            three_empty_stacks_player.one.append(" ")
    for j in range(three_empty_stacks_player.two_size):        
        numm2=random.randint(1,5)
        if numm2 not in three_empty_stacks_player.one and numm2 not in three_empty_stacks_player.two:
            three_empty_stacks_player.two.append(numm2) 
            if numm2 in list2:
                list2.remove(numm2)                   
    if len(three_empty_stacks_player.two)!=three_empty_stacks_player.two_size:
        empp2=three_empty_stacks_player.two_size-len(three_empty_stacks_player.two)
        for h in range(empp2):
            three_empty_stacks_player.two.append(" ")
    for k in range(len(list2)):                 
            three_empty_stacks_player.three.append(list2[k])        
    if len(three_empty_stacks_player.three)!=three_empty_stacks_player.three_size:
        emp3=three_empty_stacks_player.three_size-len(three_empty_stacks_player.three)
        for k in range(emp3):
            three_empty_stacks_player.three.append(" ")
def print_random():
    for i in range(3-1, -1, -1):
        elem1 = str(three_empty_stacks.one[i]) if i < len(three_empty_stacks.one) else ''
        elem2 = str(three_empty_stacks.two[i]) if i < len(three_empty_stacks.two) else ''
        elem3 = str(three_empty_stacks.three[i]) if i < len(three_empty_stacks.three) else ''
        if i!=2:
            print("\t\t\t\t\t\t\t\t",f'|_{elem1}_|', f'|_{elem2}_|', f'|_{elem3}_|')
        else:
            print("\t\t\t\t\t\t\t\t",f'|_{elem1}_|', '     ', f'|_{elem3}_|')
def print_player():
    for i in range(3-1, -1, -1):
        elem1 = str(three_empty_stacks_player.one[i]) if i < len(three_empty_stacks_player.one) else ''
        elem2 = str(three_empty_stacks_player.two[i]) if i < len(three_empty_stacks_player.two) else ''
        elem3 = str(three_empty_stacks_player.three[i]) if i < len(three_empty_stacks_player.three) else ''
        if i!=2:
            print("\t\t\t\t\t\t\t\t",f'|_{elem1}_|', f'|_{elem2}_|', f'|_{elem3}_|')
        else:
            print("\t\t\t\t\t\t\t\t",f'|_{elem1}_|', '     ', f'|_{elem3}_|')
def moving():
    match=False
    while match==False:
        select_stack=int(input("SELECT THE STACK :\n1.FIRST STACK\n2.SECOND STACK\n3.THIRD STACK\n:"))
        if select_stack==1:
            if len(three_empty_stacks_player.one)!=0:
                pop_element=0
                for i in range(len(three_empty_stacks_player.one)-1, -1, -1):
                    if isinstance(three_empty_stacks_player.one[i], int):
                        pop_element=three_empty_stacks_player.one.pop(i)
                        three_empty_stacks_player.one.insert(i," ")
                    
                        break
                move=int(input(f"Enter where do you want to move {pop_element}:\n1.SECOND STACK\n2.THIRD STACK\n:"))
                if move==1:
                    if " " in three_empty_stacks_player.two:
                        index=three_empty_stacks_player.two.index(" ")
                        three_empty_stacks_player.two[index]=pop_element
                    else:
                        print("SECOND STACK IS FULL")
                elif move==2:
                    if " " in three_empty_stacks_player.three:
                        index=three_empty_stacks_player.three.index(" ")
                        three_empty_stacks_player.three[index]=pop_element
                    else:
                        print("THIRD STACK IS FULL")
        elif select_stack==2:
            if len(three_empty_stacks_player.two)!=0:
                pop_element=0
                for i in range(len(three_empty_stacks_player.two)-1, -1, -1):
                    if isinstance(three_empty_stacks_player.two[i], int):
                        pop_element=three_empty_stacks_player.two.pop(i)
                        three_empty_stacks_player.two.insert(i," ")
                        break
                move=int(input(f"Enter where do you want to move {pop_element}:\n1.FIRST STACK\n2.THIRD STACK\n:"))
                if move==1:
                    if " " in three_empty_stacks_player.one:
                        index=three_empty_stacks_player.one.index(" ")
                        three_empty_stacks_player.one[index]=pop_element
                    else:
                        print("FIRST STACK IS FULL")
                elif move==2:
                    if " " in three_empty_stacks_player.three:
                        index=three_empty_stacks_player.three.index(" ")
                        three_empty_stacks_player.three[index]=pop_element
                    else:
                        print("THIRD STACK IS FULL")
        elif select_stack==3:
            if len(three_empty_stacks_player.three)!=0:
                pop_element=0
                for i in range(len(three_empty_stacks_player.three)-1, -1, -1):
                    if isinstance(three_empty_stacks_player.three[i], int):
                        pop_element=three_empty_stacks_player.three.pop(i)
                        three_empty_stacks_player.three.insert(i," ")
                        break
                move=int(input(f"Enter where do you want to move {pop_element}:\n1.FIRST STACK\n2.SECOND STACK\n:"))
                if move==1:
                    if " " in three_empty_stacks_player.one:
                        index=three_empty_stacks_player.one.index(" ")
                        three_empty_stacks_player.one[index]=pop_element
                    else:
                        print("FIRST STACK IS FULL")
                elif move==2:
                    if " " in three_empty_stacks_player.two:
                        index=three_empty_stacks_player.two.index(" ")
                        three_empty_stacks_player.two[index]=pop_element
                    else:
                        print("SECOND STACK IS FULL")
        print_random()
        print("\n")
        print_player()
        if three_empty_stacks.one==three_empty_stacks_player.one and three_empty_stacks.two==three_empty_stacks_player.two and three_empty_stacks.three==three_empty_stacks_player.three:
            print("YOU WIN!!!!")
            match=True 
print("-------------------------------------------------------------WELCOME TO SORTING GAME---------------------------------------------------------")       
three_empty_stacks()
three_stacks_with_random_numbers()
print("\n")
three_empty_stacks_player()
three_stacks_with_random_numbers_player()
print("-----------------------------------------------------------------YOUR OBECTIVE---------------------------------------------------------------")
print("\n")
print_random()
print("\n")
print("----------------------------------------------------------------YOUR PLAY FIELD--------------------------------------------------------------")
print("\n")
print_player()
print("\n")
moving()

    

            


    




