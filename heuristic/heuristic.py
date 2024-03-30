def heuristic_function (get_stones, player1_points, player2_points):
    # Novērtē vai akmeņu skaits uz galda ir pāra vai nepāra
    stones = 0 if get_stones % 2 == 0 else 1

    # Starpība starp datora punktu skaitu un spēlētāju punktu skaitu
    points_diff = player1_points - player2_points

    # Hierātiskās novērtējuma funkcijas vērtība
    return stones + points_diff
