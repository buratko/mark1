import re,time,os,pysubs2
import pygame
import pygame.freetype
import random
import math, itertools
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
royalblue = pygame.Color('royalblue')
black = (0, 0, 0)
red = (255, 25, 25)
grey = (30, 30, 30)
window_width = 900
window_height = 700
display_surface = pygame.display.set_mode((window_width, window_height))
#display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_width, window_height = pygame.display.get_surface().get_size()
mixer.init()
volume_offset = 0.7
songinfo = mixer.music.load("songs\\1111.ogg")
mixer.music.set_volume(0.7)
mixer.music.play()
font = pygame.font.Font('freesansbold.ttf', 80, bold=True)
fix_window_width = window_width-((2/100)*window_width)*2

MUSIC_END = pygame.USEREVENT+1
mixer.music.set_endevent(MUSIC_END)

def font_size_checker(text, fwid, fhit):
    font_text_size = 1
    while True:
        font = pygame.font.Font('freesansbold.ttf', font_text_size)
        text_width, text_height = font.size(text)
        if text_width > fwid or text_height > fhit:
            font_text_size -= 1
            break
        else:
            font_text_size += 1
    return font_text_size

def check_font_size(text):
    font_size = 0
    font_text_size = 110
    while True:
        font = pygame.font.Font('freesansbold.ttf', font_text_size)
        text_width, text_height = font.size(text)
        if text_width > fix_window_width:
            font_text_size = font_text_size - 1
        else:
            font_size = font_text_size
            break
    return font_size

lyrics = []
subs = pysubs2.load("songs\\1111.ass")


for line in subs:
    linecounter = 0
    regLyrics = re.findall('\{.*?\}([\'-.a-zA-Z0-9,!? ]+)',line.text)
    regFixLyrics = str(''.join(regLyrics))
    regFixTime = line.text.replace("\k", "")
    if regLyrics:
        font_size = check_font_size(regFixLyrics)
        lyrics.append([line.start,line.end,regFixLyrics,font_size,white,regFixTime,regLyrics])

firstLyrics = []
secondLyrics = []
thirdLyrics = []
intro_count = True

def vol_up():
    global volume_offset
    volume_offset += 0.1
    if volume_offset > 1.0:
        volume_offset = 1.0
    mixer.music.set_volume(volume_offset)
def vol_down():
    global volume_offset
    volume_offset -= 0.1
    if volume_offset < 0:
        volume_offset = 0.0
    mixer.music.set_volume(volume_offset)


def get_rand_int():
    tech = [random.randint(75,79), random.randint(80,89), random.randint(90,95), random.randint(96,100)]
    weight = [3, 5, 1, 0.5]
    rand_value = random.choices(tech, k = 1, weights = weight)
    return rand_value[0]

linemargin = window_width-fix_window_width
startline = (5/100)*window_width
endline = (95/100)*window_width
countdownformula = window_width/4000

#     0          1           2            3        4         5              6
# STARTTIME - ENDTIME - FULL LYRICS - FONTSIZE - COLOR - LYRICSTIME - LYRICS ONE BY ONE

count = 0
scoreWindow = False
scorecounter = 0
scoresize = font_size_checker('100', window_width-((10/100)*window_width), window_height-((10/100)*window_height))
is_play_once = None

mainWindow = False

