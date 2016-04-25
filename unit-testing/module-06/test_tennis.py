import pytest
from tennis import tennis_score

@pytest.mark.parametrize(("expected_score", "player1_points", "player2_points"),
                        [
                         ("Love-All", 0, 0),
                         ("Fifthteen-All", 1, 1),
                         ("Thirty-All", 2, 2),
                         ("Forty-All", 3, 3),                            
                        ])
def test_even_scores(expected_score, player1_points, player2_points):
    assert_tennis_score(expected_score, player1_points, player2_points)
    
@pytest.mark.parametrize(("expected_score", "player1_points", "player2_points"),
                    [
                     ("Fifthteen-Love",1,0),
                     ("Love-Fifthteen",0,1),
                     ("Love-Thirty",0,2),
                     ("Forty-Thirty",3,2),                            
                    ])
def test_early_games_with_uneven_scores(expected_score, player1_points, player2_points):
    assert_tennis_score(expected_score, player1_points, player2_points)
    
def assert_tennis_score(expected_score, player1_points, player2_points):
    assert expected_score == tennis_score(player1_points,player2_points)