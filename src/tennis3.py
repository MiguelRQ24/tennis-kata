class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, name):
        if name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if (self.player1_points < 4 and self.player2_points < 4) and (self.player1_points + self.player2_points < 6):
            posible_results = ["Love", "Fifteen", "Thirty", "Forty"]
            player1_result = posible_results[self.player1_points]
            return player1_result + "-All" if (self.player1_points == self.player2_points) else player1_result + "-" + posible_results[self.player2_points]
        else:
            if self.player1_points == self.player2_points:
                return "Deuce"
            more_points_player = self.player1_name if self.player1_points > self.player2_points else self.player2_name
            return (
                "Advantage " + more_points_player
                if ((self.player1_points - self.player2_points) * (self.player1_points - self.player2_points) == 1)
                else "Win for " + more_points_player
            )
