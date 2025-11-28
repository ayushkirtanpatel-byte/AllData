import numpy as np

print("\nWelcome to the numpy Analyzer 🙏😊")
print("===============================")

# --------------------------------------------------------
# 1. ARRAY CREATION
# --------------------------------------------------------

def create_A_array():
    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")     

    choice = int(input("Enter your choice: "))

    # ------------------ 1D ARRAY ------------------
    if choice == 1:
        size = int(input("Enter number of elements: "))
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        arr = np.array(elements)
        print("\n1D Array created successfully!")
        print(arr)
        return arr

    # ------------------ 2D ARRAY ------------------
    elif choice == 2:
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        print("\nEnter elements row-wise separated by space:")
        elements = list(map(int, input().split()))

        arr = np.array(elements).reshape(rows, cols)
        print("\n2D Array created successfully!")
        print(arr)
        return arr

    # ------------------ 3D ARRAY ------------------
    elif choice == 3:
        depth = int(input("Enter depth (number of matrices): "))
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        total = depth * rows * cols
        print(f"\nEnter {total} elements separated by space:")
        elements = list(map(int, input().split()))

        arr = np.array(elements).reshape(depth, rows, cols)
        print("\n3D Array created successfully!")
        print(arr)
        return arr

    else:
        print("Invalid choice!")
        return None



# --------------------------------------------------------
# 2. MATHEMATICAL OPERATIONS _ !
# --------------------------------------------------------

def mathematical_operations(arr):
    print("\nMathematical operations:")
    print("1. Addition ➕")
    print("2. Subtraction ➖")
    print("3. Multiplication ❌")
    print("4. Division 👍")

    choice = int(input("Enter your choice: "))
    n = int(input("Enter number: "))

    if choice == 1:
        print(arr + n)
    elif choice == 2:
        print(arr - n)
    elif choice == 3:
        print(arr * n)
    elif choice == 4:
        print(arr / n)
    else:
        print("Invalid choice!")



# --------------------------------------------------------
# 3. SEARCH, SORT, FILTER arrary _ !
# --------------------------------------------------------

def search_sort_filter_arrar(arr):
    print("\nSearch, Sort and Filter:")
    print("1. Search element")
    print("2. Sort array")
    print("3. Filter array")

    choice = int(input("Enter  your choice: "))

    if choice == 1:
        x = int(input("Enter element to search: "))
        positions = np.where(arr == x)
        print("Positions:", positions)

    elif choice == 2:
        print("Sorted array:", np.sort(arr, axis=None))

    elif choice == 3:
        limit = int(input("Show elements greater than: "))
        print(arr[arr > limit])

    else:
        print("Invalid choice!")



# --------------------------------------------------------
# 4. AGGREGATION / STATISTICS _ !
# --------------------------------------------------------

def aggregation_functions(arr):
    print("\nChoose aggregation/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Max")
    print("5. Min")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Sum =", np.sum(arr))
    elif choice == 2:
        print("Mean =", np.mean(arr))
    elif choice == 3:
        print("Median =", np.median(arr))
    elif choice == 4:
        print("Max =", np.max(arr))
    elif choice == 5:
        print("Min =", np.min(arr))
    else:
        print("Invalid choice!")



# --------------------------------------------------------
# 5. COMBINE the ARRAYS _ !
# --------------------------------------------------------

def combine_arrays(arr):
    print("\nCombine arrays:")
    print("1. Horizontal")
    print("2. Vertical")

    choice = int(input("Enter your choice: "))

    print("Enter elements for another array:")
    new = list(map(int, input("Enter elements: ").split()))
    arr2 = np.array(new)

    try:
        if choice == 1:
            print("Combined (Horizontal):")
            print(np.hstack((arr, arr2)))

        elif choice == 2:
            print("Combined (Vertical):")
            print(np.vstack((arr, arr2)))

        else:
            print("Invalid choice!")
    except:
        print("Shape mismatch! Cannot combine arrays.")



# --------------------------------------------------------
# 6. SPLIT ARRAYS_!
# --------------------------------------------------------

def split_array(arr):
    print("\nSplit array:")
    print("1. Horizontal split")
    print("2. Vertical split")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(np.hsplit(arr, 2))

    elif choice == 2:
        print(np.vsplit(arr, 2))

    else:
        print("Invalid choice!")



# --------------------------------------------------------
# MAIN MENU _ !
# --------------------------------------------------------

def main():
    arr = None

    while True:
        print("\nChoose an option:")
        print("1. Create array ")
        print("2. Mathematical operations")
        print("3. Search, sort, filter")
        print("4. Aggregation or Statistics")
        print("5. Combine arrays")
        print("6. Split arrays")
        print("7. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            arr = create_A_array()

        elif choice == 2 and arr is not None:
            mathematical_operations(arr)

        elif choice == 3 and arr is not None:
            search_sort_filter_arrar(arr)

        elif choice == 4 and arr is not None:
            aggregation_functions(arr)

        elif choice == 5 and arr is not None:
            combine_arrays(arr)

        elif choice == 6 and arr is not None:
            split_array(arr)

        elif choice == 7:
            print("Thank you for using the Numpy Multitool!")
            break

        else:
            print("Please create an array first!")



main()

