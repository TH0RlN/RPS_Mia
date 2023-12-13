import pytest
from src.RPSLS_dict import Game, GameResult, GameAction


@pytest.fixture
def game():
    '''
    Setup del objeto game
    '''
    setup_game = Game()
    return setup_game


@pytest.mark.draw
def test_draw(game):

    assert GameResult.Tie == game.assess_game(
        player1=GameAction.Spock,
        player2=GameAction.Spock)

    assert GameResult.Tie == game.assess_game(
        player1=GameAction.Lizard,
        player2=GameAction.Lizard)

    assert GameResult.Tie == game.assess_game(
        player1=GameAction.Rock,
        player2=GameAction.Rock)

    assert GameResult.Tie == game.assess_game(
        player1=GameAction.Scissors,
        player2=GameAction.Scissors)

    assert GameResult.Tie == game.assess_game(
        player1=GameAction.Paper,
        player2=GameAction.Paper)


@pytest.mark.spock
def test_spock_loses(game):
    '''
    Spock pierde con Lizard y Paper 
    '''
    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Paper,
        player2=GameAction.Spock)

    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Lizard,
        player2=GameAction.Spock)


@pytest.mark.spock
def test_spock_wins(game):
    '''
    Spock gana a Rock y Scissors 
    '''
    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Rock,
        player2=GameAction.Spock)

    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Scissors,
        player2=GameAction.Spock)


@pytest.mark.lizard
def test_lizard_loses(game):
    '''
    Lizard pierde con Rock y Scissors 
    '''
    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Rock,
        player2=GameAction.Lizard)

    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Scissors,
        player2=GameAction.Lizard)


@pytest.mark.lizard
def test_lizard_wins(game):
    '''
    Lizard gana a Spock y Paper 
    '''
    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Spock,
        player2=GameAction.Lizard)

    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Paper,
        player2=GameAction.Lizard)


@pytest.mark.rock
def test_rock_loses(game):
    '''
    Rock pierde con Spock y Paper 
    '''
    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Spock,
        player2=GameAction.Rock)

    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Paper,
        player2=GameAction.Rock)


@pytest.mark.rock
def test_rock_wins(game):
    '''
    Rock gana a Scissors y Lizard 
    '''
    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Scissors,
        player2=GameAction.Rock)

    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Lizard,
        player2=GameAction.Rock)


@pytest.mark.paper
def test_paper_loses(game):
    '''
    Paper pierde con Scissors y Lizard 
    '''
    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Scissors,
        player2=GameAction.Paper)

    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Lizard,
        player2=GameAction.Paper)


@pytest.mark.paper
def test_paper_wins(game):
    '''
    Paper gana a Rock y Spock 
    '''
    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Rock,
        player2=GameAction.Paper)

    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Spock,
        player2=GameAction.Paper)


@pytest.mark.scissors
def test_scissors_loses(game):
    '''
    Scissors pierde con Spock y Rock 
    '''
    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Spock,
        player2=GameAction.Scissors)

    assert GameResult.Victory == game.assess_game(
        player1=GameAction.Rock,
        player2=GameAction.Scissors)


@pytest.mark.scissors
def test_scissors_wins(game):
    '''
    Scissors gana a Lizard y Paper 
    '''
    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Lizard,
        player2=GameAction.Scissors)

    assert GameResult.Defeat == game.assess_game(
        player1=GameAction.Paper,
        player2=GameAction.Scissors)


@pytest.mark.actions
def test_minus_action():
    '''
    GameActions EnumType behaviour
    '''
    assert 1 == len(GameAction.minus(
        GameAction.Scissors,
        GameAction.Lizard,
        GameAction.Paper,
        GameAction.Rock))

    assert 4 == len(GameAction.minus(GameAction.Lizard))

    assert GameAction.Lizard not in GameAction.minus(GameAction.Lizard)

    assert GameAction.Lizard in GameAction.minus(GameAction.Spock, GameAction.Rock)
