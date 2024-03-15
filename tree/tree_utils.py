def generateGameState(stones, player=1, player1_points=0, player2_points=0):
    # I will assume that I get no issues with this (I will)
    return player*10**8+player1_points*10**5+stones*10**3+player2_points

def nextGameStates(gameState):
    # Data innit
    result_arr = []                             # Rezultātu masīvs
    player1_points = (gameState//10**5)%1000    # Pirmā spēlētāja punktu skaits
    points_toGrab = (gameState//10**3)%100      # Atlikušo akmentiņu skaits
    player2_points = gameState%1000             # Otrā spēlētāja punktu skaits
    player = gameState//10**8                   # Spēlētāja kārtas Nr.

    # Ja ir pirmā spēlētāja kārta
    if player == 1:
        # Gadījums, ja paņem 2
        # Pārbaude vai var paņemt 2
        if points_toGrab >= 2:
            # Punktu manipulācijas
            player1_points_t2 = player1_points+2
            points_toGrab_t2 = points_toGrab-2
            player2_points_t2 = player2_points
            # Punkti par pāra/nepāra skaita atlikumu
            if points_toGrab_t2 % 2 == 0:
                player2_points_t2 = player2_points_t2+2
            else:
                player1_points_t2 = player1_points+2
            # Rezultātu pierakstīšana        
            result_arr.append(generateGameState(points_toGrab_t2,2,player1_points_t2,player2_points_t2))

        # Gadījums ja paņem 3
        # Pārbaude vai var paņemt 3
        if points_toGrab >= 3:
            # Punktu manipulācijas
            player1_points_t3 = player1_points+3
            points_toGrab_t3 = points_toGrab-3
            player2_points_t3 = player2_points
            # Punkti par pāra/nepāra skaita atlikumu
            if points_toGrab_t3 % 2 == 0:
                player2_points_t3 = player2_points_t3+2
            else:
                player1_points_t3 = player1_points_t3+2
            # Rezultātu pierakstīšana
            result_arr.append(generateGameState(points_toGrab_t3,2,player1_points_t3,player2_points_t3))
    # Ja bija otrā spēlētāja kārta (nav paredzēts ka spēlē 3 cilvēki)
    else:
        # Gadījums ja paņem 2
        # Pārbaude vai var paņemt 2
        if points_toGrab >= 2:
            # Punktu manipulācijas
            player1_points_t2 = player1_points
            points_toGrab_t2 = points_toGrab-2
            player2_points_t2 = player2_points+2
            # Punkti par pāra/nepāra skaita atlikumu
            if points_toGrab_t2 % 2 == 0:
                player1_points_t2 = player1_points_t2+2
            else:
                player2_points_t2 = player2_points_t2+2
            # Rezultātu pierakstīšana
            result_arr.append(generateGameState(points_toGrab_t2,1,player1_points_t2,player2_points_t2))

        # Gadījums ja paņem 3
        # Pārbaude vai var paņemt 3
        if points_toGrab >= 3:
            # Punktu manipulācijas
            player1_points_t3 = player1_points
            points_toGrab_t3 = points_toGrab-3
            player2_points_t3 = player2_points+3
            # Punkti par pāra/nepāra skaita atlikumu
            if points_toGrab_t3 % 2 == 0:
                player1_points_t3 = player1_points_t3+2
            else:
                player2_points_t3 = player2_points_t3+2
            # Rezultātu pierakstīšana
            result_arr.append(generateGameState(points_toGrab_t3,1,player1_points_t3,player2_points_t3))
    # Rezultātu izvade
    return result_arr
 
def previousStates(gameState, tree):            # Inverse of nextGameStates
    theoretical_arr = []                        # Rezultātu masīvs
    player1_points = (gameState//10**5)%1000    # Pirmā spēlētāja punktu skaits
    points_toGrab = (gameState//10**3)%100      # Atlikušo akmentiņu skaits
    player2_points = gameState%1000             # Otrā spēlētāja punktu skaits
    player = gameState//10**8                   # Spēlētāja kārta
    # Ja ir pirmā spēlētāja kārta
    if player == 1:
        # Tika paņemti 2 akmentiņi
        # Punktu manipulācija
        player1_points_t2 = player1_points
        points_toGrab_t2 = points_toGrab
        player2_points_t2 = player2_points
        if points_toGrab % 2 == 0:
            player1_points_t2 -= 2
        else:
            player2_points_t2 -= 2
        player2_points_t2 -= 2
        if player2_points_t2 >=0 and player1_points_t2 >=0:
            points_toGrab_t2 += 2
            theoretical_arr.append(generateGameState(points_toGrab_t2,2,player1_points_t2,player2_points_t2))
        
        # Tika paņemti 3 akmentiņi
        player1_points_t3 = player1_points
        points_toGrab_t3 = points_toGrab
        player2_points_t3 = player2_points
        if points_toGrab % 2 == 0:
            player1_points_t3 -= 2
        else:
            player2_points_t3 -= 2
        player2_points_t3 -= 3
        # Pārbaude vai šāds stāvoklis var pastāvēt
        if player2_points_t3 >=0 and player1_points_t3 >=0:
            points_toGrab_t3 += 3
            theoretical_arr.append(generateGameState(points_toGrab_t3,2,player1_points_t3,player2_points_t3))

    # Ja tagad ir otrā spēlētāja kārta
    if player == 2:
        # Tika paņemti 2 akmentiņi
        # Punktu manipulācijas
        player1_points_t2 = player1_points
        points_toGrab_t2 = points_toGrab
        player2_points_t2 = player2_points
        if points_toGrab % 2 == 0:
            player2_points_t2 -= 2
        else:
            player1_points_t2 -= 2
        player1_points_t2 -= 2
        # Pārbaude vai šāds stāvoklis var pastāvēt
        if player2_points_t2 >=0 and player1_points_t2 >=0:
            points_toGrab_t2 += 2
            theoretical_arr.append(generateGameState(points_toGrab_t2,1,player1_points_t2,player2_points_t2))

        # Tika paņemti 3 akmentiņi
        player1_points_t3 = player1_points
        points_toGrab_t3 = points_toGrab
        player2_points_t3 = player2_points
        if points_toGrab % 2 == 0:
            player2_points_t3 -= 2
        else:
            player1_points_t3 -= 2
        player1_points_t3 -= 3
        if player2_points_t3 >=0 and player1_points_t3 >=0:
            points_toGrab_t3 += 3
            theoretical_arr.append(generateGameState(points_toGrab_t3,1,player1_points_t3,player2_points_t3))
        
    # Filtering
    # No previous states exist
    if len(theoretical_arr)==0:
        return []
    # NOTE: I've yet to think and find a possibility
    #       where a child has 2 parent nodes
    #       but I am accounting for an edge case.
    for level in tree:
        for item in theoretical_arr:
            if item in level:
                return list(set(theoretical_arr) & set(level))
            
    return [] # Also expecting edge case.

def generateTree(startingGameState, height=-1): # Generate tree
    # Initial starting value
    game_tree=[[startingGameState]]
    if height == -1:
        startingStones = (startingGameState//10**3)%100
        height=startingStones//2                # Maximum height calculation
    # Iterē pāri koka līmenim katram stāvoklim pievienojot nākamos stāvokļus
    for i in range(height):
        additional_level = []
        tree_level = game_tree[i]
        for gameState in tree_level:
            additional_level += nextGameStates(gameState)
        # Duplikātu dzēšana
        additional_level = list(set(additional_level))
        # Ja viss padarīts, tad var neko tālāk nedarīt
        if (len(additional_level) == 0):
            break
        game_tree.append(additional_level)
    return game_tree