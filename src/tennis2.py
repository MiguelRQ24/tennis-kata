class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.__player1_score()
        else:
            self.__player2_score()

    def score(self):
       
        
        if abs(self.p1points - self.p2points) > 1 and max(self.p1points, self.p2points) > 3:
            return "Win for " + (self.player1_name if self.p1points > self.p2points else self.player2_name)
        elif abs(self.p1points - self.p2points) == 1 and max(self.p1points, self.p2points) > 3:
            return "Advantage " + (self.player1_name if self.p1points > self.p2points else self.player2_name)
        elif self.p1points == self.p2points and self.p1points > 2:
            return "Deuce"
        else:
            players_points = []
            for player_points in [self.p1points, self.p2points]:
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
        self.p1points += 1

    def __player2_score(self):
        self.p2points += 1
