import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.winner_indicator = 0
        self.for_cycle_2_winner = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:            
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        head = cycle.get_segments()[0]
        head2 = cycle2.get_segments()[0]
        segments = cycle.get_segments()[1:]
        segments2 = cycle2.get_segments()[1:]     

        if not self._is_game_over:
  
            for segment in segments:    
                if head.get_position().equals(segment.get_position()):  #cycle1 hits own body
                    self._is_game_over = True
                    cycle.kill()
                    cycle2.kill()
                    self.winner_indicator = 4                    
                if head2.get_position().equals(segment.get_position()): #cycle2 hits cycle1 body
                    self._is_game_over = True
                    cycle.kill()
                    cycle2.kill()
                    self.winner_indicator = 2
            for segment in segments2:
                if head2.get_position().equals(segment.get_position()): #cycle2 hits own body
                    self._is_game_over = True
                    cycle.kill()
                    cycle2.kill()
                    self.winner_indicator = 5
                if head.get_position().equals(segment.get_position()): #cycle1 hits cycle2 body
                    self._is_game_over = True
                    cycle.kill()
                    cycle2.kill()
                    self.winner_indicator = 3
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over and self.winner_indicator == 4:
            cycle = cast.get_first_actor("cycles")
            cycle2 = cast.get_second_actor("cycles")
            segments = cycle.get_segments()
            segments2 = cycle2.get_segments()
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)            

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Cycle Pink collided to itself! Cycle Blue wins!")
            message.set_position(position)
            message.set_color(constants.BLUE)
            cast.add_actor("messages", message)
        elif self._is_game_over and self.winner_indicator == 5:
            cycle = cast.get_first_actor("cycles")
            cycle2 = cast.get_second_actor("cycles")
            segments = cycle.get_segments()
            segments2 = cycle2.get_segments()
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)            

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Cycle Blue collided to itself. Cycle Pink wins!")
            message.set_position(position)
            message.set_color(constants.PINK)
            cast.add_actor("messages", message)
        elif self._is_game_over and self.winner_indicator == 2:
            cycle = cast.get_first_actor("cycles")
            cycle2 = cast.get_second_actor("cycles")
            segments = cycle.get_segments()
            segments2 = cycle2.get_segments()
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)            

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Cycle Pink wins!")
            message.set_position(position)
            message.set_color(constants.PINK)
            cast.add_actor("messages", message)
        elif self._is_game_over and self.winner_indicator == 3:
            cycle = cast.get_first_actor("cycles")
            cycle2 = cast.get_second_actor("cycles")
            segments = cycle.get_segments()
            segments2 = cycle2.get_segments()
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)            

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Cycle Blue wins!")
            message.set_position(position)
            message.set_color(constants.BLUE)
            cast.add_actor("messages", message)       

          