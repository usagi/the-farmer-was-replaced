import(env)
import(params)
import(util)
import(usa_plant)
import(usa_harvest)
import(usa_move)

usa_plant.set_watring(params.watering)
usa_harvest.set_watring(params.watering)

while True:
 def was_reset(usa_move_result):
  return usa_move_result[1] < 0

 for entity_sequence_index in range(len(params.entity_sequence)):
  # 初期化
  clear()
  current_entity = params.entity_sequence[entity_sequence_index]
  usa_plant.set_entity(current_entity)
  usa_harvest.set_entity(current_entity)

  # 植える部
  harvest_candidates = []
  def plant_with_move():
   usa_plant.invoke()
   harvest_candidates.append(util.get_pos())
   return was_reset(usa_move.next())
  util.until(plant_with_move)

  # 刈る部
  while len(harvest_candidates) > 0:
   harvest_retries = []
   for index in range(len(harvest_candidates)):
    pos = harvest_candidates[index]
    usa_move.to(pos[0], pos[1])
    is_final_one = index == len(harvest_candidates) - 1
    is_final_one = is_final_one and len(harvest_retries) == 0
    if not usa_harvest.invoke(not is_final_one):
     harvest_retries.append(util.get_pos())
   harvest_candidates = harvest_retries
