def linear_search( array, target ):
  for i in xrange( len( array ) ):
    if array[ i ] == target:
      return i
  return false
