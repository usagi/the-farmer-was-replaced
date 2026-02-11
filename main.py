import(env)
import(params)
import(util)
import(usa_plant)
import(usa_harvest)
import(usa_move)

while True:
 for sequence_index in range(len(params.sequence)):
  # 初期化
  # clear()
  current_sequence = params.sequence[sequence_index]
  current_entity = current_sequence[params.SEQUENCE_INDEX_ENTITY]
  usa_plant.set_entity(current_entity)
  usa_plant.set_size(current_sequence[params.SEQUENCE_INDEX_SIZE])
  usa_plant.set_watring(current_sequence[params.SEQUENCE_INDEX_WATER])
  usa_plant.set_fertilizer(current_sequence[params.SEQUENCE_INDEX_FERTILIZER])
  usa_harvest.set_entity(current_entity)
  usa_harvest.set_watring(current_sequence[params.SEQUENCE_INDEX_WATER])
  current_size = current_sequence[params.SEQUENCE_INDEX_SIZE]
  if current_entity == Entities.Grass:
   clear()
  if current_size < 1:
   continue
  usa_move.init(current_sequence[params.SEQUENCE_INDEX_SIZE])

  # 植える部
  # bucket sort without dictionary indexing cost
  # [ [priority=15], [priority=14], [priority=13], .. [priority=7] ]
  harvest_candidates = [ [], [], [], [], [], [], [], [], [] ]
  harvest_candidates_index_offset = 7
  harvest_candidates_index_top = 15
  def plant_with_move():
   usa_plant.invoke()
   if current_entity == Entities.Treasure:
    return True
   elif get_entity_type() == Entities.Sunflower:
    priority = measure()
   else:
    priority = harvest_candidates_index_top
   index = harvest_candidates_index_top - priority
   harvest_candidates[index].append(util.get_pos())
   usa_move.next()
   return get_pos_y() == 0 and get_pos_x() == current_size // 2 - 1
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
 #usa_plant.plant_with_till(Entities.Bush)
 #use_item(Items.Weird_Substance, 1 * 2 ** (num_unlocked(Unlocks.Mazes) - 1))
 #harvest()
