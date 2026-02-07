def includes(item, list):
 for _item in list:
  if _item == item:
   return True
 return False

def until(predicator):
 while not predicator():
  continue

def until_with(predicator, with):
 while not predicator():
  with()

def get_pos():
 return [get_pos_y(), get_pos_x()]
