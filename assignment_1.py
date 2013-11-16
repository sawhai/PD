'''
Simple PD game model.
'''

# Numpy imports
import numpy.random


class SimpleGame(object):
    '''
    Simple game class.
    This class is analogous to our Tournament object in the
    Rock-Paper-Scissors tournament.
    '''

    # Payoff matrix;
    payoff_matrix = [[(3, 3), (0, 5)],
                    [(5, 0), (1, 1)]]

    # Game history
    game_history = []

    def __init__(self, player_list):
        '''
        Constructor for the game; takes a list of players.

        You need to make sure that any variables, e.g., player_list,
        are made available to the class ongoing.
        '''
        pass

    def payoff(self, moves):
        '''
        Payoff method given a set of moves.

        This method needs to return the payoff value for a given
        pair of moves; you should use the payoff_matrix defined
        above.
        '''
        pass

    def run(self):
        '''
        Run method to run an actual game.

        You will need to do the following:
            1. Ask players for their moves
            2. Score the moves to determine their payoffs
            3. Update their scores
            4. Record their histories
        '''
        pass

class RandomPlayer(object):
    '''
    RandomPlayer class is a simple PD player who
    has a constant probability of defecting per game.
    '''

    # Default probability of defection
    probability_defect = 0.5

    # Score
    score = 0.0

    # History
    history = []

    def __init__(self, probability_defect):
        '''
        Constructor for the player; takes a probability
        of defection as input.

        You will need to set the class variable from the argument.
        '''
        pass

    def move(self):
        '''
        The move method returns the player's move based on a
        random draw and their constant probability.

        You will need to:
            1. Draw a random variate from numpy.random.random()
            2. Transform the value into an action
        '''
        pass

    def record(self, outcome, score):
        '''
        The record method allows the player to update their score
        and history values if desired.
        '''
        pass


if __name__ == "__main__":
    '''
    Sample driver.
    '''
    # Create players
    player_1 = RandomPlayer(0.5)
    player_2 = RandomPlayer(0.25)

    # Create game
    simple_game = SimpleGame([player_1, player_2])

    # Run the game
    result = simple_game.run()
    print result
