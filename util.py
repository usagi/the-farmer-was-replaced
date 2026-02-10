def len_all(list):
 _len = 0
 for list_in_list in list:
  _len = _len + len(list_in_list)
 return _len

def empty_all(list):
 for list_in_list in list:
  if len(list_in_list) > 0:
   return False
 return True

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
