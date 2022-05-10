from pygame import * 
import os
import pygame

#moving screen to top left corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 20)
init()

# screen size and display
size = width, height = 1000, 600
screen = display.set_mode(size)

# Colours
BLACK = (0, 0, 0)
GREY = (192,192,192)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (51,25,0)
PALEYELLOW = (255,255,153)
DEEPBLUE = (0,0,102)
PURPLE = (153,153,255)

#fonts
Roman = font.SysFont("Times New Roman",60)
Heading = font.SysFont("Times New Roman",25)
writing = font.SysFont("Times New Roman",20)
impact = font.SysFont("Impact",100)
impacter = font.SysFont("Impact",50)

#images
    #load first room background
office = image.load ("officeroom.png")
    #scaling the image to fit the screen
office = transform.scale (office,[1000,600])
    #load aquarium image
aqua = image.load ("water.jpg")
aqua = transform.scale (aqua,[800,500])
    #load fish background
fish = image.load ("MahamFish.png")
fish = transform.scale (fish,[300,200])
    #load crowbar image
crowbar = image.load ("MahamCrowbar.png")
crowbar = transform.scale (crowbar,[250,150])
    #load first book about battery image
battery = image.load ("sonicBattery.png")
battery = transform.scale (battery, [250,300])
    #load second book
book2 = image.load ("Mahambook2.jpg")
book2 = transform.scale (book2, [275,400])
    # load second book
book3 = image.load ("Mahambook3.jpg")
book3 = transform.scale (book3, [250,350])
    # load fish food
food = image.load ("fishFood.png")
food = transform.scale (food, [45,35])
    # load e-waste image on the wall that is covering painting
waste = image.load ("MahamE-waste.jpg")
waste = transform.scale (waste, [1000,625])
    # load e-waste fact on large
stat = image.load ("MahamStat.jpg")
stat = transform.scale (stat, [800,500])
    # load e-waste fact on large
stats = image.load ("MahamStat.jpg")
stats = transform.scale (stat, [125,100])
    # load panasonic factory
factory = image.load ("factory.png")
factory = transform.scale (factory, [1000,800])
    # load fumes image
fumes = image.load ("fumes.jpg")
fumes = transform.scale (fumes, [1000,600])

# define states
STATEMENU = 0
STATEOFFICE = 1
STATEQUIT = 2
STATEINSTRUCT = 3
STATEOVER = 4
 
# VR - set to starting at a 0 for substates, not using the same values
SUBSTATENONE = 0 
SUBSTATEOPENDRAWER = 1
SUBSTATERIUM = 2
SUBSTATESHELF = 3
SUBSTATEDOORLOCK = 4
SUBSTATEDOORUNLOCK = 5
SUBSTATEFISHDRAWER = 6
SUBSTATEFISHBAR = 7
SUBSTATEFRAME = 8

# state of the fish
SUBSTATEFISHSTOP = 0
SUBSTATEFISHY = 1

# the original states of the major, sub and fish states
state = STATEMENU
subState = SUBSTATENONE
subFish = SUBSTATEFISHSTOP

myClock = time.Clock()
cx = 0 # for my game
timed = 6000 # when the timer starts

count = [0,0,0,0] # for first number of code of the drawer
codeDrawer = [220,365,510,655] # these are where each x-position square starts 

counter = [0,0,0] # for first number of code of the door
codeDoor = [300,450,600] # these are where each x-position square starts

opener = 1   # the variable that determines draws whether the drawer is locked or not
keyDoor = 1  # the variable that determines draws whether the door is locked or not
changer = False  # the variable that determines draws whether the user has the bar or not 

correct = False  # Boolean determining the writing that states if code is correct to the user
fishy = False    # Boolean that aids in determining if fish has moved or not
bar = False      # Boolean that aids in determining whether user can get the bar

fishPosX = 450  # x cooridinates of fish
fishPosY = 360  # Y coordinates of fish

buttonList = [Rect(370,350,80,70)]



