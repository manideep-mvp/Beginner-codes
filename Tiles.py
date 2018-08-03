import datetime
d = datetime.datetime.now()
print(d.strftime("%A")+ "," + d.strftime("%B") +" "+ d.strftime("%d") +" "+ d.strftime("%Y")+ "     " + d.strftime("%I") +":"+ d.strftime("%M") +" "+ d.strftime("%p"))    

""" displays current date and time """
def solve():
        tile_length = 12
        tile_breadth = 12
        num_tiles_perbox = 12
        tile_area = (tile_length*tile_breadth)*(0.006945)    #converting square inches to square feet
        num_tiles = customer_floor_area/tile_area
        num_tiles_final = int(num_tiles)+(customer_floor_area%tile_area>0)
        num_boxes = num_tiles_final/num_tiles_perbox
        final_boxes = int(num_boxes)+(num_tiles_final%num_tiles_perbox>0)
        print("You need "+str(num_tiles_final)+" tiles for your floor")
        print("You need "+str(final_boxes)+" boxes ")
        
def room_length(): 
    while True:
        global var_room_length
        global length_inches
        length_inches=0
        i=1
        while i>0:
            input1 = input("Please enter length of the room in feet or inches: ")
            print("The length you entered is in feet units? press 'y' for yes, 'n' for no")
            conf = input()
            if conf=="y":
                break
            elif conf == "n":
                length_inches = input1
                break
            else:
                i+=1
                
        try:
            var_room_length = float(input1)
        except ValueError:
            print("Please enter a valid number")
        else:
            if var_room_length in range(1,9999999): #gets out of the loop when user inputs valid number
                break
            else:
                print("Please enter a valid number")
def room_width():
    while True:
        global var_room_width
        global width_inches
        width_inches=0
        j=1
        while j>0:
            input2 = input("Please enter width of the room in feet or inches: ")
            print("Please confirm that width is in feet. press 'y' for yes 'n' for no")
            conf3 = input()
            if conf3=="y":
                break
            elif conf3 =="n":
                width_inches = input2
                break
            else:
                j+=1
        
        try:
            var_room_width = float(input2)
        except ValueError:
            print("Please enter a valid number")
        else:
            if var_room_width in range(1,9999999): #gets out of the loop when user inputs valid number
                break
            else:
                print("Please enter a valid number")
def room_area():
    global var_room_area
    global customer_floor_area
    room_length()
    room_width()
    if length_inches==0 and width_inches == 0:
        var_room_area = var_room_length*var_room_width
    elif length_inches!=0 and width_inches !=0:
        var_room_area = var_room_length*var_room_width*0.084*0.084
    else:
        var_room_area = var_room_length*var_room_width*0.084
    customer_floor_area = float(var_room_area)
    
print("please enter the room specifications.")

room_area()
solve()



