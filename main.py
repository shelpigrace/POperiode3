# PO periode 3 met twee amsterdammers en SLI, BITCHESSSSSSSSSSSSSSSSS
import pygame, random  # imorteren van de pygame en random libraries


# -------- Globale variabelen --------

# coordinaten van de vakjes:
vakjes = vakjes = [[870,460], [870,380], [870, 315], [870,250], [870, 180], [870, 110],[795,70], [710,70], [710,142], [710,210], [710,280], [710, 348], [710, 415], [710, 478], [639,475], [562,475], [486, 475], [410, 475],[336, 475], [261, 475], [188, 475], [117,475], [70,410], [65,343], [65,270],[65, 206], [65,136], [86,68], [166,67], [240,67], [315,67],[387,67], [465,67], [509,144], [557,214], [570,285], [558,357],[475,382], [394,392], [305,396], [226,389], [156,319], [153,244],[163,174], [250,147], [340,150], [422,183], [453,260], [373,305],[270,285], [324,229]] # laatste coordinaat is van kleine vakje, moet nog worden aangepast!! 

# pion posities
posities = [0,0,0]

# wie is aan de beurt?
huidige_speler_beurt = 0

# dobbelsteenworp:
worp = 0

# bord afbeelding
bord = pygame.image.load("fotos/leipe levensweg4.0.png")

# -------- Pygame initialisatie --------

# Pygame initialiseren (is altijd nodig bij begin van gebruik pygame)
pygame.init()

# Afmetingen van het spelscherm instellen (in pixels [breedte, hoogte])
# Daarna het spelscherm maken (en opslaan in een variabele screen)
WINDOW_SIZE = [960, 540]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Titel van het spelscherm instellen:
pygame.display.set_caption("Leuke Levensweg langs... de weg")

# Deze boolean laat ons spel straks in een oneindige loop lopen, totdat er op 
# het kruisje wordt geklikt om af te sluiten (deze zet dan done op True)
done = False

# We maken een pygame Clock object. Deze is nodig om de verversingssnelheid
# (framerate) van het scherm te beheren
clock = pygame.time.Clock()

# spelers
spelers = ['Speler 1', 'Speler 2', 'Speler 3']



# -------- Hoofdloop van het programma --------

while not done:

    # --- Check gebeurtenissen (zoals muiskliks e.d.) en werk de administratie bij ---

    for event in pygame.event.get():  # doorloop alle gebeurtenissen sinds de vorige schermupdate

        if event.type == pygame.QUIT: # Gebeurtenis: het kruisje is aangeklikt
            done = True # Het spel moet eindigen dus we zetten done op True, zodat de loop straks stopt
        elif event.type == pygame.KEYDOWN:
            # Er is een toets ingedrukt, we kijken welke en ondernemen actie
            if event.key == pygame.K_SPACE: # spatie
                print("Knop: Spatie")

                worp = random.randint(1,6) #kies een random getal tussen 1 en 6 als dobbelsteenworp
                posities[huidige_speler_beurt] += worp # verzet de pion die op dit moment aan de beurt is

                # is de pion op of voorbij het laatste vakje? Zal valt hij van het bord af!
                # Zet hem dan precies op het laatste vakje om dat te voorkomen:
                if posities[huidige_speler_beurt] >= 50:
                    posities[huidige_speler_beurt] = 50
                # heeft de speler nog niet gewonnen? Ga dan de beurt door naar de vol
                else:
                # beurt wisselen
                 huidige_speler_beurt = (huidige_speler_beurt + 1) % 3 

            elif event.key == pygame.K_BACKSPACE: #backspace
                print("Knop: Backspace")
                huidige_speler_beurt = 0  # Terug naar speler 0
                posities = [0, 0, 0]  # Reset spelerposities naar begin
    # --- Teken de graphics voor de volgende schermupdate (nog buiten beeld) ---
  
    screen.fill((255,255,255)) # begin met een witte achtergrond 

    bordrect = bord.get_rect() #vraag afmetingen (rectangle) van het bordplaatje op
    screen.blit(bord, bordrect) # teken het bord op het volgende screen:

    # teken pionnen als gekleurde cirkels op de coordinaten van de vakjes waar ze staan:
    speler0_x = vakjes[posities[0]][0]; # x-cordinaten pion speler 0
    speler0_y = vakjes[posities[0]][1]; # y-cordinaten pion speler 0
    kleur0 = (0,255,0) # groene pion
    pygame.draw.circle(screen, kleur0, (speler0_x, speler0_y), 10) # teken cirkel als pion speler 0
    speler1_x = vakjes[posities[1]][0] + 5; # x-cordinaten pion speler 1
    speler1_y = vakjes[posities[1]][1] + 5; # y-cordinaten pion speler 1
    kleur1 = (0,0,255) # blauwe pion
    pygame.draw.circle(screen, kleur1, (speler1_x, speler1_y), 10) # teken cirkel als pion speler 1
    speler2_x = vakjes[posities[2]][0] + 10; # x-cordinaten pion speler 2
    speler2_y = vakjes[posities[2]][1] + 10; # y-cordinaten pion speler 2
    kleur1 = (255,0,0) # rode pion
    pygame.draw.circle(screen, kleur1, (speler2_x, speler2_y), 10) # teken cirkel als pion speler 2

  

    # We tekenen wat tekst op het scherm
    # Kies het standaardfont en een lettergrootte (30):
    myfont = pygame.font.SysFont("None", 30)

    # Teken de laatste worp op het scherm:
    text = "Laatste worp: " + str(worp)
    label = myfont.render(text, 1, (0,0,0))
    screen.blit(label, (350,470))

    # Teken de speler die aan de beurt is op het scherm:
    text = "Aan de beurt: " + str(huidige_speler_beurt + 1)
    label = myfont.render(text, 1, (0,0,0))
    screen.blit(label, (350,495))

    # --- Update het beeldscherm met de nieuwe graphics ---

    clock.tick(60) # Zet de limiet op 60 frames per seconde
    pygame.display.flip() # ververs het beeldscherm met de nieuwe versie van het scherm
    # --- Update het  beeldscherm met de nieuwe graphics ---

    clock.tick(60) # Zet de limiet op 60 frames per seconde
    pygame.display.flip() # verwers het beeldscherm met de nieuwe versie van het scherm


# -------- Afsluiting --------
pygame.quit() #dit sluit pygame en sluit het gamevenster