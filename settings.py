#-------------------------------------------------------------------------------------------------
# Rules for creating level maps
#
#  X: tile
#  B: Banker player
#  J: Janitor player
#  E: enemy, specify the distance it travels and its speed
#  F: Janitor item
#  G: Banker item
#  L: Lever, specify id     **not implmented yet**
#  O: Obstacle, specify id  **id not implemented yet**
#  C: Point obstacle
#  N: Janitor exit
#  M: Banker exit
#
#
# Rules for parameters
#
#  - put parameters in order of which the entity appears in the map (left to right, top to bottom)
#  - level_param is a 2d array, each subarray contains the parameters for one entity
# -----------------------------------------------------------------------------------------------


level_map_test = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X     C                    X',
'X     X       C   N  M     X',
'X C    XXXXXXXXXXXXXXXXXXXXX',
'XXXXX   X                  X',
'XXXXX      XXXXXX          X',
'XXXXXXXXXXXXXXXXXXXXXX     X',
'X     O                    X',
'X    XXXXXXXXXXX  C        X',
'X              XXXXXXXXXXXXX',
'XL      E                  X',
'XXXXXXXXXXXXXX             X',
'X  B         XXXXXXXXXX    X',
'XXXXXXXXXXX     C   C    XXX',
'X  J      F   G            X',
'XXXXXXXXXXXWWXXXWWWWXXXXXXXX']
leveltest_param = [[1], [1], [350, 2]]

level_map_test_gravity = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X     C                    X',
'X     X       C   N  M     X',
'X C    XXXXXXXXXXXXXXXXXXXXX',
'XXXXX   X                  X',
'XXXXX      XXXXXX          X',
'XXXXXXXXXXXXXXXXXXXXXX     X',
'X     O                    X',
'X    XXXXXXXXXXX  C        X',
'X              XXXXXXXXXXXXX',
'XL      E                  X',
'XXXXXXXXXXXXXX             X',
'X  B    J   F   G XXXXX    X',
'X               C   C    XXX',
'X                          X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']


level_map = [
'                            ',
'                            ',
' F     C N                  ',
' XX    XXX            XX    ',
' XXBX          M            ',
' XXXX         XX         XX ',
' XXXX  GE     XX            ',
' XX    XXXXXXXX   XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']
level_param = [[225, 2]]


level_map_0 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X     C                    X',
'X     X       C     N  M   X',
'X C    XXXXXXXXXXXXXXXXXXXXX',
'XXXXX   X                  X',
'XXXXX      XXXXXX          X',
'XXXXXXXXXXXXXXXXXXXXXX     X',
'X        C                 X',
'X    XXXXXXXXXXX  C        X',
'X              XXXXXXXXXXXXX',
'X   E  G                   X',
'XXXXXXXXXXXXXX             X',
'X  B         XXXXXXXXXX    X',
'XXXXXXXXXXX     C   C    XXX',
'X  J                       X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level0_param = [[350, 2]]

level_map_1 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X     C                    X',
'X     X       C     N  M   X',
'X C    XXXXXXXXXXXXXXXXXXXXX',
'XXXXX   X                  X',
'XXXXX      XXXXXX          X',
'XXXXXXXXXXXXXXXXXXXXXX     X',
'X        C                 X',
'X    XXXXXXXXXXX  C        X',
'X              XXXXXXXXXXXXX',
'X   E  G                   X',
'XXXXXXXXXXXXXX             X',
'X  B         XXXXXXXXXX    X',
'XXXXXXXXXXX     C   C    XXX',
'X   J                      X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level1_param = [[350, 2]]



level_map_2 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XX          NM    XXXXXXXXXX',
'XXX         XXX    XXXXXXXXX',
'XXXX          X     XXXXXXXX',
'XXXX B        X      XXXXXXX',
'XXXXXX       XXX      XXXXXX',
'XXXXXXX X              XXXXX',
'XXXXXXX X                XXXX',
'XXXXXXXXX                XXX',
'XXXXXXXXXX                XX',
'XXXXXXXXXXX                X',
'XXXXXXXXXXXX   E           X',
'XXXXXXXXXXXXX              X',
'XXXXXXXXXXXXXX             X',
'XXXXXXXXXXXXXXX            X',
'XXXXXXXXXXXXXXXX           X']
level2_param = [[335, 2]]

<<<<<<< Updated upstream
=======
level_map_3 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                         BX',
'X         C           C   XX',
'X  X  X   X   X   X   X  XXX',
'X XXWWWWWWWWWWWWWWWWWWWWWXXX',
'X                          X',
'X                  N   M   X',
'X XXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                          X',
'XX                  C      X',
'XXX                  X     X',
'XXXXX E  C  X E CX ECX     X',
'XXXXXXXXXXXXXXXXXXXXXXXXXX X',
'X                          X',
'X  J                    XXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level3_param=[[100,2],[80,2], [35,3]]


level_map_4 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                          X',
<<<<<<< Updated upstream
'X NM O       X             X',
'XXXXXXX      X             X',
'X     X      X             X',
'X    FX      XZ            X',
'X   XXX XXX  XXXX          X',
'X     X      JXBO          X',
=======
'X NM O                    LX',
'XXXXXXXXXXXXXXXXXXWWWWWWW  X',
'X     X                    X',
'X    FX                    X',
'X   XXX                    X',
'X     X       XXX          X',
'X     X       JXBO         X',
>>>>>>> Stashed changes
'X     X  XXXXXXXXG         X',
'X    LX         XX         X',
'X     X          XX        X',
<<<<<<< Updated upstream
'X     X           XX       X',
'XZ                 XX      X',
'X                   XX    LX',
'X                          X',
'XXXXXXXXXXXXXXXWWWWWWWWWWWWX']

level4_param = [[2], [3, 2], [1], [1], [6, 2], [2]]
=======
'X                 XX       X',
'XZ                 XX      X',
'XL                       Z X',
'XXXXXXXXXXXXXXXWWWWWWWWWWWWX']

level4_param = [[1], [1], [2], [6, 2], [2], [11, 4]]

>>>>>>> Stashed changes


>>>>>>> Stashed changes
#11 rows
# tile_size = 64
# screen_width = 1280
# screen_height = len(level_map) * tile_size
