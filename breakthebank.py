#--------------------------------------------------------
# Import and initialize the pygame library
#--------------------------------------------------------
import pygame, os, random
pygame.init()
pygame.mixer.init()

#--------------------------------------------------------
# Check if the images are loaded
#--------------------------------------------------------
if not os.path.exists("imgs"):
    print("you do not have imgs folder")

#--------------------------------------------------------
# Sets the bar icon and text for game window
# Defines size for convert()
#--------------------------------------------------------
pygame.display.set_caption('Break the Bank')
gameicon = pygame.image.load("imgs/game_icon.png")
pygame.display.set_icon(gameicon)
size = 80

#--------------------------------------------------------
# Define buttons
#--------------------------------------------------------
class button():
    def __init__(self, x,y,width,height, text='', color = None,image=None, hovering_image=None, amplifier=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = image
        self.hovering_image = hovering_image
        self.amplifier = amplifier

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if self.color != None:
            if outline:
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
        if self.image != None:
            if self.amplifier == None:
                if not self.isOver(pygame.mouse.get_pos()):
                    image = pygame.image.load(self.image)
                    rect_image = image.get_rect()
                    
                    image = pygame.transform.scale(image, ((rect_image.width/(237.5*16))*size*16,(rect_image.height/(237.5*9))*size*9))
                    
                else:
                    image = pygame.image.load(self.hovering_image)
                    rect_image = image.get_rect()
                    image = pygame.transform.scale(image, ((rect_image.width/(237.5*16))*size*16,(rect_image.height/(237.5*9))*size*9))
            else:
                if not self.isOver(pygame.mouse.get_pos()):
                    image = pygame.image.load(self.image)
                    rect_image = image.get_rect()
                    #print(rect_image)
                    image = pygame.transform.scale(image, ((rect_image.width/(self.amplifier*16))*size*16,(rect_image.height/(self.amplifier*9))*size*9))
                else:
                    image = pygame.image.load(self.hovering_image)
                    rect_image = image.get_rect()
                    image = pygame.transform.scale(image, ((rect_image.width/(self.amplifier*16))*size*16,(rect_image.height/(self.amplifier*9))*size*9))
            win.blit(image, (self.x, self.y))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if self.image == None:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
                
            return False
        elif self.amplifier == None:
            image = pygame.image.load(self.image)
            rect_image = image.get_rect()
            if pos[0] > self.x and pos[0] < self.x + (rect_image.width/(237.5*16))*size*16:
                if pos[1] > self.y and pos[1] < self.y + (rect_image.height/(237.5*9))*size*9:
                    return True
            
            return False
        else:
            image = pygame.image.load(self.image)
            rect_image = image.get_rect()
            if pos[0] > self.x and pos[0] < self.x + (rect_image.width/(self.amplifier*16))*size*16:
                if pos[1] > self.y and pos[1] < self.y + (rect_image.height/(self.amplifier*9))*size*9:
                    return True
            
            return False

#--------------------------------------------------------
# Load music
#--------------------------------------------------------

#pygame.mixer.music.load("audio/menu_maintheme.mp3")
#pygame.mixer.music.load("audio/stage1_bgm_spookydarkpad.wav")
pygame.mixer.music.load("audio/maintheme_syndicate.wav")
pygame.mixer.music.set_volume(0.5)         

#--------------------------------------------------------
# Control objects on the Title Screen/Main Menu
#--------------------------------------------------------
def drawMainMenu():
    backgroundphoto = pygame.image.load("imgs/start_bare.png")#.convert()
    screen.blit(backgroundphoto,(0,0))
    start_button.draw(screen)
    quit_button.draw(screen)
    audio_button.draw(screen)
    accessibility_button.draw(screen)

#--------------------------------------------------------
# Control objects on the Stage Selection page
# - TODO: finalize page, add buttons for stages
#--------------------------------------------------------
def drawStageSelection():
    backgroundphoto = pygame.image.load("imgs/stage_select.png").convert()
    backgroundphoto = pygame.transform.scale(backgroundphoto, (size*16,size*9))
    screen.blit(backgroundphoto,(0,0))
    stage_placeholderbutton.draw(screen)
    quit_mainmenu_button.draw(screen)

#--------------------------------------------------------
# Control objects on the Pause Menu
#--------------------------------------------------------
def drawPauseMenu():
    #global backgroundphoto
    screen.blit(current_screen,(0,0))
    backgroundphoto = pygame.image.load("imgs/pause_bg_light.png")
    backgroundphoto = pygame.transform.scale(backgroundphoto, (size*16,size*9))
    #backgroundphoto.convert_alpha()
    backgroundphoto.set_alpha(250)
    screen.blit(backgroundphoto, (0,0))
    continue_button.draw(screen)
    restart_button.draw(screen)
    tutorial_button.draw(screen)
    pause_title.draw(screen)
    quit_button.draw(screen)
    audio_button.draw(screen)
    accessibility_button.draw(screen)

#--------------------------------------------------------
# Placeholder for In Game stages
# - TODO: this might need to be split into a def for 
#         every individual stage
#--------------------------------------------------------
def drawInGame():
    backgroundphoto = pygame.image.load("imgs/in_game.png")
    backgroundphoto = pygame.transform.scale(backgroundphoto, (size*16,size*9))
    screen.blit(backgroundphoto,(0,0))

#--------------------------------------------------------
# Set up the drawing window
#--------------------------------------------------------
screen = pygame.display.set_mode([size*16, size*9])
# screen = pygame.transform.scale(backgroundphoto,[859, 727])
width = screen.get_width()
height = screen.get_height()

start_button = button(width/2.807,height/1.6,20,100,'',None,"imgs/buttons/slice_start.png","imgs/buttons/hovering_slice_start.png")
quit_button = button(width/2.2,height/1.3,20,100,'',None,"imgs/buttons/slice_quit.png", "imgs/buttons/hovering_slice_quit.png")
quit_mainmenu_button = button(width/2.2,height/1.3,20,100,'',None,"imgs/buttons/slice_quit.png", "imgs/buttons/hovering_slice_quit.png")
audio_button = button(width/2.015748,height/1.15,20,100,'',None,"imgs/buttons/slice_audio.png", "imgs/buttons/hovering_slice_audio.png")
accessibility_button = button(width/2.4063063,height/1.15,20,100,'',None,"imgs/buttons/slice_cb.png", "imgs/buttons/hovering_slice_cb.png")
continue_button = button(width/2.4288,height/2.1951219, 20, 100, '', None, "imgs/buttons/slice_continue.png","imgs/buttons/hovering_slice_continue.png",160)
restart_button = button(width/2.4015,height/1.75182, 20, 100, '', None, "imgs/buttons/slice_restart.png","imgs/buttons/hovering_slice_restart.png",160)
tutorial_button = button(width/2.424242,height/1.50627, 20, 100, '', None, "imgs/buttons/slice_tutorial.png","imgs/buttons/hovering_slice_tutorial.png",160)
pause_title = button(width/3.12195,height/11.6129, 20, 100, '', None, "imgs/slice_paused.png","imgs/slice_paused.png",160) #bad code 

# TODO: placeholders for Stage Selection Menu
stage_placeholderbutton = button(width/18,height/3,0,20,'',None,"imgs/stage_placeholderbutton.png","imgs/stage_placeholderbutton_hover.png")
notify_msg = button( width/2+50, height/2, 250, 100,"PRESS ENTER TO GO BACK TO MAIN MENU FOR NOW",(255, 0, 255), None, None)
smallfont = pygame.font.SysFont('comicsansms',25)
text = smallfont.render('quit', True, (255,00,255))
color_light = (255,255,255)
color_dark = (0,0,0)

#--------------------------------------------------------
#Define Booleans for stage states
#--------------------------------------------------------
running = True #game run state
main_menu = True #title screen/main menu
pause_menu = False #game paused
stage_selection = False #level/stage select
in_game = False #in level/stage
in_cutscene = False #visual story mode
main_menu_music = True #if music should be playing

#--------------------------------------------------------
# Main Game Loop
# - Clock tick needs to be contained here
# - Game state is controlled here
#--------------------------------------------------------
while running:
    timer = pygame.time.Clock()
    timer.tick(60)

    if main_menu_music:
        pygame.mixer.music.play(-1)
        main_menu_music = False
        
    #-------------MAIN MENU-------------
    if main_menu:
        drawMainMenu()
        # screen.fill((40, 0, 80))
        # Did the user click the window close button?
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isOver(mouse):
                    print("TRIGGERED start game")
                    main_menu = False
                    in_game = False
                    stage_selection = True
                    main_menu_music = False
                    pygame.mixer.music.pause()
                if quit_button.isOver(mouse):
                    pygame.quit()
            # if event.type == pygame.MOUSEMOTION:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # print("width: " + str(width/mouse[0]))
                    # print("height: " + str(height/mouse[1]))
                    print(mouse)
    #-------------STAGE SELECTION-------------
    elif stage_selection:
        drawStageSelection()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stage_placeholderbutton.isOver(mouse):
                    print("TRIGGERED stage selection -> in game")
                    main_menu = False
                    in_game = True
                    stage_selection = False
                if quit_mainmenu_button.isOver(mouse):
                    main_menu = True
                    main_menu_music = True
                    stage_selection = False
    #-------------IN GAME-------------
    elif not main_menu and not pause_menu and in_game:
        #screen.fill((40, 0, 80))
        drawInGame()
        mouse = pygame.mouse.get_pos()
        main_menu = False
        in_game = True
        stage_selection = False
        in_cutscene = False
        #notify_msg.draw(screen)
        #print("we are supposed to be in game right now.")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = screen.copy()
                    # put physics stuff here to remember when unpausing
                    pause_menu = True
                if event.key == pygame.K_RETURN:
                    main_menu = True
    #-------------PAUSE MENU-------------
    elif pause_menu:
        screen.blit(current_screen, (0,0))
        drawPauseMenu()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.isOver(mouse):
                    print("test")
                    main_menu = False
                    pause_menu = False
                    in_game = True
                if quit_button.isOver(mouse):
                    main_menu = False
                    pause_menu = False
                    stage_selection = True
                    in_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # go back to game
                    pause_menu = False
                    main_menu = False
                    in_game = True
    pygame.display.update()
                #for finding location of button
                # if event.key == pygame.K_RIGHT:
                #     xIMG = xIMG+1
                # if event.key == pygame.K_LEFT:
                #     xIMG = xIMG-1
                # if event.key == pygame.K_DOWN:
                #     yIMG = yIMG+1
                # if event.key == pygame.K_UP:
                #     yIMG = yIMG-1
                # if event.key == pygame.K_RETURN:
                #     print("x: " +str(xIMG) + " y: " +str(yIMG))
                # if event.key == pygame.K_SPACE:
                #     # print("width: " + str(width/mouse[0]))
                #     # print("height: " + str(height/mouse[1]))
                #     print(pygame.mouse.get_pos())


    # Fill the background with white
    
    
    # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
    #         pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
            
    # else:
    #     pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
    # screen.blit(text , (width/2+50,height/2))


# Done! Time to quit.
pygame.quit()