#draws the menu page, game page, and everything within
def drawScene(screen, curState,subState, circlex,correct,changer):
    # what is drawn within the menu page
    if curState == STATEMENU:
        screen.fill (BLACK)
        screen.blit (waste, Rect (0,-25,1000,600))
         #PLAY button
        draw.rect (screen, DEEPBLUE, (250,150,450,75))
            # Setting up the PLAY Text
        text1 = Roman.render("PLAY", 1, WHITE) 
            # getting the width of the text
        text1Width = Roman.size("PLAY")[0] 
            # getting the height of the text
        text1Height = Roman.size("PLAY")[1] 
            # blitting "PLAY" to the screen
        screen.blit(text1, Rect(175 + (600 - text1Width)/2, 150 + (80 - text1Height)/2, text1Width, text1Height)) 
        
        #Instructions Button
        draw.rect (screen, DEEPBLUE, (250,275,450,75))
            # Setting up the Instructions Text
        text1 = Roman.render("INSTRUCTIONS", 1, WHITE) 
            # getting the width of the text
        text1Width = Roman.size("INSRTUCTIONS")[0]
            # getting the height of the text
        text1Height = Roman.size("INSTRUCTIONS")[1] 
            # blitting "INSTRUCTIONS" to the screen
        screen.blit(text1, Rect(175 + (600 - text1Width)/2, 275 + (80 - text1Height)/2, text1Width, text1Height))
        
        #Quit Button
        draw.rect (screen, DEEPBLUE, (250,400,450,75))
            # Setting up the QUIT Text
        text1 = Roman.render("QUIT", 1, WHITE) 
            # getting the width of the text
        text1Width = Roman.size("QUIT")[0] 
            # getting the height of the text
        text1Height = Roman.size("Quit")[1] 
            # blitting "Quit" to the screen
        screen.blit(text1, Rect(175 + (600 - text1Width)/2, 400 + (80 - text1Height)/2, text1Width, text1Height))
        # Setting up the Play Game Text
        text1 = Roman.render("PLAY GAME", 1, RED)
        text1Width = Roman.size("PLAY GAME")[0]  # getting the width of the text
        text1Height = Roman.size("PLAY GAME")[1] # getting the height of the text

    # the instructinos to the game
    elif state == STATEINSTRUCT:
        screen.fill (PALEYELLOW)
            # back button to menu page
        draw.rect (screen, WHITE, (25,25,125,75))
        text1 = Roman.render ("Back", 1,BLACK)
        screen.blit (text1, (25,25))        
        
        #Writing out the plotline of the game
        draw.rect (screen,PURPLE, Rect (75,100,375,425))
        text1 = Heading.render ("Game Plot",1,BLACK)
        text2 = writing.render ("You (an employee) are trapped in a ",1,BLACK) 
        text3 = writing.render ("battery factory. Something malfunctioned",1,BLACK)
        text4 = writing.render ("and the air is becoming polluted causing",1,BLACK)
        text5 = writing.render ("the factory to go into lock-down mode in",1,BLACK)
        text6 = writing.render ("order to prevent any toxic fumes from",1,BLACK)
        text7 = writing.render ("escaping the facility. However in case of",1,BLACK)
        text8 = writing.render ("an emergency, employees can still escape",1,BLACK)
        text9 = writing.render ("if they figure out the passcode to the door.",1,BLACK) 
        #blitting the text Game Plot 
        screen.blit (text1, (190,115))
        screen.blit (text2, (100,160))
        screen.blit (text3, (100,185))
        screen.blit (text4, (100,210))
        screen.blit (text5, (100,235))
        screen.blit (text6, (100,260))
        screen.blit (text7, (100,285))
        screen.blit (text8, (100,310))
        screen.blit (text9, (100,335))
        
        # writing how to play this game. 
        draw.rect (screen,PURPLE,(550,100,375,425))
        text1 = Heading.render ("How To Play",1,BLACK)
        text2 = writing.render ("The Objective of the game is to escape the",1,BLACK) 
        text3 = writing.render ("toxic factory before the timer runs out.",1,BLACK)
        text4 = writing.render ("Click around the room for certain aspects",1,BLACK)
        text5 = writing.render ("of the room to enlarge so it can be used ",1,BLACK)
        text6 = writing.render ("for your escape. Once enlarged, in order  ",1,BLACK)
        text7 = writing.render ("to go back to the room, click the right ",1,BLACK)
        text8 = writing.render ("hand side of the mouse. If a passcode iS ",1,BLACK)
        text9 = writing.render ("figured out, you will be prompted and  ",1,BLACK)
        text10 = writing.render ("click the right side of the mouse to go ",1,BLACK)
        text11 = writing.render ("back. Good Luck!",1,BLACK)
        # blitting the text how to play
        screen.blit (text1, (665,115))
        screen.blit (text2, (575,160))
        screen.blit (text3, (575,185))
        screen.blit (text4, (575,210))
        screen.blit (text5, (575,235))
        screen.blit (text6, (575,260))
        screen.blit (text7, (575,285))
        screen.blit (text8, (575,310))
        screen.blit (text9, (575,335))
        screen.blit (text10, (575,360))
        screen.blit (text11, (575,385))   
        
    # if the timer hits 0 before user figures it out, "game over"
    elif state == STATEOVER:
        screen.blit (fumes, Rect (0,0,1000,800))
            # GAME OVER TEXT
        text1 = impact.render("GAME OVER", 1, WHITE)
        screen.blit(text1, (275,250))
        text2 = impacter.render ("You were intoxicated by the gas!",1,BLACK)
        screen.blit (text2, (175,25))
    # if the user click the play button, an image of an office shows up
    elif state == STATEOFFICE:
        screen.blit (office, Rect (0,0,1000,700))  
        #this changes depending on whether or not the user has the bar or not
        if changer == False:
            draw.rect (screen, BROWN, (330,95,125,100))
        if changer == True:
            # the pic is a state about e-waste and the bolded 3 numbers in the middle are the code
            screen.blit (stats, Rect (330,95,125,100))
            
       # draws the scene for a locked drawer
        if subState == SUBSTATEOPENDRAWER:
             #if the user has not figured out the code yet, they can go back and forth to the locked drawer
            if opener == 1:
                draw.rect (screen,BROWN, (100,100,800,500))
                draw.rect (screen,BLACK, (200,150,600,150))
                
                # the squares for the code
                draw.rect (screen,GREY, (220,175,125,100))
                draw.rect (screen,GREY, (365,175,125,100))
                draw.rect (screen,GREY, (510,175,125,100))
                draw.rect (screen,GREY, (655,175,125,100))
                
                # the number
                text1 = Roman.render (str(count[0]),3,BLACK)
                screen.blit (text1, (265,190))
                text2 = Roman.render (str(count[1]),3,BLACK)
                screen.blit (text2, (410,190))
                text3 = Roman.render (str(count[2]),3,BLACK)
                screen.blit (text3, (555,190))
                text4 = Roman.render (str(count[3]),3,BLACK)
                screen.blit (text4, (700,190))
                
                # if the user finds the correct passcode, message will show up
                if correct == True:
                    text5 = Roman.render ("YOU UNLOCKED THE DRAWER!",1,BLACK)
                    screen.blit (text5,(45,400))
             # if the user figures out the password, the drawer will now show the state showing the fish food
            elif opener == 2:
                draw.rect (screen,BLACK, (370,350,80,70))
                screen.blit (food, Rect (390,375,40,35))
            # if the user clicks on the password, the drawer will show an empty drawer
            elif opener == 3:
                draw.rect (screen,BLACK, (370,350,80,70))
            
        # draws scene for aquirium
        elif subState == SUBSTATERIUM:
            draw.rect (screen,BLACK, (100,100,800,500),10)
            screen.blit (aqua, Rect (100,100,800,500))
            screen.blit (crowbar, Rect (450,360,400,200))
            screen.blit (fish, Rect (fishPosX,fishPosY,300,200))
            
        # draws this scene for when the user clicks on the crowbar AFTER the fish has moved out of the way
        elif subState == SUBSTATEFISHBAR: 
            draw.rect (screen,BLACK, (100,100,800,500),10)
            screen.blit (aqua, Rect (100,100,800,500))            
            screen.blit (fish, Rect (fishPosX,fishPosY,300,200))
            
        # draws scene for the book shelf
        elif subState == SUBSTATESHELF:
            draw.rect (screen,BROWN,(150,500,700, 50))
            
            # blitting the three images that determine the passcode
            screen.blit (book2, Rect (325,120,100,300))
            screen.blit (battery, Rect (115,250,250,100))
            draw.rect (screen,BLACK, (295,415,50,25)) 
            screen.blit (book3, Rect (590,170,100,300))
            
        # draws scene for the locked door
        elif subState == SUBSTATEDOORLOCK:
            draw.polygon (screen, BROWN, [(500,25),(100,300),(500,575),(900,300)])
            
            # draws squares where numbers are supposed to go
            draw.rect (screen,BLACK, (275,200,475,140))
            draw.rect (screen,GREY, (300,220,125,100))
            draw.rect (screen,GREY, (450,220,125,100))
            draw.rect (screen,GREY, (600,220,125,100))
            
            #blitting numbers
            text1 = Roman.render (str(counter[0]),3,BLACK)
            screen.blit (text1, (350,240))
            text2 = Roman.render (str(counter[1]),3,BLACK)
            screen.blit (text2, (500,240))
            text3 = Roman.render (str(counter[2]),3,BLACK)
            screen.blit (text3, (650,240))  
        
        # draws scene of what happens when the door unlocks    
        elif subState == SUBSTATEDOORUNLOCK:
            screen.blit (factory,(0,-50,900,600))
            text3 = impact.render ("YOU ESCAPED!",1,BLACK)
            screen.blit (text3, (250,240))
        
        # draws scene of painting on the wall
        elif subState == SUBSTATEFRAME:
            # if the user has found the bar, blits statistics
            if changer == False:
                draw.rect (screen, BROWN, (100,100,800,500))
                text1 = Heading.render ("There must be something behind here to help unlock the door and get out.",1,BLACK)
                screen.blit (text1,(75,25))
            elif changer == True:
                # the pic is a state about e-waste and the bolded 3 numbers in the middle are the code
                screen.blit (stat, Rect (100,100,800,500))                
    display.flip()

