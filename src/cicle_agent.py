# This is a class that returns each possible game action in order
class Cicle_agent:
    next_move = -1

    @staticmethod
    def get_move(game):
        rps = __import__(game + '_dict')
        Cicle_agent.next_move += 1
        return Cicle_agent.next_move % len(rps.GameAction)
