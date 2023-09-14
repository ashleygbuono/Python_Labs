from packageforlab6 import numberstuff, stringstuff

def main() :
    a_num = 12
    print(f'Original number: {a_num}')
    print(f'Cosine: {numberstuff.cosine_of( a_num ) }')
    print(f'Square root: {numberstuff.square_root_of( a_num ) }')
    print(f'Factorial: {numberstuff.factorial_of( a_num ) }')

if __name__ == "__main__":
    main()


def main() :
    a_string = "Mary had a little lamb"
    print(f'Original string: {a_string}')
    print(f'Upper case: {stringstuff.make_upper_case( a_string ) }')
    print(f'Lower case: {stringstuff.make_lower_case( a_string ) }')
    print(f'Title case: {stringstuff.make_title_case( a_string ) }')
    print(f'Number of characters: {stringstuff.string_length( a_string ) }')

if __name__ == "__main__":
    main()


print(f'Calling functions from package modules')
