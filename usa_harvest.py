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

 elif entity == Entities.Treasure:
  solve_maze()
  return True

 # その他の場合
 else:
  def _():
   return can_harvest() or get_entity_type() == None
  util.until_with(_, do_a_flip)
  harvest()
  return True

# Maze
# { (x, y): from }
#  from: North などどこから来たか
global map
global goal

def pos(dx = 0, dy = 0 ):
 return (get_pos_x() + dx, get_pos_y() + dy)

def forward():
 global map
 global is_forwarding
 p0_from = map[pos()]
 # 各方向へ"新規に"移動可能な場合
 if p0_from != North and not pos(0, 1) in map and move(North):
  map[pos()] = South
  return
 if p0_from != East and not pos(1, 0) in map and move(East):
  map[pos()] = West
  return
 if p0_from != South and not pos(0, -1) in map and move(South):
  map[pos()] = North
  return
 if p0_from != West and not pos(-1, 0) in map and move(West):
  map[pos()] = East
  return
 # 行き止まりだった場合
 move(p0_from)
      
def search():
 global goal
 dx = goal[0] - get_pos_x()
 dy = goal[1] - get_pos_y()
 if ( abs(dx) == 1 and abs(dy) == 0 ) or ( abs(dx) == 0 and abs(dy) == 1 ):
  usa_move.x(dx)
  usa_move.y(dy)
  if pos() == goal:
   harvest()
   return True
 return False

def solve_maze():
 global map
 global goal
 map = { (get_pos_x(), get_pos_y()):None }
 goal = measure()
 
 while not search():
  forward()
