## framework for backtracking problems

if condition satisfied:

  succeed
  
  record solution to result
  
else:
  
  if can continue:
  
    for i in list:
    
      if i satisfy some condition:
      
        add i to solution
        
        solve subproblem
        
        remove i from solution
        
  return result
  
  
  ## Typical problems
  
  216 combination sum
  51 N queens
