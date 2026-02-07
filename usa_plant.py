# Global Variables
global entity_mode
global watering

# Local Variables
water_ground_max = 1.00
water_bucket_max = 0.25
water_delta = water_ground_max - water_bucket_max

import(util)

def set_entity_mode(_entity_mode):
 global entity_mode
 entity_mode = _entity_mode

def set_watring(_watering):
 global watering
 watering = _watering

def invoke():
 global entity_mode
 global watering
 
 if entity_mode == Entities.Tree:
  plant_chessboard(Entities.Tree, Entities.Bush)
 
 elif entity_mode == Entities.Carrot:
  plant_chessboard(Entities.Carrot, Entities.Tree)
 
 elif entity_mode == Entities.Pumpkin:
  plant_with_till(Entities.Pumpkin)
 
 elif entity_mode == Entities.Grass:
  plant_with_till(entity_mode)

 else:
  print("Warning: Unsupported `entity_mode`")
 
 if watering and get_water() < water_delta:
  use_item(Items.Water)

def till_for(entity):
 if util.includes(entity, [Entities.Carrot, Entities.Pumpkin]):
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
