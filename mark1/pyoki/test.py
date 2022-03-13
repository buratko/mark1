thirdffont = pygame.font.Font('freesansbold.ttf', thirdLyrics[3])
thirdftext = thirdffont.render(thirdLyrics[6][thirdtimecount], True, 'royalblue', 'blue')
thirdftextRect = thirdftext.get_rect()
thirdftextVX,thirdftextVY,thirdftextX,thirdftextY = thirdftextRect

thirdtest = (track_pos-thirdLyrics[0])
thirdregLyricsTime = re.findall("\{([0-9_]+)\}",thirdLyrics[5])
thirddivLyric = thirdtextX/len(thirdLyrics[6])#  Divide All Lyrics
thirdlenLyric = len(thirdLyrics[6][thirdtimecount]) # 1-2
thirdformula2 = thirddivLyric*thirdtimecount
thirdformula3 = thirdftextX/(int(thirdregLyricsTime[thirdtimecount])*10)
thirdformula4 = thirdtextVX+thirddtextX+((thirdtest-thirdcounttime)*thirdformula3)
if thirdformula4 > thirdcounter:
    thirdcounter = thirdformula4
if int(thirdregLyricsTime[thirdtimecount+1]):
    if thirdtest >= thirdcounttime:
        thirdgagu = thirdgagu + str(thirdLyrics[6][thirdtimecount])
        thirdcounttime = thirdcounttime + int(thirdregLyricsTime[thirdtimecount])*10
        thirdtimecount += 1
        thirddfont = pygame.font.Font('freesansbold.ttf', thirdLyrics[3])
        thirddtext = thirddfont.render(thirdgagu, True, 'royalblue', 'blue')
        thirddtextRect = thirddtext.get_rect()
        thirddtextVX,thirddtextVY,thirddtextX,thirddtextY = thirddtextRect
