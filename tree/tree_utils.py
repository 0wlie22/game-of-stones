def generateGameState(stones, player=1, player1_points=0, player2_points=0):
    # I will assume that I get no issues with this (I will)
    return player*10**8+player1_points*10**5+stones*10**3+player2_points

def getPlayerPoints(gameState, player): # Pirmā spēlētāja punktu skaits
    if player not in (1,2):
        raise ValueError("Invalid player number! (1 or 2)")
    if player == 1:
        return (gameState//10**5)%1000
    else:
        return gameState%1000

def getStones(gameState): # Atlikušo akmentiņu skaits
    return (gameState//10**3)%100

def getPlayer(gameState): # Spēlētāja kārtas Nr.
    return gameState//10**8

# === Taking ===

def takeStones(gameState, stoneCount): # Logic for taking two stones
    if stoneCount not in (2,3):
        raise ValueError("Invalid stone take ammount! (2 or 3)")
    stone_count = getStones(gameState)
    if stone_count < stoneCount: # Check if there are enough stones to take
        return 
    player = getPlayer(gameState)
    player1_points = getPlayerPoints(gameState, 1)
    player2_points = getPlayerPoints(gameState, 2)
    if player == 1: # If it's player 1's turn
        # Point arithmetic
        player1_points += stoneCount
        stone_count -= stoneCount
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player2_points += 2
        else:
            player1_points +=2
    else: # 2nd player's turn
        # Point arithmetic
        stone_count -= stoneCount
        player2_points += stoneCount
        # Rule about additional points depending on remaining stone count
        if stone_count % 2 == 0:
            player1_points += 2
        else:
            player2_points += 2
    next_player = (player%2)+1
    return generateGameState(stone_count, next_player, player1_points, player2_points)

def nextGameStates(gameState):
    result = [takeStones(gameState,2),takeStones(gameState,3)]
    filtered_result = [state for state in result if state is not None]
    return filtered_result
 
# === Undoing moves ===

def undo_takeStones(gameState, stoneCount):
    if stoneCount not in (2,3):
        raise ValueError("Invalid stone take ammount! (2 or 3)")
    # Value gathering
    player1_points = getPlayerPoints(gameState, 1) 
    player2_points = getPlayerPoints(gameState, 2) 
    player = getPlayer(gameState)
    stone_count = getStones(gameState)
    # If it is currently the 1st player's turn (means that previous was 2nd player)
    if player == 1:
        if stone_count % 2 == 0:
            player1_points -= 2
        else:
            player2_points -= 2
        player2_points -= stoneCount
        # Player points have to be positive values after returning them
        if player1_points >=0 and player2_points >=0:
            stone_count += stoneCount
    else: # 2nd player's turn
        if stone_count % 2 == 0:
            player2_points -= 2
        else:
            player1_points -= 2
        player1_points -= stoneCount
        # Pārbaude vai šāds stāvoklis var pastāvēt
        if player2_points >=0 and player1_points >=0:
            stone_count += stoneCount
    previous_player = (player%2)+1
    return generateGameState(stone_count, previous_player, player1_points, player2_points)

def previousStates(gameState, tree):
    result = [undo_takeStones(gameState, 2),undo_takeStones(gameState, 3)]
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