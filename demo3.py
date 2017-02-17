# -*- coding: UTF-8 -*-


import codity


@codity.trace_entry_and_exit
def asolution(A):
    raise IndexError()
    
    



if __name__ == "__main__":    
    
    c = codity.CodityRunner(asolution)
    
    c.run(1) 
    c.add_vector(1, 1)
    c.add_vector(2, 1)
    
    c.run_test()
    

    









