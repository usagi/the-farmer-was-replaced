global entity
global watering

import(env)
import(util)
import(usa_move)

def set_entity(_entity):
 global entity
 entity = _entity

def set_watring(_watering):
 global watering
 watering = _watering

# only_simulate: 収穫可能な場合でも harvest() しない True/False
# return: 収穫成否 True/False
def invoke(only_simulate = False):
 global entity
 global watering

 # かぼちゃで収穫不能な場合は植え直して失敗を返す
 if entity == Entities.Pumpkin:
  if not can_harvest():
   plant(Entities.Pumpkin)
   return False
  if not only_simulate:
   harvest()
  return True

 # かぼちゃではない場合
 else:
  util.until_with(can_harvest, do_a_flip)
  harvest()
  return True
