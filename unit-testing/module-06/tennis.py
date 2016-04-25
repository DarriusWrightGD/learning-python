point_words = ["Love", "Fifthteen", "Thirty", "Forty"]

def tennis_score(player1_points, player2_points):
    if player1_points == player2_points:
        return "{0}-All".format(point_words[player1_points])
    else:
        return "{0}-{1}".format(point_words[player1_points], point_words[player2_points])