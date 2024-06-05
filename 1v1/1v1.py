import pygame as pg
from sys import exit
import random

pg.init()
#background
bg=pg.image.load(r"bgc.png")
#font
game_font=pg.font.Font(r"Pixeltype.ttf",30)

def display_health1(x,y):
    a=10
    health_surf=game_font.render(f'{a}/10',False,(0,0,0))
    health_rect=health_surf.get_rect(topleft=(x,y))
    screen.blit(health_surf,health_rect)
def display_shield1(x,y):
    b=5
    shield_surf=game_font.render(f'{b}/5',False,(0,0,0))
    shield_rect=shield_surf.get_rect(topleft=(x,y))
    screen.blit(shield_surf,shield_rect)
#computer_stone
def stone1(x,y):
    stone=pg.image.load(r"stone.png")
    stone1=pg.transform.scale(stone,(190,310))
    stone_rect=stone1.get_rect(topleft=(x,y))
    screen.blit(stone1,stone_rect)

#computer_paper
def paper1(x,y):
    paper=pg.image.load(r"paper.png")
    paper1=pg.transform.scale(paper,(190,250))#THIS ONE :))
    paper_rect=paper1.get_rect(topleft=(x,y))
    screen.blit(paper1,paper_rect)
#computer_scissor
def scissor1(x,y):
    scissor=pg.image.load(r"scissor.png")
    scissor1=pg.transform.scale(scissor,(180,240))
    scissor_rect=scissor1.get_rect(topleft=(x,y))
    screen.blit(scissor1,scissor_rect)

# player_stone
def stone(x,y):
    stone=pg.image.load(r"stone.png")
    stone1=pg.transform.scale(stone,(90,150))
    stone_rect=stone1.get_rect(topleft=(x,y))
    screen.blit(stone1,stone_rect)
def stone2(x,y):
    stone=pg.image.load(r"stone.png")
    stone1=pg.transform.scale(stone,(130,190))
    stone_rect=stone1.get_rect(topleft=(x,y))
    screen.blit(stone1,stone_rect)


#player_paper
def paper(x,y):
    paper=pg.image.load(r"paper.png")
    paper1=pg.transform.scale(paper,(90,120))#THIS ONE :))
    paper_rect=paper1.get_rect(topleft=(x,y))
    screen.blit(paper1,paper_rect)

def paper2(x,y):
    paper=pg.image.load(r"paper.png")
    paper1=pg.transform.scale(paper,(130,150))
    paper_rect=paper1.get_rect(topleft=(x,y))
    screen.blit(paper1,paper_rect)
#player_scissor
def scissor(x,y):
    scissor=pg.image.load(r"scissor.png")
    scissor1=pg.transform.scale(scissor,(85,115))
    scissor_rect=scissor1.get_rect(topleft=(x,y))
    screen.blit(scissor1,scissor_rect)

def scissor2(x,y):
    scissor=pg.image.load(r"scissor.png")
    scissor1=pg.transform.scale(scissor,(115,145))
    scissor_rect=scissor1.get_rect(topleft=(x,y))
    screen.blit(scissor1,scissor_rect)
#black_boxes
def black_box(x,y):
    black_box1=pg.image.load(r"bl box.png")
    black_box11=pg.transform.scale(black_box1,(250,250))
    black_box_rect=black_box1.get_rect(topleft=(x,y))
    screen.blit(black_box11,black_box_rect)
def black_box2(x,y):
    black_box1=pg.image.load(r"blbox2.png")
    black_box11=pg.transform.scale(black_box1,(325,325))
    black_box_rect=black_box1.get_rect(topleft=(x,y))
    screen.blit(black_box11,black_box_rect)

#heart_img
def heart(x1,y2):
    hi=pg.image.load(r"health.png")
    hi1=pg.transform.scale(hi,(33,33))
    hi_rect=hi1.get_rect(topleft=(x1,y2))
    screen.blit(hi1,hi_rect)

def health_border(x,y):
    hb=pg.Rect(x,y,105,30)
    pg.draw.rect(screen,(0,0,0),hb)

#shield_img
def shield(x1,y1):
    si=pg.image.load(r"shield.png")
    si1=pg.transform.scale(si,(35,35))
    si_rect=si1.get_rect(topleft=(x1,y1))
    screen.blit(si1,si_rect)

def shield_border(x,y):
    sb=pg.Rect(x,y,55,30)
    pg.draw.rect(screen,(0,0,0),sb)