# within some major states, there are substates that occur in order to play the game     
def changeSubState(but, mousex, mousey, curState,curSubState):
    global fishy, fishPosX,changer,opener
    if but == 1:
        
        # VR - modified to make sure we have no chosen substate yet
        if state == STATEOFFICE and subState == SUBSTATENONE:
            if 330 <= mousex <= 455:
                if 95 <= mousey <= 195:
                    curSubState = SUBSTATEFRAME             
            if 370 <= mousex <= 450:        # x range for drawer
                if 350 <= mousey <= 420:    # y range for drawer
                    if opener == 1:
                        curSubState = SUBSTATEOPENDRAWER
                    elif opener == 2:
                        time.wait (1000)
                        display.flip ()
                        curSubState = SUBSTATEFISHDRAWER 
                    elif opener == 3:
                        draw.rect (screen,BLACK, (370,350,80,70))
                        fishy = True                    
            # the x and y coordinates range in order to click on the aqaurium
            elif 800 <= mousex <= 950:
                if 125 <= mousey <= 225:
                    # if the changer = False, the substate will draw an aquarium with bar
                    if changer == False:
                        curSubState = SUBSTATERIUM
                    # if the changer = True, the substate will draw accordingly
                    elif changer == True: 
                        curSubState = SUBSTATEFISHBAR                            
            # the x and y coordinates range in order to click on the bookshelf
            elif  55 <= mousex <= 145:
                if 185 <= mousey <= 275:
                    curSubState = SUBSTATESHELF 
            # the x and y coordinates range in order to click on the door
            elif 530 <= mousex <= 710:
                if 65 <= mousey <= 475:
                    # if the door is locked the code will appear
                    if keyDoor == 1:
                        curSubState = SUBSTATEDOORLOCK 
                    # if the user finds the password, an unlocked image of the door will appear
                    elif keyDoor == 2:
                        curSubState = SUBSTATEDOORUNLOCK
        # checks if the fish has moved all the way over
        if curSubState == SUBSTATERIUM and fishPosX <= 200:
            curSubState = SUBSTATEFISHBAR
            changer = True
        
            
    return curSubState

