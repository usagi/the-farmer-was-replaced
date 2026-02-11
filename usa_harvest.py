global entity
global watering

import(env)
import(util)

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

 # その他の場合
 else:
  def _():
   return can_harvest() or get_entity_type() == None
  util.until_with(_, do_a_flip)
  harvest()
  return True
