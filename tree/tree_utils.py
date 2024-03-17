def generateGameState(stones, player=1, player1_points=0, player2_points=0):
    # I will assume that I get no issues with this (I will)
    return player*10**8+player1_points*10**5+stones*10**3+player2_points

def getPlayer1Points(gameState): # Pirmā spēlētāja punktu skaits
    return (gameState//10**5)%1000

def getPlayer2Points(gameState): # Otrā spēlētāja punktu skaits
    return gameState%1000

def getStones(gameState): # Atlikušo akmentiņu skaits
    return (gameState//10**3)%100

def getPlayer(gameState): # Spēlētāja kārtas Nr.
    return gameState//10**8

# === Taking ===

def take2stones(gameState): # Logic for taking two stones
    stone_count = getStones(gameState)
    if stone_count < 2: # Check if there are enough stones to take
        return 
    player = getPlayer(gameState)
    if player == 1: # If it's player 1's turn
        # Point arithmetic
        player1_points = getPlayer1Points(gameState)+2
        stone_count -= 2
        player2_points = getPlayer2Points(gameState)
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player2_points += 2
        else:
            player1_points +=2
    else: # 2nd player's turn
        # Point arithmetic
        player1_points = getPlayer1Points(gameState)
        stone_count -= 2
        player2_points = getPlayer2Points(gameState)+2
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player1_points += 2
        else:
            player2_points += 2
    next_player = (player%2)+1
    return generateGameState(stone_count, next_player, player1_points, player2_points)

def take3stones(gameState): # Logic for taking two stones
    stone_count = getStones(gameState)
    if stone_count < 3: # Check if there are enough stones to take
        return
    player = getPlayer(gameState)
    if player == 1: # If it's player 1's turn
        # Point arithmetic
        player1_points = getPlayer1Points(gameState)+3
        stone_count -= 3
        player2_points = getPlayer2Points(gameState)
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player2_points += 2
        else:
            player1_points += 2
    else: # 2nd player's turn
        # Point arithmetic
        player1_points = getPlayer1Points(gameState)
        stone_count -= 3
        player2_points = getPlayer2Points(gameState)+3
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player1_points += 2
        else:
            player2_points += 2
    next_player = (player%2)+1
    return generateGameState(stone_count, next_player, player1_points, player2_points)

def nextGameStates(gameState):
    result = [take2stones(gameState),take3stones(gameState)]
    filtered_result = [state for state in result if state is not None]
    return filtered_result
 
# === Undoing moves ===

def undo_take2stones(gameState):
    # Value gathering
    player1_points = getPlayer1Points(gameState) 
    player2_points = getPlayer2Points(gameState) 
    player = getPlayer(gameState)
    stone_count = getStones(gameState)
    # If it is currently the 1st player's turn (means that previous was 2nd player)
    if player == 1:
        if stone_count % 2 == 0:
            player1_points -= 2
        else:
            player2_points -= 2
        player2_points -= 2
        # Player points have to be positive values after returning them
        if player1_points >=0 and player2_points >=0:
            stone_count += 2
    else: # 2nd player's turn
        if stone_count % 2 == 0:
            player2_points -= 2
        else:
            player1_points -= 2
        player1_points -= 2
        # Pārbaude vai šāds stāvoklis var pastāvēt
        if player2_points >=0 and player1_points >=0:
            stone_count += 2
    previous_player = (player%2)+1
    return generateGameState(stone_count, previous_player, player1_points, player2_points)

def undo_take3stones(gameState):
    # Value gathering
    player1_points = getPlayer1Points(gameState) 
    player2_points = getPlayer2Points(gameState) 
    player = getPlayer(gameState)
    stone_count = getStones(gameState)
    # If it is currently the 1st player's turn (means that previous was 2nd player)
    if player == 1:
        if stone_count % 2 == 0:
            player1_points -= 2
        else:
            player2_points -= 2
        player2_points -= 3
        # Player points have to be positive values after returning them
        if player1_points >=0 and player2_points >=0:
            stone_count += 3
    else: # 2nd player's turn
        if stone_count % 2 == 0:
            player2_points -= 2
        else:
            player1_points -= 2
        player1_points -= 3
        # Pārbaude vai šāds stāvoklis var pastāvēt
        if player2_points >=0 and player1_points >=0:
            stone_count += 3
    previous_player = (player%2)+1
    return generateGameState(stone_count, previous_player, player1_points, player2_points)

def previousStates(gameState, tree):
    result = [undo_take2stones(gameState),undo_take3stones(gameState)]
    none_filtering = [state for state in result if state is not None]
    # Filtering
    if len(none_filtering)==0: # No previous states exist
        return []
    # Finding a match within a tree | NOTE: Have yet to find a case where a game state has 2 parents
    for level in tree:
        for item in none_filtering:
            if item in level:
                return list(set(none_filtering) & set(level))
    return [] # Failsafe

def generateTree(startingGameState, height=-1): # Generate tree
    # Initial starting value
    game_tree=[[startingGameState]]
    if height == -1:
        height = getStones(startingGameState)//2 # Maximum height calculation
    # Iterē pāri koka līmenim katram stāvoklim pievienojot nākamos stāvokļus
    for i in range(height):
        additional_level = []
        tree_level = game_tree[i]
        for gameState in tree_level:
            additional_level += nextGameStates(gameState)
        # A failsafe
        if (len(additional_level) == 0):
            break
        # Duplikātu dzēšana
        additional_level = list(set(additional_level))
        game_tree.append(additional_level)
    return game_tree