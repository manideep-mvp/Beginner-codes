import random
import datetime
random_int = random.randint(1,10)
d = datetime.datetime.now()
count = 1
def main():


    def success():
   
        print("Congrats!!! You guessed the correct number")

    
    def high():
        global count
        m=1
        while m>0:
                print("Your number is higher than the intended value, enter a lower number")
                while True:
                    v1 = input("Please enter your guess: ")
                    count = count+1
                    try:
                        lowval = int(v1)
                    except ValueError:
                        print("Please enter a number")
                    else:
                        if lowval in range(1,11):
                            break
                        else:
                            print("Number not in range. Please try again")
                c = lowval
                if random_int-c>0:
                    low()
                    break
                elif random_int-c==0:
                    success()
                    gen()
                    print("You took " + str(count)+ " guesses to win the game")
                    break
                else:
                    m=+1
            
                
    def low():
        global count
        i=1
        while i>0:
            print("Your number is lower than the intended value, enter a higher number")
            while True:
                    v2 = input("Please enter your guess: ")
                    count = count+1
                    try:
                        highval = int(v2)
                    except ValueError:
                        print("Please enter a number")
                    else:
                        if highval in range(1,11):
                            break
                        else:
                            print("Number not in range. Please try again")
            b = highval
            if random_int-b<0: 
               high()
               break
            elif random_int-b==0:
                success()
                gen()
                print("You took " + str(count)+ " guesses to win the game")
                break
            else:
                i+=1

            
    def gen():
        print("The random number generated was "+str(random_int))
    
    def process():
        if random_int-a>0:
            low()
        elif random_int-a<0:   
            high()           
        elif random_int-a==0:
            success()
            gen()
            print("you won the game in the first try!")

    print(d.strftime("%A")+ "," + d.strftime("%B") +" "+ d.strftime("%d") +" "+ d.strftime("%Y")+ "     " + d.strftime("%I") +":"+ d.strftime("%M") +" "+ d.strftime("%p"))    
    print("Welcome to the guessing game")
    while True:
        num = input("Please enter a number between 1 and 10:")
        try:
            number = int(num)
        except ValueError:
            print("Please enter a number")
        else:
            if number in range(1,11):
                break
            else:
                print("Number not in range. Please try again")          
    a = int(num)
    process()
main()
g=1
while g>0:
    print("Do you wanna play again?")
    print("Please enter Y or N")
    new = str(input())
    if new =="Y":
       count = 1
       random_int = random.randint(1,10)
       main() 
    elif new == "N":
        break
    else:
        print("please enter a valid answer")
        g+=1
    



