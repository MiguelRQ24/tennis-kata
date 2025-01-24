class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        POINTS_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        if self.player1_points == self.player2_points:
            return {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}.get(self.player1_points, "Deuce")
        
        elif self.player1_points >= 4 or self.player2_points >= 4:
            diferential_ponits = self.player1_points - self.player2_points
            return {1: "Advantage player1", -1: "Advantage player2"}.get(diferential_ponits, "Win for player1" if diferential_ponits > 0 else "Win for player2")
        
        else:
            return POINTS_NAMES[self.player1_points] + '-' + POINTS_NAMES[self.player2_points]
        