def fwd_diff(vector):
    ###
    '''Calculate the forward difference of elements in a numpy vector:
    v_i+1 - v_i'''
    ###
    import numpy as np
    ###
    subs_val = vector[0]
    ##
    dimension = vector.shape[0]
    fwd_vals = np.zeros(dimension - 1)
    index = 0
    ### 
    for value in vector[1:]:
        fwd_vals[index] = value - subs_val
        subs_val = value
        index = index + 1
    ###
    return fwd_vals
        
