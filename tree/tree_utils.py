def generate_game_state(stones, player=1, player1_points=0, player2_points=0):
    # I will assume that I get no issues with this (I will)
    return player * 10**8 + player1_points * 10**5 + stones * 10**3 + player2_points


def get_player_points(gameState, player):  # Pirmā spēlētāja punktu skaits
    if player not in (1, 2):
        raise ValueError("Invalid player number! (1 or 2)")
    if player == 1:
        return (gameState // 10**5) % 1000
    else:
        return gameState % 1000


def get_stones(gameState):  # Atlikušo akmentiņu skaits
    return (gameState // 10**3) % 100


def get_player(gameState):  # Spēlētāja kārtas Nr.
    return gameState // 10**8


# === Taking ===


def take_stones(gameState, stoneCount):  # Logic for taking two stones
    if stoneCount not in (2, 3):
        raise ValueError("Invalid stone take ammount! (2 or 3)")
    stone_count = get_stones(gameState)
    if stone_count < stoneCount:  # Check if there are enough stones to take
        return
    player = get_player(gameState)
    player1_points = get_player_points(gameState, 1)
    player2_points = get_player_points(gameState, 2)
    if player == 1:  # If it's player 1's turn
        # Point arithmetic
        player1_points += stoneCount
        stone_count -= stoneCount
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player2_points += 2
        else:
            player1_points += 2
    else:  # 2nd player's turn
        # Point arithmetic
        stone_count -= stoneCount
        player2_points += stoneCount
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player1_points += 2
        else:
            player2_points += 2
    next_player = (player % 2) + 1
    return generate_game_state(stone_count, next_player, player1_points, player2_points)


def next_game_states(gameState):
    result = [take_stones(gameState, 2), take_stones(gameState, 3)]
    filtered_result = [state for state in result if state is not None]
    return filtered_result


# === Undoing moves ===


def undo_take_stones(gameState, stoneCount):
    if stoneCount not in (2, 3):
        raise ValueError("Invalid stone take ammount! (2 or 3)")
    # Value gathering
    player1_points = get_player_points(gameState, 1)
    player2_points = get_player_points(gameState, 2)
    player = get_player(gameState)
    stone_count = get_stones(gameState)
    # If it is currently the 1st player's turn
    if player == 1:
        if stone_count % 2 == 0:
            player1_points -= 2
        else:
            player2_points -= 2
        player2_points -= stoneCount
        # Player points have to be positive values after returning them
        if player1_points >= 0 and player2_points >= 0:
            stone_count += stoneCount
    else:  # 2nd player's turn
        if stone_count % 2 == 0:
            player2_points -= 2
        else:
            player1_points -= 2
        player1_points -= stoneCount
        # Pārbaude vai šāds stāvoklis var pastāvēt
        if player2_points >= 0 and player1_points >= 0:
            stone_count += stoneCount
    previous_player = (player % 2) + 1
    return generate_game_state(
        stone_count, previous_player, player1_points, player2_points
    )


def previous_states(gameState, tree):
    result = [undo_take_stones(gameState, 2), undo_take_stones(gameState, 3)]
    none_filtering = [state for state in result if state is not None]
    # Filtering
    if len(none_filtering) == 0:  # No previous states exist
        return []
    # Finding a match within a tree | NOTE: Have yet to find a case where a game state has 2 parents
    for level in tree:
        for item in none_filtering:
            if item in level:
                return list(set(none_filtering) & set(level))
    return []  # Failsafe


def generate_tree(startingGameState, height=-1):  # Generate tree
    # Initial starting value
    game_tree = [[startingGameState]]
    if height == -1:
        height = get_stones(startingGameState) // 2  # Maximum height calculation
    # Iterē pāri koka līmenim katram stāvoklim pievienojot nākamos stāvokļus
    for i in range(height):
        additional_level = []
        tree_level = game_tree[i]
        for gameState in tree_level:
            additional_level += next_game_states(gameState)
        # A failsafe
        if len(additional_level) == 0:
            break
        # Duplikātu dzēšana
        additional_level = list(set(additional_level))
        game_tree.append(additional_level)
    return game_tree
