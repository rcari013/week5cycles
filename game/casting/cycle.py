from pickle import FALSE, TRUE
import constants
from game.casting.actor import Actor
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself while growing gradually.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, _index):
        super().__init__()
        self._segments = []
        self._index = _index #This index is used to set the cycle's starting position and color
        self._prepare_body()
        self._is_dead = FALSE
        
        

    def kill(self):
        self._is_dead = TRUE

    def get_segments(self):
        return self._segments

    def move_next(self):
        # moving the body
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("O")
            if self._is_dead == TRUE:
                segment.set_color(constants.WHITE)

            else:
                if self._index == 2:
                    segment.set_color(constants.BLUE)
                else:
                    segment.set_color(constants.PINK)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)        
    
    def _prepare_body(self):
        x = int(constants.MAX_X / self._index)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "#" if i == 0 else "O"
            if self._index == 2:
                color = constants.YELLOW if i == 0 else constants.BLUE
            else:
                color = constants.YELLOW if i == 0 else constants.PINK
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)