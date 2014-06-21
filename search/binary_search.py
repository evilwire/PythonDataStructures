# assumption: the list is sorted
def binary_search_index( array, target, start, end ):
  if start == end:
    return start if array[ start ] == target else -1
  
  half_point = int( ( start - end )/ 2 ) 
  if array[ half_point ] == target:
    return half_point

  if array[ half_point ] < target :
    return binary_search_index( array, target, 
      start, half_point )
  
  return binary_search_index( array, target, 
    half_point, end )

def binary_search( arr, target ):
  return binary_search_index( array, target, 0,
    len( array ) )
