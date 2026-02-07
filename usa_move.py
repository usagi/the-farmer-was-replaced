import(env)
global scaling
global next_is_east
scaling = 1.0
next_dx= -1

def set_scaling(_scaling):
 global scaling
 scaling = _scaling

def get_scaled_size_y():
 global scaling
 return scaling * env.size_y

def get_scaled_size_x():
 global scaling
 return scaling * env.size_x

def init(_scaling = 1.0):
 set_scaling(_scaling)
 y = 0
 x = get_scaled_size_x() // 2 - 1
 to(y, x)
 return 0 

def x(distance):
 if (distance > 0):
  direction(East, distance)
 elif (distance < 0):
  direction(West, -distance)

def y(distance):
 if (distance > 0):
  direction(North, distance)
 elif (distance < 0):
  direction(South, -distance)

def direction(_direction, distance):
 for _ in range(distance):
  move(_direction)

def reset_x():
 d = -get_pos_x()
 x(d)
 return d

def reset_y():
 d = -get_pos_y()
 y(d)
 return d
 
def reset():
 reset_y()
 reset_x()

def next():
 global next_dx
 next_x = get_pos_x() + next_dx
 next_y = get_pos_y()
 scaled_size_x_div2 = get_scaled_size_x() // 2
 
 # 左半面の場合
 if get_pos_x() < scaled_size_x_div2:
  if next_x < 0:
   next_x = 0
   next_y = next_y + 1
   next_dx = -next_dx
  elif next_x >= get_scaled_size_x() // 2 and next_y < get_scaled_size_y() - 1:
   next_x = scaled_size_x_div2 - 1
   next_y = next_y + 1
   next_dx = -next_dx

 # 右半面の場合
 else:
  if next_x >= get_scaled_size_x():
   next_x = get_scaled_size_x() - 1
   next_y = next_y - 1
   next_dx = -next_dx
  elif next_x <= get_scaled_size_x() // 2 - 1 and next_y != 0:
   next_x = scaled_size_x_div2
   next_y = next_y - 1
   next_dx = -next_dx
 # そして移動
 to(next_y, next_x)

def to(_y, _x):
 y(_y - get_pos_y())
 x(_x - get_pos_x())

def end():
 to(get_scaled_size_y() - 1, get_scaled_size_x() - 1)