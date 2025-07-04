import numpy as np

class NumPyAnalyzer:
    def __init__(self):
        self.array = None

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array") 
        print("2. 2D Array")
        print("3. 3D Array")
        array_type = int(input("Enter your choice: "))

        match array_type:
            case 1:
                elements = list(map(int, input("Enter elements separated by space: ").split()))
                self.array = np.array(elements)
            case 2:
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                elements = list(map(int, input("Enter elements separated by space: ").split()))
                self.array = np.array(elements).reshape(rows, cols)
            case 3:
                depth = int(input("Enter dim 1: "))
                rows = int(input("Enter dim 2: "))
                cols = int(input("Enter dim 3: "))
                elements = list(map(int, input("Enter elements separated by space: ").split()))
                self.array = np.array(elements).reshape(depth, rows, cols)
        print("Array created successfully:\n", self.array)

    def mathematical_operations(self):
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter your choice: "))
        elements = list(map(int, input(f"Enter elements (same shape as original): ").split()))
        other = np.array(elements).reshape(self.array.shape)

        match choice:
            case 1:
                result = self.array + other
            case 2:
                result = self.array - other
            case 3:
                result = self.array * other
            case 4:
                result = self.array / other
        print("Result:\n", result)

    def combine_split_arrays(self):
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                elements = list(map(int, input("Enter elements for second array: ").split()))
                second = np.array(elements).reshape(self.array.shape)
                combined = np.vstack((self.array, second))
                print("Combined Array (Vertical Stack):\n", combined)
            case 2:
                print("Split not implemented in output sample.")

    def search_sort_filter(self):
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array") 
        print("3. Filter values")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                value = int(input("Enter value to search: "))
                result = np.where(self.array == value)
                print("Value found at indices:", result)
            case 2:
                sorted_array = np.sort(self.array, axis=1)
                print("Sorted Array:\n", sorted_array)
            case 3:
                threshold = int(input("Enter value to filter above: "))
                filtered = self.array[self.array > threshold]
                print("Filtered values:\n", filtered)

    def aggregate_statistics(self):
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("Sum:", np.sum(self.array))
            case 2:
                print("Mean:", np.mean(self.array))
            case 3:
                print("Median:", np.median(self.array))
            case 4:
                print("Standard Deviation:", np.std(self.array))
            case 5:
                print("Variance:", np.var(self.array))

    def run(self):
        while True:
            print("\nWelcome to the NumPy Analyzer!")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    self.create_array()
                case 2:
                    self.mathematical_operations()
                case 3:
                    self.combine_split_arrays()
                case 4:
                    self.search_sort_filter()
                case 5:
                    self.aggregate_statistics()
                case 6:
                    print("Thank you for using the NumPy Analyzer! Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")


ana = NumPyAnalyzer()
ana.run()
