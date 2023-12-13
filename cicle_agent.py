class Cicle_agent:
    next_move = -1

    @staticmethod
    def get_move(game):
        rps = __import__(game)
        Cicle_agent.next_move += 1
        return Cicle_agent.next_move % len(rps.GameAction)
