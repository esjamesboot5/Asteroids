import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from pshot import Shot
import sys


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    dt = 0
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)

    Asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        #Limit the timeframe to 60 fps
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()




if __name__ == "__main__":
    main()
