def merge( array_A, array_B ):
  merged_array = []
  A_index = 0
  B_index = 0
  for i in xrange( len(array_A) + len(array_B) ):
    if array_A[ A_index ] >= array_B[ B_index ]:
      merged_array.append( array_A[ A_index ] )
      A_index += 1
    else
      merged_array.append( array_B[ B_index ] )
      B_index += 1

def merge_sort( array ):
  array_length = len( array )
  half_way = int( array_length / 2 )
  array_A = merge_sort( array[0 : half_way ] )
  array_B = merge_sort( array[ half_way : array_length ] )
  return merge( array_A, array_B )