while True:
    track_pos = mixer.music.get_pos()
    display_surface.fill(grey)
    print(int(count))
    count += 1/300

    if mainWindow:
        mainfont = pygame.font.Font('freesansbold.ttf', 200)
        maintext = mainfont.render('Main Window', True, white)
        maintextRect = maintext.get_rect()
        maintextRect.center = (window_width // 2, window_height // 2)
        display_surface.blit(maintext, maintextRect)


    if lyrics or firstLyrics or secondLyrics or thirdLyrics:
        mainWindow = False
        if not firstLyrics and lyrics:
            firstLyrics = lyrics[0]
            first_run_once = True

            firstregLyricsTime = re.findall("\{([0-9_]+)\}",firstLyrics[5])

            firsttimecount = 0
            firstcounttime = int(firstregLyricsTime[0])
            #firstcounttime = 0
            firstgagu = str(firstLyrics[6][firsttimecount])
            #firstcounttime = 0
            #print(firstregLyricsTime)
            #exit()
            #print(len(firstregLyricsTime))


            #firstdivLyric = 0
            #firstlenLyric = 0

            firstcounter = 0
            firstfont = pygame.font.Font('freesansbold.ttf', firstLyrics[3])
            firsttext = firstfont.render(firstLyrics[2], True, 'royalblue')
            firsttextRect = firsttext.get_rect()
            firsttextRect.center = (window_width // 2, (25/100)*window_height)
            firsttextVX,firsttextVY,firsttextX,firsttextY, = firsttextRect

            #exit()


            firstfrontfont = pygame.font.Font('freesansbold.ttf', firstLyrics[3])
            firstfronttext = firstfrontfont.render(firstLyrics[2], True, 'white')
            firstfronttextRect = firsttext.get_rect()
            firstfronttextVX,firstfronttextVY,firstfronttextX,firstfronttextY, = firstfronttextRect
            timecount = 0


            bugok = ''
            #print("Orig: "+str(firsttextRect))
            firstdtextX = 0
            lyrics.pop(0)
        if not secondLyrics and lyrics:
            secondLyrics = lyrics[0]
            secondregLyricsTime = re.findall("\{([0-9_]+)\}",secondLyrics[5])
            secondtimecount = 0
            secondcounttime = int(secondregLyricsTime[0])
            secondgagu = str(secondLyrics[6][secondtimecount])
            seconddtextX = 0

            #print(len(secondregLyricsTime))



            secondcounter = 0

            secondfont = pygame.font.Font('freesansbold.ttf', secondLyrics[3])
            secondtext = secondfont.render(secondLyrics[2], True, 'royalblue')
            secondtextRect = secondtext.get_rect()
            secondtextRect.center = (window_width // 2, (45/100)*window_height)
            secondtextVX,secondtextVY,secondtextX,secondtextY, = secondtextRect

            secondfrontfont = pygame.font.Font('freesansbold.ttf', secondLyrics[3])
            secondfronttext = secondfrontfont.render(secondLyrics[2], True, 'white')
            secondfronttextRect = secondtext.get_rect()
            secondfronttextVX,secondfronttextVY,secondfronttextX,secondfronttextY, = secondfronttextRect

            lyrics.pop(0)
            second_run_once = True
        if not thirdLyrics and lyrics:
            thirdLyrics = lyrics[0]

            thirdregLyricsTime = re.findall("\{([0-9_]+)\}",thirdLyrics[5])

            thirdtimecount = 0
            thirdcounttime = int(thirdregLyricsTime[0])
            thirdgagu = str(thirdLyrics[6][thirdtimecount])
            thirddtextX = 0

            thirdcounter = 0
            thirdfont = pygame.font.Font('freesansbold.ttf', thirdLyrics[3])
            thirdtext = thirdfont.render(thirdLyrics[2], True, 'royalblue')
            thirdtextRect = thirdtext.get_rect()
            thirdtextRect.center = (window_width // 2, (65/100)*window_height)
            thirdtextVX,thirdtextVY,thirdtextX,thirdtextY, = thirdtextRect

            thirdfrontfont = pygame.font.Font('freesansbold.ttf', thirdLyrics[3])
            thirdfronttext = thirdfrontfont.render(thirdLyrics[2], True, 'white')
            thirdfronttextRect = thirdtext.get_rect()
            thirdfronttextVX,thirdfronttextVY,thirdfronttextX,thirdfronttextY, = thirdfronttextRect

            lyrics.pop(0)
            third_run_once = True


        try:
            display_surface.fill(grey)
            #===================================================================
            display_surface.blit(firsttext, firsttextRect)
            firstempty_surface = pygame.Surface((firsttextX,firsttextY), pygame.SRCALPHA)
            firstempty_surfaceRect = firstempty_surface.get_rect().center

            firstnewtext = pygame.transform.chop(firstfronttext, (0, 0, firstcounter, 0))
            firstempty_surface.blit(firstnewtext, (firstcounter, firstfronttextVY))
            display_surface.blit(firstempty_surface, (firsttextVX,firsttextVY))

            #===================================================================
            display_surface.blit(secondtext, secondtextRect)
            secondempty_surface = pygame.Surface((secondtextX,secondtextY), pygame.SRCALPHA)
            secondempty_surfaceRect2 = secondempty_surface.get_rect().center

            secondnewtext = pygame.transform.chop(secondfronttext, (0, 0, secondcounter, 0))
            secondempty_surface.blit(secondnewtext, (secondcounter, secondfronttextVY))
            display_surface.blit(secondempty_surface, (secondtextVX,secondtextVY))

            #===================================================================
            display_surface.blit(thirdtext, thirdtextRect)
            thirdempty_surface = pygame.Surface((thirdtextX,thirdtextY), pygame.SRCALPHA)
            thirdempty_surfaceRect2 = thirdempty_surface.get_rect().center

            thirdnewtext = pygame.transform.chop(thirdfronttext, (0, 0, thirdcounter, 0))
            thirdempty_surface.blit(thirdnewtext, (thirdcounter, thirdfronttextVY))
            display_surface.blit(thirdempty_surface, (thirdtextVX,thirdtextVY))





            if firstLyrics:
                if track_pos >= firstLyrics[0] and track_pos <= firstLyrics[1]:
                    try:

                        firstffont = pygame.font.Font('freesansbold.ttf', firstLyrics[3])
                        firstftext = firstffont.render(firstLyrics[6][firsttimecount], True, 'royalblue', 'blue')
                        firstftextRect = firstftext.get_rect()
                        firstftextVX,firstftextVY,firstftextX,firstftextY = firstftextRect


                        firstdfont = pygame.font.Font('freesansbold.ttf', firstLyrics[3])
                        firstdtext = firstdfont.render(firstgagu, True, 'royalblue', 'blue')
                        firstdtextRect = firstdtext.get_rect()
                        firstdtextVX,firstdtextVY,firstdtextX,firstdtextY = firstdtextRect


                        firsttest = (track_pos-firstLyrics[0])

                        firstformula3 = firstftextX/(int(firstregLyricsTime[firsttimecount])*10)
                        firstformula4 = firstdtextX+((firsttest-firstcounttime)*firstformula3)
                        if firstformula4 > firstcounter:
                            firstcounter = firstformula4
                        if int(firstregLyricsTime[firsttimecount+1]):
                            if firsttest >= firstcounttime:

                                firstcounttime = firstcounttime + (int(firstregLyricsTime[firsttimecount])*10)
                                firsttimecount += 1
                                firstgagu = firstgagu + str(firstLyrics[6][firsttimecount])

                                #print(firsttimecount)

                    except Exception as e:
                        if first_run_once:
                            #print("Error: "+str(e))
                            first_run_once = False
                        pass
                    if(thirdLyrics[1] < track_pos and lyrics):
                        thirdLyrics = []
            if secondLyrics:
                if track_pos >= secondLyrics[0] and track_pos <= secondLyrics[1]:
                    try:
                        secondffont = pygame.font.Font('freesansbold.ttf', secondLyrics[3])
                        secondftext = secondffont.render(secondLyrics[6][secondtimecount], True, 'royalblue', 'blue')
                        secondftextRect = secondftext.get_rect()
                        secondftextVX,secondftextVY,secondftextX,secondftextY = secondftextRect

                        seconddfont = pygame.font.Font('freesansbold.ttf', secondLyrics[3])
                        seconddtext = seconddfont.render(secondgagu, True, 'royalblue', 'blue')
                        seconddtextRect = seconddtext.get_rect()
                        seconddtextVX,seconddtextVY,seconddtextX,seconddtextY = seconddtextRect

                        secondtest = (track_pos-secondLyrics[0])
                        #print(secondcounter)
                        secondformula3 = secondftextX/(int(secondregLyricsTime[secondtimecount])*10)
                        secondformula4 = seconddtextX+((secondtest-secondcounttime)*secondformula3)
                        if secondformula4 > secondcounter:
                            secondcounter = secondformula4
                        if int(secondregLyricsTime[secondtimecount+1]):
                            if secondtest >= secondcounttime:

                                #print(secondgagu)
                                secondcounttime = secondcounttime + int(secondregLyricsTime[secondtimecount])*10
                                secondtimecount += 1
                                secondgagu = secondgagu + str(secondLyrics[6][secondtimecount])

                                #print(secondtimecount)

                    except Exception as e:
                        if second_run_once:
                            #print("Error: "+str(e))
                            second_run_once = False
                        pass
                    if(firstLyrics[1] < track_pos and lyrics):
                        firstLyrics = []
            if thirdLyrics:
                if track_pos >= thirdLyrics[0] and track_pos <= thirdLyrics[1]:
                    try:
                        thirdffont = pygame.font.Font('freesansbold.ttf', thirdLyrics[3])
                        thirdftext = thirdffont.render(thirdLyrics[6][thirdtimecount], True, 'royalblue', 'blue')
                        thirdftextRect = thirdftext.get_rect()
                        thirdftextVX,thirdftextVY,thirdftextX,thirdftextY = thirdftextRect

                        thirdtest = (track_pos-thirdLyrics[0])

                        thirdlenLyric = len(thirdLyrics[6][thirdtimecount]) # 1-2
                        thirdformula3 = thirdftextX/(int(thirdregLyricsTime[thirdtimecount])*10)
                        thirdformula4 = thirddtextX+((thirdtest-thirdcounttime)*thirdformula3)
                        if thirdformula4 > thirdcounter:
                            thirdcounter = thirdformula4
                        if int(thirdregLyricsTime[thirdtimecount+1]):
                            if thirdtest >= thirdcounttime:
                                thirdcounttime = thirdcounttime + int(thirdregLyricsTime[thirdtimecount])*10
                                thirdtimecount += 1
                                thirdgagu = thirdgagu + str(thirdLyrics[6][thirdtimecount])
                                thirddfont = pygame.font.Font('freesansbold.ttf', thirdLyrics[3])
                                thirddtext = thirddfont.render(thirdgagu, True, 'royalblue', 'blue')
                                thirddtextRect = thirddtext.get_rect()
                                thirddtextVX,thirddtextVY,thirddtextX,thirddtextY = thirddtextRect
                    except Exception as e:
                        if third_run_once:
                            #print("Error: "+str(e))
                            #thirdcounter = thirdtextX
                            third_run_once = False
                        pass

                    if(secondLyrics[1] < track_pos and lyrics):
                        secondLyrics = []


            gago = 0
            if intro_count:
                if (int(firstLyrics[0])-track_pos) < 4000 and (int(firstLyrics[0])-track_pos) > 0:
                    gago = countdownformula*(firstLyrics[0]-track_pos)
                    if gago > 0:
                        startline = (window_width//2)-(gago//2)
                        startline = startline+linemargin
                        if startline > window_width//2:
                            startline = window_width//2
                            intro_count = False
                        endline = (window_width//2)+(gago//2)
                        endline = endline-linemargin
                        if endline < window_width//2:
                            endline = window_width//2
                            intro_count = False
                pygame.draw.line(display_surface, 'green', (startline,100), (endline,100), 3)

        except Exception as e:
            print("Error: "+str(e))

    if scoreWindow:
        if not scorecounter >= 30:
            score = get_rand_int()
            scorefont = pygame.font.Font('freesansbold.ttf', scoresize)
            scoretext = scorefont.render(str(score), True, white)
            scoretextRect = scoretext.get_rect()
            scoretextRect.center = (window_width // 2, window_height // 2)
            display_surface.blit(scoretext, scoretextRect)
            scorecounter += .1
        else:
            scorefont = pygame.font.Font('freesansbold.ttf', scoresize)
            scoretext = scorefont.render(str(score), True, green)
            scoretextRect = scoretext.get_rect()
            scoretextRect.center = (window_width // 2, window_height // 2)
            display_surface.blit(scoretext, scoretextRect)
            if is_play_once:
                mixer.music.load("scoresound.ogg")
                mixer.music.set_volume(.3)
                mixer.music.play()
                is_play_once = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == MUSIC_END:
            #mixer.music.unload()
            lyrics,firstLyrics,secondLyrics,thirdLyrics = [],[],[],[]
            if scoreWindow:
                scoreWindow = False
                mainWindow = True
            else:
                is_play_once = True
                scoreWindow = True
            print('music end event')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_s:
                #lyrics,firstLyrics,secondLyrics,thirdLyrics = [],[],[],[]
                mixer.music.stop()
            if event.key == pygame.K_KP_PLUS:
                #mixer.music.unload()
                mixer.music.load("scoresound.ogg")
                mixer.music.set_volume(.7)
                mixer.music.play()
                #vol_up()
                print(volume_offset)
                print("PLUS")
            if event.key == pygame.K_KP_MINUS:
                vol_down()
                print(volume_offset)
                print("MINUS")
            if event.key == pygame.K_HOME:
                print("HOME")
            if event.key == pygame.K_p:
                if mixer.music.get_busy():
                    mixer.music.pause()
                else:
                    mixer.music.unpause()


    pygame.display.flip()
    #clock.tick(30)
