import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from chatbot.bot_agent import get_bot_response

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Whispers of the Ancients")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 20)

input_text = ""
chat_log = []

def draw_chat_ui():
    # Draw background
    pygame.draw.rect(screen, (0, 0, 0), (0, 450, 800, 150))
    pygame.draw.rect(screen, (255, 255, 255), (5, 455, 790, 30))  # Input box

    # Draw input text
    input_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(input_surface, (10, 460))

    # Draw last few chat log messages
    for i, msg in enumerate(chat_log[-5:]):
        msg_surface = font.render(msg, True, (255, 255, 255))
        screen.blit(msg_surface, (10, 495 + i * 20))

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.strip():
                    chat_log.append(f"You: {input_text}")
                    try:
                        response = get_bot_response(input_text)
                    except Exception as e:
                        response = "Error contacting the chatbot."
                    chat_log.append(f"Bot: {response}")
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    draw_chat_ui()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
