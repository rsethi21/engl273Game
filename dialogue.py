import pygame


def speech_bubble(WIN, text, pos):
    # creating bubble
    pygame.font.init()  # initialize font methods
    speech_font = pygame.font.SysFont("comicsans", 20)  # initialize font style
    speech = speech_font.render(text, True, (255, 255, 255))  # create text
    text_wrap = speech.get_rect(midbottom=pos)  # organize text as rect.
    text_bubble = text_wrap.copy()  # create background text bubble
    text_bubble.inflate_ip(10, 10)  # make the bubble bigger
    frame = text_bubble.copy()  # create a bordering frame
    frame.inflate_ip(4, 4)  # enlarge bordering frame

    # draw
    pygame.draw.rect(WIN, (255, 255, 255), frame)  # draw frame
    pygame.draw.rect(WIN, text_bubble, (0, 0, 0))  # superimpose box
    WIN.blit(speech, text_wrap)  # input text into box
