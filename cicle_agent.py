from RPS_dict import GameAction

class Cicle_agent:
    next_move = -1

    @staticmethod
    def get_move():
        Cicle_agent.next_move += 1
        return Cicle_agent.next_move % len(GameAction)
