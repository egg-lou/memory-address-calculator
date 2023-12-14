def calculate_memory_address_column_major(base_address, data_type_size, lower_bound_row, lower_bound_col, index_row, index_col, upper_bound_row):
    # Calculate the number of rows in the matrix
    num_rows = upper_bound_row - lower_bound_row + 1
    
    # Calculate the memory address using the column-major formula
    address = base_address + data_type_size * (num_rows * (index_col - lower_bound_col) + (index_row - lower_bound_row))
    
    return address

def main_column_major():
    print("Column-Major Order Memory Address Calculator:")
    
    # User inputs
    base_address = int(input("Enter the Base Address for the matrix: "))
    data_type_size = int(input("Enter the Data Type Size for each element in the matrix: "))
    lower_bound_row = int(input("Enter the Lower Bound Row index for the matrix: "))
    lower_bound_col = int(input("Enter the Lower Bound Column index for the matrix: "))
    index_row = int(input("Enter the index row for the element: "))
    index_col = int(input("Enter the index column for the element: "))
    upper_bound_row = int(input("Enter the Upper Bound Row index for the matrix: "))
    
    # Calculate memory address using the column-major formula
    result_column_major = calculate_memory_address_column_major(
        base_address, data_type_size, lower_bound_row, lower_bound_col, index_row, index_col, upper_bound_row
    )
    
    # Display the detailed result for column-major order
    print("\nCalculation for Column-Major Order:")
    print(f"The memory address for A[{index_row}][{index_col}] in column-major order is calculated as follows:")
    print(f"Base Address: {base_address}")
    print(f"Data Type Size: {data_type_size} bytes")
    print(f"Lower Bound Row Index: {lower_bound_row}")
    print(f"Lower Bound Column Index: {lower_bound_col}")
    print(f"Index Row: {index_row}")
    print(f"Index Column: {index_col}")
    print(f"Upper Bound Row Index: {upper_bound_row}")
    print(f"Number of Rows in the Matrix: {upper_bound_row - lower_bound_row + 1}")
    print(f"Calculated Memory Address: {result_column_major}")

if __name__ == "__main__":
    main_column_major()
