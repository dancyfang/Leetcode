## framework for backtracking problems
``` python
if condition satisfied:
  
  record solution to result
  
  return result
  
else:
  
  if can continue:
  
    for i in list:
    
      if i satisfy some condition:
      
        add i to solution
        
        result = solve subproblem
        
        remove i from solution
        
  return result
 ```
  
  ## Typical problems
  
  216 combination sum
  51 N queens
