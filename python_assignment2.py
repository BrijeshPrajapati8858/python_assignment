def minimum(list):
    # Start by assuming the first number is smallest
  current_min = list[0]  

  # Loop through each number in the list
  for num in list:      
    if num < current_min:
    
    # Update current_min if current number is less
      current_min = num 
  return current_min

print (minimum([10,12,3,5,6,4]))