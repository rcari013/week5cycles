from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    """A thing that is done.
    
    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """
    def __init__(self):
        self.counter = 0

    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        cycle = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        for actor in actors:
            actor.move_next()
        self.counter +=1
        if self.counter %10 == 0:
            cycle.grow_tail(1)
            cycle2.grow_tail(1)