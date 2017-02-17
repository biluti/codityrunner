# -*- coding: UTF-8 -*-


import codity


@codity.trace_entry_and_exit
def solution(A):
    return sum(A)



if __name__ == "__main__":    
    
    c = codity.CodityRunner()
    
    c.run([1, 2, 3]) 
    c.run([1, 1]) 
    
    c.add_vector(0, [1, 2, 3])
    c.add_vector(6, [1, 2, 3])
    
    c.run_test()
    

    