# changing the main states through specific ranges
def changeState(but, mousex, mousey, curState,curSubState):
    # timed is a global varibale hence called to the function
    global timed
    # ony occurs if user clicks on the mouse
    if but == 1:
        # if the user is on the menu page
        if curState == STATEMENU:
            if 250 <= mousex <= 750:                    # x range for all boxes
                if 400 <= mousey <= 475:                # quit box - x range
                    curState = STATEQUIT
                elif 275 <= mousey <= 350:              # instructions both - x range
                    curState = STATEINSTRUCT
                elif 150 <= mousey <= 225:
                    curState = STATEOFFICE              # start game box - x range
                    timed = pygame.time.get_ticks()     #calling ticks to start timer
                    
        # if the state is office           
        elif curState == STATEOFFICE:
            curSubState = changeSubState (button, mx, my, curState,curSubState)   
                 
        # if the user clicks on the instructions   
        elif curState == STATEINSTRUCT:
            if 25 <= mousex <= 150:
                if 25 <= mousey <= 100:
                    curState = STATEMENU 

    # in order for the state to go into it's original state (so no state) press the right side of the mouse
    elif but == 3:            
        # if we aren't in SUBSTATENONE - otherwise we set it to None
        if curSubState != SUBSTATENONE:
            curSubState = SUBSTATENONE      
    return curState,curSubState

# function allows the fish to stop or move
def moveFishy (button,mousex,mousey,posx,curFishState,curSubState,fishy,bar):
    # only occurs if the substate is SUBSTATERIUM or SUBSTATEFISHBAR also while bar is False
    if (subState == SUBSTATERIUM or subState == SUBSTATEFISHBAR) and bar == False:
        print ("hi",curFishState)
        if 450 <= mousex <= 850 and 360 <= mousey <= 560:    # x and y range for fish
            print("Right here.")
            if fishy == True:                                # only occurs if they found the passcode for the drawer
                if bar == False:                             # fish moves if the bar is False
                    curFishState = SUBSTATEFISHY
                elif bar == True:                            # fish stops at a certain point where bar then = True
                    curFishState = SUBSTATEFISHSTOP
        
        # if the fish moves, below occurs             
        if curFishState == SUBSTATEFISHY:
            posx -= 5                                        # how much it moves by
            print(posx)
            if posx <= 200:                                  # stops when the fish hits 200 making he bar available for user to take
                curFishState = SUBSTATEFISHSTOP
                bar = True
                
    display.flip ()
    return curFishState,bar,posx

