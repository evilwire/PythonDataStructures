def swap( array, i, j ):
  b = array[j]
  array[j] = array[i]
  array[i] = b

def insertion_sort(array):
  for i in range( 1, len( array ) ):
    currentNum = array[i]
    if currentNum < array[i - 1]:
      for j in xrange( i ):
        if array[j] > currentNum:
          swap( array, i, j )

arr = [1, 9, 7, 2, 19, 5, 3]
insertion_sort( arr )
print arr
