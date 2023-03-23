from data_persistence import unpickle_object

SS = unpickle_object('./ACTIVIDADES/stackitys')
print('cuanto tiene?: {}'.format(SS.top))