#Cards
def card(x1,y1):
    card1=pg.image.load(r"card 1.png")
    card11=pg.transform.scale(card1,(105,120))
    card1_rect=card11.get_rect(topleft=(x1,y1))
    screen.blit(card11,card1_rect)

    mouse_pos = pg.mouse.get_pos()
    if card1_rect.collidepoint(mouse_pos):
        card2_image = pg.image.load(r"card 2.png") 
        card2_scaled = pg.transform.scale(card2_image, (105, 120))  
        screen.blit(card2_scaled, card1_rect.topleft) 
    else:  
        screen.blit(card11, card1_rect)

def card2(x1,y1):
    card2=pg.image.load(r"card 2.png")
    card22=pg.transform.scale(card2,(105,120))
    card2_rect=card22.get_rect(topleft=(x1,y1))
    screen.blit(card22,card2_rect)

#player_health
a=100
ph1=pg.Rect(0,0,100,25)#format(x,y,width,height)
ph2=pg.Rect(0,0,a,25)

#player_shield
a1=50
ps1=pg.Rect(150,0,a1,25)
ps2=pg.Rect(150,0,50,25)

#computer_health
b=100
ch1=pg.Rect(700,0,100,25)#format(x,y,width,height)
ch2=pg.Rect(700,0,b,25)

#computer_shield
b2=50 
cs1=pg.Rect(600,0,b2,25)
cs2=pg.Rect(600,0,50,25)

sw=800
sh=450
screen=pg.display.set_mode((sw,sh))
pg.display.set_caption("1v1")

#GAME LOOP
selected_card=None
computer_choice=None
game_status=True
result_display_time = None
while game_status==True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game_status=False
            pg.quit()
            exit()
    screen.blit(bg,(0,0))
    health_border(0,0)
    pg.draw.rect(screen,(252,0,0),ph1)#red
    pg.draw.rect(screen,(0, 222, 74),ph2)#green
    health_border(695,0)
    pg.draw.rect(screen,(252,0,0),ch1)#red
    pg.draw.rect(screen,(0, 222, 74),ch2)#green
    shield_border(150,0)
    pg.draw.rect(screen,(252,0,0),ps2)#red
    pg.draw.rect(screen,(36, 126, 255),ps1)#blue
    shield_border(595,0)
    pg.draw.rect(screen,(252,0,0),cs2)#red
    pg.draw.rect(screen,(36, 126, 255),cs1)#blue
    heart(0,0)
    heart(770,0)
    shield(130,-5)
    shield(634,-5)
    card(20,300)
    card(140,300)
    card(260,300)
    black_box(70,50)
    black_box2(450,50)
    stone(30,283)
    paper(147,302)
    scissor(270,303)
    display_health1(40,5)
    display_health1(715,5)
    display_shield1(165,5)
    display_shield1(605,5)
    if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            card1_rect = pg.Rect(20, 300, 105, 120)
            card2_rect = pg.Rect(140, 300, 105, 120)
            card3_rect = pg.Rect(260, 300, 105, 120)
            if card1_rect.collidepoint(mouse_pos):
                selected_card="stone"
            elif card2_rect.collidepoint(mouse_pos): 
                selected_card="paper"
            elif card3_rect.collidepoint(mouse_pos):
                selected_card="scissor"
            result_display_time = pg.time.get_ticks()
    if selected_card=="stone":
        stone2(130,77)
    if selected_card=="paper":
        paper2(130,102)
    if selected_card=="scissor":
        scissor2(135,102)
#BRAIN
    if selected_card and computer_choice is None:
        computer_choice = random.choice(["stone", "paper", "scissor"])
        print(f"Computer's choice: {computer_choice}")
    if selected_card and computer_choice:
        if selected_card == computer_choice:
            print("Draw")
        elif (selected_card == "stone" and computer_choice == "scissor") or \
             (selected_card == "paper" and computer_choice == "stone") or \
             (selected_card == "scissor" and computer_choice == "paper"):
            print("Player wins")
        else:
            print("Computer wins")
    if computer_choice == "stone":
           stone1(520,60)
    elif computer_choice == "paper":
         paper1(510,90)
    elif computer_choice == "scissor":
         scissor1(520,95)
    
    if result_display_time and pg.time.get_ticks() - result_display_time > 1000:
        selected_card = None
        computer_choice = None
        result_display_time = None
    pg.display.update()
pg.quit()
