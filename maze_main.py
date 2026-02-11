import(usa_move)

# params
n = 8

# 生成
#clear()
#plant(Entities.Bush)
#use_item(Items.Weird_Substance, n * 2 ** (num_unlocked(Unlocks.Mazes) - 1))

# 探索
global map
map = {(get_pos_x(), get_pos_y()):0}
def mapping(_x, _y, _w):
 global map
 pos = (_x, _y)
 if pos in map:
  map[pos] = min(map[pos], _w)
 else:
  map[pos] = _w

def search():
 x = get_pos_x()
 y = get_pos_y()
 w = map[(x, y)]
 
 if can_move(North):
  mapping(x, y + 1, w + 1)
 if can_move(South):
  mapping(x, y - 1, w + 1)
 if can_move(East):
  mapping(x + 1, y, w + 1)
 if can_move(West):
  mapping(x - 1, y, w + 1)
      
search()
print("hoge")
