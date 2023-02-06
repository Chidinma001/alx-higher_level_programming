#!/usr/bin/python3                                                                                     
                                                                                                       
"""                                                                                                    
divides all elements of a matrix                                                                       
"""                                                                                                    
def matrix_divided(matrix, div):                                                                       
    '''                                                                                                
                                                                                                       
    :param matrix:    the matrix in form of a list                                                     
    :param div:     the divisor , a constant number                                                    
    :return:        returns the quotients of the elements in form of a matrix                          
    '''
    newlist=[]                                                                         
    if  not  isinstance(div,(int,float)):                                                              
                                                                                                       
        raise TypeError('div must be a number')                                                        
    if div == 0:                                                                                       
        raise ZeroDivisionError("division by zero")                                                    
                                                                                                       
    for i in matrix:                                                                                   
        if len(i) != len(matrix[0]):                                                                   
                                                                                                       
            raise TypeError('Each row of the matrix must have the same size')                          
                                                                                                       
        result = []                                                                                    
                                                                                                       
        for j in i:                                                                                    
                                                                                                       
           if isinstance(j,(int,float)) == False:                                                      
                                                                                                       
              raise TypeError('matrix must be a matrix (list of lists) of integers/floats')            
                                                                                                       
           result.append(round((j / div),2))
        newlist.append(result)                                                    
        return result
