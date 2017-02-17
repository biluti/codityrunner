# -*- coding: UTF-8 -*-


import codity


@codity.trace_entry_and_exit
def solution(a, b):
    return a+b



if __name__ == "__main__":    
    
    c = codity.CodityRunner()
    
    c.run(1, 2) 
    c.run(2, 2) 
    
    
    c.add_vector(3, 1, 2)
    c.add_vector(3, 2, 2)
    
    c.run_test()
    

    









