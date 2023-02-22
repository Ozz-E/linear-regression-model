from calculate_hypothesis import *

def hypothesis_to_vector(X, theta):

    ''' This function takes in a matrix X and a vector theta and returns a vector 
        of the same size as X, where each element is the value 
        of the hypothesis function at the corresponding element of X.
    '''
    
    hypothesis_vec = np.array([], dtype=np.float32)
    for i in range(X.shape[0]):
        hypothesis_vec = np.append(hypothesis_vec, calculate_hypothesis(X, theta, i))
    
    return hypothesis_vec