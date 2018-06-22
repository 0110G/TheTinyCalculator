#!/usr/bin/python
import pygame,sys
from pygame.locals import *

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
L_BLUE = (0,0,10)
screen_width = 300
screen_height = 400
cell_value = {(10,70):'7',(80,70):'8',(150,70):'9',(10,130):'4',(80,130):'5',(150,130):'6',(10,190):'1',(80,190):'2',(150,190):'3',(220,70):'+',(220,130):'-',(220,190):'*',(10,250):'.',(80,250):'0',(150,250):'Clear',(220,250):'/',(10,310):'=',}



def draw_calculator () :
	pygame.draw.rect(DISPLAY,GREEN,(10,70,60,50))	#7
	pygame.draw.rect(DISPLAY,GREEN,(80,70,60,50))	#8
	pygame.draw.rect(DISPLAY,GREEN,(150,70,60,50))	#9
	pygame.draw.rect(DISPLAY,GREEN,(10,130,60,50))	#4
	pygame.draw.rect(DISPLAY,GREEN,(80,130,60,50))	#5
	pygame.draw.rect(DISPLAY,GREEN,(150,130,60,50))	#6
	pygame.draw.rect(DISPLAY,GREEN,(10,190,60,50))	#1
	pygame.draw.rect(DISPLAY,GREEN,(80,190,60,50))	#2
	pygame.draw.rect(DISPLAY,GREEN,(150,190,60,50))	#3
	pygame.draw.rect(DISPLAY,GREEN,(220,70,60,50))	#+
	pygame.draw.rect(DISPLAY,GREEN,(220,130,60,50))	#-
	pygame.draw.rect(DISPLAY,GREEN,(220,190,60,50))	#*
	pygame.draw.rect(DISPLAY,GREEN,(10,250,60,50))	#.
	pygame.draw.rect(DISPLAY,GREEN,(80,250,60,50))	#0
	pygame.draw.rect(DISPLAY,GREEN,(150,250,60,50))	#Clear
	pygame.draw.rect(DISPLAY,GREEN,(220,250,60,50))	#/
	pygame.draw.rect(DISPLAY,GREEN,(10,310,270,50))	#=
	pygame.draw.rect(DISPLAY,(135,206,250),(10,10,270,50))

def text_objects(text, font) :
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text,font_size,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)                              #200 307
    DISPLAY.blit(TextSurf, TextRect)

def display_cell_values () :
	message_display ("7",15,40,95)
	message_display ("8",15,110,95)
	message_display ("9",15,180,95)
	message_display ("+",15,250,95)

	message_display ("4",15,40,155)
	message_display ("5",15,110,155)
	message_display ("6",15,180,155)
	message_display ("-",15,250,155)

	message_display ("1",15,40,215)
	message_display ("2",15,110,215)
	message_display ("3",15,180,215)
	message_display ("x",15,250,215)

	message_display (".",15,40,275)
	message_display ("0",15,110,275)
	message_display ("Clr",15,180,275)
	message_display ("/",15,250,275)

	message_display ("=",15,145,335)
	message_display ("GUI Developed by Bhavya Saraf",15,140,380)
def get_cell_position (mouse) :

	if mouse[0] >= 10 and mouse[0] <= 280 and mouse[1] >= 310 and mouse[1] <= 360 :
		return 10,310

	for cell_x in range (10,230,70) :
		for cell_y in range (70,260,60) :
			if mouse[0] >= cell_x and mouse[0] <= cell_x + 60 and mouse[1] >= cell_y and mouse[1] <= cell_y + 50 :
				return cell_x,cell_y
	return 0

def blink_cell_on_hover (mouse) :
	global count,x,y
	count = 0
	if get_cell_position(mouse) == 0:
		return 0
	else :
		x,y = get_cell_position(mouse)
		if x == 10 and y == 310 :
			pygame.draw.rect(DISPLAY,BLUE,(10,310,270,50))
			return 1
		pygame.draw.rect(DISPLAY,BLUE,(x,y,60,50))
		return 1

def calculator_display(message) :
	message_display(message,40,120,30)

def check_validity(expression):
	l = len(expression)
	status = True
	if expression[0] == '*' or expression[0] == '/' :
		return True
	for i in range (l) :
		if expression[i] <= '9' and expression[i] >= '0' :
			continue
		else :

			if expression[i] == '+' and expression[i+1] in ('*','/'):
				return False
			elif expression[1] == '-' and expression[i+1] in ('*','/'):
				return False
			elif expression[i] == '.':
				if expression[i+1] in ('+','-','*','/','.'):
					return False
				else :
					if status == True :
						status = False
					else :
						return 0,0
			else :
				status = True
	
	return True


pygame.init()
fpsClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pocket Calculator')
count = 0
num1 = ''
num2 = ''
while True :
	DISPLAY.fill(WHITE)
	mouse = pygame.mouse.get_pos()
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN :
			if event.button == 1:
				if get_cell_position(mouse) == 0:
					continue
				elif cell_value[(x,y)] == '=': 
					if check_validity(num1) :
						num1 = str(eval(num1,None,None))
					else :
						num1 = 'Error'
					#x,y = get_cell_position(mouse)
				elif cell_value[(x,y)] == 'Clear' :
					num1=''
				else :
					num1 = num1+cell_value[(x,y)]


	draw_calculator()
	calculator_display(num1)
	blink_cell_on_hover(mouse)
	display_cell_values()
	pygame.display.update()
	fpsClock.tick(30)
