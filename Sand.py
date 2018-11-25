import pygame

pygame.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prosta gra")

window = pygame.display.get_surface()
window.fill((128, 128, 128))

rectangle = pygame.Surface((80, 20))
window.blit(rectangle, (100, 50))

pygame.display.flip()