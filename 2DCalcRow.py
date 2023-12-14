def calculate_memory_address_row_major(base_address, data_type_size, lower_bound_row, lower_bound_col, index_row, index_col, upper_bound_col):
    # Calculate the number of columns in the matrix
    num_cols = upper_bound_col - lower_bound_col + 1
    
    # Calculate the memory address using the row-major formula
    address = base_address + data_type_size * (num_cols * (index_row - lower_bound_row) + (index_col - lower_bound_col))
    
    return address

def main_row_major():
    print("Row-Major Order Memory Address Calculator:")
    
    # User inputs
    base_address = int(input("Enter the Base Address for the matrix: "))
    data_type_size = int(input("Enter the Data Type Size for each element in the matrix: "))
    lower_bound_row = int(input("Enter the Lower Bound Row index for the matrix: "))
    lower_bound_col = int(input("Enter the Lower Bound Column index for the matrix: "))
    index_row = int(input("Enter the index row for the element: "))
    index_col = int(input("Enter the index column for the element: "))
    upper_bound_col = int(input("Enter the Upper Bound Column index for the matrix: "))
    
    # Calculate memory address using the row-major formula
    result_row_major = calculate_memory_address_row_major(
        base_address, data_type_size, lower_bound_row, lower_bound_col, index_row, index_col, upper_bound_col
    )
    
    # Display the detailed result for row-major order
    print("\nCalculation for Row-Major Order:")
    print(f"The memory address for A[{index_row}][{index_col}] in row-major order is calculated as follows:")
    print(f"Base Address: {base_address}")
    print(f"Data Type Size: {data_type_size} bytes")
    print(f"Lower Bound Row Index: {lower_bound_row}")
    print(f"Lower Bound Column Index: {lower_bound_col}")
    print(f"Index Row: {index_row}")
    print(f"Index Column: {index_col}")
    print(f"Upper Bound Column Index: {upper_bound_col}")
    print(f"Number of Columns in the Matrix: {upper_bound_col - lower_bound_col + 1}")
    print(f"Calculated Memory Address: {result_row_major}")

if __name__ == "__main__":
    main_row_major()