# this function allows the digits of the code to change numbers on the drawer
def ChangeNumber (button, mousex, mousey, curSubState,position,count,lowX,lowY): 
    global opener
    # only occurs while the user is looking at the enlarged image of the drawer
    if curSubState == position:
        # only occurs if mouse is pressed
        if button == 1:
            #checks for the range of the access as well as where the mouse is in relation to it
            for i in range (lowX,(lowX+125)):
                if i <= mousex <= i:
                    if lowY <= mousey <= lowY + 100:  
                        # adds once if following commands are met
                        count += 1   
    # if the user gets to the 10th element, the counter restarts allowing no digits other than single digits
    if count == 10:
        count = 0
        
    display.flip ()
    return count

# Game Loop
# loop occurs while the game is not in STATEQUIT (plays until user quits)
while state != STATEQUIT:
    button = 0
    mx = my = 0
    
    for evnt in event.get():                    # checks all events that happen
        if evnt.type == QUIT:
            state = STATEQUIT
        if evnt.type == MOUSEBUTTONDOWN:        # checks all events that happens with the mouse
            mx, my = evnt.pos          
            button = evnt.button  
            
    # calling the functions to draw the scenes as user clicks specific ranges
    drawScene(screen, state, subState, cx,correct,changer)
    state,subState = changeState(button, mx, my, state,subState) 
    #mouse coordinates to detect fish food
    mouse = [mx,my,1,1]
    
    # adjusting for the timer
    if state == STATEOFFICE and subState != SUBSTATEDOORUNLOCK:
        # makes it countdown
        timer = ((101000 - (pygame.time.get_ticks()-timed))//1000)    
        timeText = Roman.render (str(timer),1,BLACK) 
        screen.blit (timeText, (900,15)) 
        # if the timer hits 0, game over
        if timer <= 0:
            state = STATEOVER        
    
        
    # each code digit for the drawer        
    count[0] = ChangeNumber (button, mx, my,subState,SUBSTATEOPENDRAWER,count[0],codeDrawer[0],175)
    count[1] = ChangeNumber (button, mx, my,subState,SUBSTATEOPENDRAWER,count[1],codeDrawer[1],175)
    count[2] = ChangeNumber (button, mx, my,subState,SUBSTATEOPENDRAWER,count[2],codeDrawer[2],175)
    count[3] = ChangeNumber (button, mx, my,subState,SUBSTATEOPENDRAWER,count[3],codeDrawer[3],175)
    
    # each code digit for the locked door
    counter[0] = ChangeNumber (button, mx, my,subState,SUBSTATEDOORLOCK,counter[0],codeDoor[0],220)
    counter[1] = ChangeNumber (button, mx, my,subState,SUBSTATEDOORLOCK,counter[1],codeDoor[1],220)
    counter[2] = ChangeNumber (button, mx, my,subState,SUBSTATEDOORLOCK,counter[2],codeDoor[2],220)
    
    # calling the fish to move
    subFish,bar, fishPosX = moveFishy (button,mx,my,fishPosX,subFish,subState,fishy,bar)    
    
    # for my game
    if state == STATEOFFICE:
        cx += 1
     
    # checks to see if the user has the correct passcode for the drawer
    # once figured out, access to drawer can be given and fish will be able to move
    if count == [2,4,6,3]:      
        if opener == 1:
            opener = 2 
            correct = True
        elif buttonList[0].colliderect (mouse):
            fishy = True     
            opener = 3
        elif opener == 3:
            opener = 3
    # if the user is incorrect or is still finding the code, everything is false
    elif count != [2,4,6,3]:
        opener = 1
        correct = False    
    
    # allows for detection of fish food
    if opener == 2:
        if buttonList[0].colliderect (mouse):
            fishy = True     
            opener = 3     
    
    # check for door passcode         
    if counter == [4,4,7]:
        subState = SUBSTATEDOORUNLOCK
    elif counter != [4,4,7]:
        keyDoor = 1    
        
    display.flip ()
    print(state,subState,count,counter,fishy,bar,fishPosX,changer,opener)