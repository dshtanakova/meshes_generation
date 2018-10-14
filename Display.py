import pygame


class Display():

    def __init__(self):
        self.w = 300
        self.h = 300
        scl = 10
        self.cols = self.w / scl
        self.rows = self.h / scl

    # def generate(self):

        # for x in range(self.cols):
        #     for y in range(self.rows):



    def run(self):
        # pygame.init()
        pygame.display.set_caption('Generation')
        width = 300
        height = 200
        screen = pygame.display.set_mode((width, height))

        running = True


        while running:
            screen.fill((255, 255, 255))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
         # self.generate()

        pygame.draw.circle(screen, (0, 0, 255), (150, 50), 15, 1)


display = Display()
display.run()