def calculate_1d_address(base_address, data_type_size, index, lower_bound):
    # Calculate the memory address for a 1D array
    address = base_address + (index - lower_bound) * data_type_size
    return address

def main_1D():
    print("1D Array Memory Address Calculator:")
    
    # User inputs
    base_address = int(input("Enter the Base Address of the array: "))
    lower_bound = int(input("Enter the Lower Bound (starting index) of the array: "))
    data_type_size = int(input("Enter the size of each element in bytes: "))
    index_1d = int(input("Enter the index for the element to calculate the address for in the 1D array: "))
    
    # Calculate 1D array memory address
    address_1d = calculate_1d_address(base_address, data_type_size, index_1d, lower_bound)
    
    # Display the detailed result for the 1D array
    print("\nCalculation for 1D Array:")
    print(f"The memory address for B[{index_1d}] in the 1D array is calculated as follows:")
    print(f"Base Address: {base_address}")
    print(f"Data Type Size: {data_type_size} bytes")
    print(f"Lower Bound (Starting Index): {lower_bound}")
    print(f"Index for the Element: {index_1d}")
    print(f"Calculated Memory Address: {address_1d}")

if __name__ == "__main__":
    main_1D()
