'''
Poor man's implementation of a 2D matrix class
Pass a list of numbers and a TUPLLE of #rows/#cols to CTOR
Matrix object has 3 properties:

_rows = number of rows
_columns = number of columns
_data = elements of the matrix

my_mat = Matrix( [1, 2, 3, 4, 5], (2,3) ) yields a 2 x 3 matrix =>
| 1 2 |
| 3 4 |
| 5 6 |


'''
import operator

class Matrix:
    '''
    data is a list, order is a tuple of (rows, cols)
    Some arg checking?
    '''
    #Code CTOR here

    def __init__(self, data, dimensions):
        #Check if dimensions is a tuple of two integers, if not raise exception
        if len(dimensions) != 2 or type(dimensions[0]) != int or type(dimensions[1]) != int: 
            raise ValueError(f'Elements in {dimensions} not numeric OR wrong number of elements passed in') 
        #Check if dimensions size equals data size, if not raise an exception
        if len(data) != (dimensions[0] * dimensions[1]):
            raise ValueError(f'Dimensions given in {dimensions} do not match number of elements in {data}') 
        #Check if ALL entries are numeric, if not raise exception
        if any(type(elem) not in (int, float) for elem in data):
            raise ValueError(f'Not all entries in {data} are numeric') 

        self._rows = dimensions[1]
        self._columns = dimensions[0]  
        self._data = data.copy()
        

    #To print it out  --  use dunder
    def __str__(self):
        #Init an empty string and concat data and row delimiters
        '''
        | 1 2 |
        | 3 4 |
        | 5 6 |
        
        '''
        matrix_str = ""
        for row in range(self._rows):
            matrix_str += "| "
            start_idx = row * self._columns
            end_idx = (row + 1) * self._columns
            elems_this_row = [str(each_elem) for each_elem in self._data[start_idx : end_idx]]   #comprehension will convert every list item to a string, so that join can be used vvv
            elems_as_str = " ".join(elems_this_row)
            matrix_str += elems_as_str + " |\n"

        return matrix_str

    def _operate_on_matrices(self, rho_mat, operation):
        # Check if rows and columns of both match
        if self._rows != rho_mat._rows or self._columns != rho_mat._columns:
            raise ValueError ('Matrix dimensions incompatible')
        # All good...let's add elements, return result
        return Matrix([operation(elem1, elem2) for (elem1, elem2) in zip(self._data, rho_mat._data)], 
                             (self._columns, self._rows))
        
    
    # Add two matrices
    def __add__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.add)
    
    # Subtract two matrices
    def __sub__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.sub)  
    
    # Multiply (dot product, actually) two matrices
    def __mul__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.mul)      
    
    # Divide (element divide) two matrices
    def __truediv__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.truediv)     
        
        
        
if __name__ == "__main__":
    mat = Matrix([1,2,3,4,5,6], (2, 3))
    mat2 = Matrix([11,12,13,14,15,16], (2, 3))
    
    print("Matrix 'mat':")
    print(mat)
    print("Matrix 'mat2':")
    print(mat2)    
    # Add them, print result 
    sum_mats = mat + mat2  
    print("Sum of the above matrices:")
    print(sum_mats)  
    diff_mats = sum_mats - mat
    print("Difference of the above matrices:")
    print(diff_mats)  
    dot_prod_mats = sum_mats * mat
    print("Dot product of the above matrices:")
    print(dot_prod_mats)  