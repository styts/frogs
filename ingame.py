from dvizshok.appstate import AppState
import pygame


class InGame(AppState):
    def process_input(self, event):
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            self.next_state = ("GoodBye", None)

    def draw(self):
        tree = self.app.resman.get_surface("tree")
        self.app.screen.blit(tree, (10, 20))
        self.app.dirty(pygame.Rect(10, 20, 10, 20))
        pass
