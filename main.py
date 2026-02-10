import(env)
import(params)
import(util)
import(usa_plant)
import(usa_harvest)
import(usa_move)

usa_plant.set_watring(params.watering)
usa_harvest.set_watring(params.watering)

while True:
 if len(params.entity_sequence) != len(params.scaling_sequence):
  print("Error: dirrerent size of `params.entity_sequence` and `params.scaling_sequence`.")
  break

 for entity_sequence_index in range(len(params.entity_sequence)):
  # 初期化
  # clear()
  current_entity = params.entity_sequence[entity_sequence_index]
  usa_plant.set_entity(current_entity)
  usa_harvest.set_entity(current_entity)
  current_scaling = params.scaling_sequence[entity_sequence_index]
  if current_entity == Entities.Grass:
   clear()  
  if current_scaling * get_world_size() < 1:
   continue
  usa_move.init(params.scaling_sequence[entity_sequence_index])
       
  # 植える部
  # bucket sort without dictionary indexing cost
  # [ [priority=15], [priority=14], [priority=13], .. [priority=7] ]
  harvest_candidates = [ [], [], [], [], [], [], [], [], [] ]
  harvest_candidates_index_offset = 7
  harvest_candidates_index_top = 15
  def plant_with_move():
   usa_plant.invoke()
   if get_entity_type() == Entities.Sunflower:
    priority = measure()
   else:
    priority = harvest_candidates_index_top
   index = harvest_candidates_index_top - priority 
   harvest_candidates[index].append(util.get_pos())
   usa_move.next()
   return get_pos_y() == 0 and get_pos_x() == usa_move.get_scaled_size_x() // 2 - 1
  if current_entity == Entities.Grass:
   clear()
  util.until(plant_with_move)

  # 刈る部
  num_harvest_required = util.len_all(harvest_candidates)
  while not util.empty_all(harvest_candidates):
   harvest_retries = [ [], [], [], [], [], [], [], [], [] ]
   for prioritied_candidates in harvest_candidates:
    for pos in prioritied_candidates:
     usa_move.to(pos[0], pos[1])
     only_simulate = current_entity == Entities.Pumpkin and num_harvest_required > 1
     #if not only_simulate and current_entity == Entities.Pumpkin:
     # do_a_flip()
     if usa_harvest.invoke(only_simulate):
      num_harvest_required = num_harvest_required - 1
     else:
      harvest_retries[0].append(util.get_pos())
   harvest_candidates = harvest_retries
