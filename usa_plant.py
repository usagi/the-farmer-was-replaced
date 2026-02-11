# Global Variables
global entity
global size
global watering
global fertilizer

# Local Variables
water_ground_max = 1.00
water_bucket_max = 0.25
water_delta = water_ground_max - water_bucket_max

import(util)
import(usa_move)

def set_entity(_entity):
 global entity
 entity = _entity

def set_size(_size):
 global size
 size = _size

def set_watring(_watering):
 global watering
 watering = _watering

def set_fertilizer(_fertilizer):
 global fertilizer
 fertilizer = _fertilizer

def invoke():
 global entity
 global size
 global watering
 global fertilizer

 if entity == Entities.Tree:
  plant_chessboard(Entities.Tree, Entities.Bush)

 elif entity == Entities.Carrot:
  plant_with_till(Entities.Carrot)

 elif entity == Entities.Pumpkin:
  plant_with_till(Entities.Pumpkin)
  
 elif entity == Entities.Cactus:
  plant_with_till(Entities.Cactus)
  
 elif entity == Entities.Sunflower:
  plant_with_till(Entities.Sunflower)

 elif entity == Entities.Grass:
  if get_entity_type() != Entities.Grass:
    plant_with_till(entity)
  harvest()
  
 elif entity == Entities.Treasure:
  usa_move.to(0, 0)
  plant_with_till(Entities.Bush)
  use_item(Items.Weird_Substance, size ** (num_unlocked(Unlocks.Mazes) - 1))

 else:
  print("Warning: Unsupported `entity`")

 if watering and get_water() < water_delta:
  use_item(Items.Water)
 if fertilizer:
  use_item(Items.Fertilizer)

def till_for(entity):
 soils = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
 if util.includes(entity, soils):
  if get_ground_type() == Grounds.Grassland:
   till()
 elif get_ground_type() == Grounds.Soil:
  till()

def plant_with_till(entity):
 till_for(entity)
 if can_harvest() and entity != Entities.Pumpkin:
   harvest()
 plant(entity)

def plant_chessboard(p1, p2):
 is_p1 = get_pos_y() % 2 == 0
 if get_pos_x() % 2 != 0:
  is_p1 = not is_p1
 if is_p1 and p1 != False:
  plant_with_till(p1)
 elif p2 != False:
  plant_with_till(p2)

def ground_to(ground):
 if ground != get_ground_type():
  till()
