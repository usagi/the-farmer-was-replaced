import(env)

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

def next(skip = 0):
 distance = skip + 1
 current = get_pos_y()
 if current + distance < env.size_y:
  y(distance)
  return [current + distance, 0]
 else:
  return next_line()

def next_line(skip = 0):
 dy = reset_y()
 distance = skip + 1
 current = get_pos_x()
 if current + distance < env.size_x:
  x(distance)
  return [dy, current + distance]
 else:
  dx = reset_x()
  return [dy, dx]

def to(_y, _x):
 y(_y - get_pos_y())
 x(_x - get_pos_x())

def end():
 to(env.size_y - 1, env.size_x - 1)