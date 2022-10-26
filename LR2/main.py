import csv
import os
from time import sleep

def esc(code):
    return f"\u001b[{code}m"

GREEN = esc(42)
RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
PURPLE = esc(45)
BLACK = esc(48)
END = esc(0)

print(PURPLE + "Task-1" + END)


def draw_flag():
    for i in range(1):
        print(f'{GREEN}{"   " * 9}{END}')
    for i in range(1,8, 2):
        print(f'{GREEN}{"   " * ((9-i)//2)}{RED}{"   " * i + GREEN}{"   " * ((10-i)//2)}{END}')
    for i in range(7,0, -2):
        print(f'{GREEN}{"   " * ((9-i)//2)}{RED}{"   " * i + GREEN}{"   " * ((10-i)//2)}{END}')
    for i in range(1):
        print(f'{GREEN}{"   " * 9 + END}')

draw_flag()

print("\n")
print(PURPLE + "Task-2" + END)
print("\n")

def draw_pattern():
    for k in range(1):
        print((RED + '  ' * (5) + WHITE + '  ' * (3) + END))
        print((RED + '  ' * (1) + WHITE + '  ' * (3) + RED + '  ' * (1) + WHITE + '  ' * (3) + END))
        print((RED + '  ' * (1) + WHITE + '  ' * (1) + RED + '  ' * (3) + WHITE + '  ' * (3) + END))
        print((RED + '  ' * (1) + WHITE + '  ' * (1) + RED + '  ' * (1) + WHITE + '  ' * (5) + END))
        print((RED + '  ' * (1) + WHITE + '  ' * (1) + RED + '  ' * (6) + END))
        
draw_pattern()

print("\n")
print(PURPLE + "Task-3" + END)
print("\n")

def draw_function_graph():
    print("19" +  BLACK + '  '*7 + WHITE + ' '*1 + END)
    print("17" +  BLACK + '  '*6 + WHITE + ' '*1 + END)
    print("15" +  BLACK + '  '*5 + WHITE + ' '*1 + END)
    print("13" +  BLACK + '  '*4 + WHITE + ' '*1 + END)
    print("11" +  BLACK + '  '*3 + WHITE + ' '*1 + END)
    print(" 9" +  BLACK + '  '*2 + WHITE + ' '*1 + END)
    print(" 7" +  BLACK + '  '*1 + WHITE + ' '*1 + END)
    print(" 5" +  WHITE + ' '*1 + END)
    print(" 3" )
    print(" 1")
    print("  1 2 3 4 5 6 7 8 9")

draw_function_graph()

print("\n")
print(PURPLE + "Task-4" + END)
print("\n")

def draw_diagram():
    befor_2015_year = 0
    after_2015_year = 0
    start_row = 0
    with open('books.csv', 'r', encoding='cp1251') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        for row in table:
            if start_row != 0:
                if row[6][6:10] < '2015':
                    befor_2015_year += 1
                else:
                    after_2015_year += 1
            start_row += 1
            
    percent_books_befor_2015 = int((befor_2015_year/(befor_2015_year+after_2015_year))*100)
    percent_books_after_2015 = 100 - percent_books_befor_2015
    print(f'books published before 2015 year     {WHITE}{"  " * percent_books_befor_2015}{END}{percent_books_befor_2015}%')
    print(f'books published after 2015 year      {RED}{"  " * percent_books_after_2015}{END}{"  " *(percent_books_befor_2015-percent_books_after_2015)}{percent_books_after_2015}%')

draw_diagram()

print("\n")
print(PURPLE + "Additional task" + END)
print("\n")

def draw_animation():
    time_sleep = 0.8
    for j in range(10):
        
        os.system('cls')
        print(WHITE + '  ' * 7 + END)
        sleep(time_sleep)
        os.system('cls')
        print("\n" + RED + '  ' * 7 +END)
        sleep(time_sleep)

play_animation = input("play animation? Input: y/n\n")
if(play_animation == "y"):
    draw_animation()
