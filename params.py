# 実行パラメーター定数群
SEQUENCE_INDEX_ENTITY = 0
SEQUENCE_INDEX_SIZE = 1
SEQUENCE_INDEX_WATER = 2
SEQUENCE_INDEX_FERTILIZER = 3
SEQUENCE_INDEX_REPEAT = 4
sequence = [
 [Entities.Grass    , 4, True, True , 1],
 [Entities.Tree     , 4, True, True , 1],
 [Entities.Carrot   , 6, True, False, 1],
 [Entities.Sunflower, 4, True, False, 1],
 [Entities.Pumpkin  , 6, True, False, 1],
 [Entities.Cactus   , 5, True, True , 1]
]
entity_sequence = [Entities.Grass, Entities.Tree, Entities.Carrot, Entities.Sunflower, Entities.Pumpkin, Entities.Cactus]
scaling_sequence = [0, 7/32, 5/32, 5/32, 6/32, 5/32]
#entity_sequence = [Entities.Cactus]
#scaling_sequence = [3/32]
watering = True
fertilizer = False
