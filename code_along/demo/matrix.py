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



if __name__ == "__main__":
    mat = Matrix([1, 2, 3, 4, 5, 6], (2, 3))

    print(mat)  