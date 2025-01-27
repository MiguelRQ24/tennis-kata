class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.__player1_score()
        else:
            self.__player2_score()

    def score(self):
       
        
        if abs(self.player1_points - self.player2_points) > 1 and max(self.player1_points, self.player2_points) > 3:
            return "Win for " + (self.player1_name if self.player1_points > self.player2_points else self.player2_name)
        
        elif abs(self.player1_points - self.player2_points) == 1 and max(self.player1_points, self.player2_points) > 3:
            return "Advantage " + (self.player1_name if self.player1_points > self.player2_points else self.player2_name)
        
        elif self.player1_points == self.player2_points and self.player1_points > 2:
            return "Deuce"
        
        else:
            players_points = []
            for player_points in [self.player1_points, self.player2_points]:
                if player_points == 0:
                    players_points.append("Love")
                elif player_points == 1:
                    players_points.append("Fifteen")
                elif player_points == 2:
                    players_points.append("Thirty")
                elif player_points == 3:
                    players_points.append("Forty")
            return "-".join(players_points) if len(set(players_points)) == 2 else players_points[0] + "-All"

    def set_p1_score(self, number):
        for i in range(number):
           self.__player1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.__player2_score()

    def __player1_score(self):
        self.player1_points += 1

    def __player2_score(self):
        self.player2_points += 1
