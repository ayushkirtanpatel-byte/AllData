import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class NumpyAnalyzer:

    def __init__(self):
        self.df = None

    # ------------------ LOAD DATASET ------------------
    
    def load_data_set(self):
        file = input("Enter file name with extension (e.g., data.csv): ")
        try:
            self.df = pd.read_csv(file)
            print("✅ Data loaded successfully!")
        except:
            print("❌ Error: File not found!")

    # ------------------ EXPLORE DATASET ------------------

    def explore_data_set(self):

        if self.df is None:
            print("❌ Load dataset first!")
            return

        while True:
            print("\n===== Exploring Dataset =====")
            print("1. Display first 5 rows")
            print("2. Display last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice < 1 or choice > 6:
                print("❌ Invalid choice!")
                continue


            if choice == 1:
                print(self.df.head())

            elif choice == 2:
                print(self.df.tail())

            elif choice == 3:
                print(self.df.columns)

            elif choice == 4:
                print(self.df.dtypes)

            elif choice == 5:
                print(self.df.info())

            elif choice == 6:
                break

            else:
                print("❌ Invalid choice!")

    # ------------------ HANDLE MISSING VALUES ------------------

    def handling_missing_values_data(self):

        if self.df is None:
            print("❌ Load dataset first!")
            return

        while True:

            print("\n===== Handling Missing Values =====")

            print("1. Remove rows with missing values")
            print("2. Fill missing values (mean/median/mode)")
            print("3. Drop rows where ANY value is missing")
            print("4. Replace missing values with a specific value")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice < 1 or choice > 5:
                print("❌ Invalid choice!")
                continue

            if choice == 1:
                self.df.dropna(inplace=True)
                print("✅ Rows with missing values removed!")

            elif choice == 2:
                col = input("Enter column name: ")
                method = input("Enter method (mean/median/mode): ")

                if col not in self.df.columns:
                    print("❌ Column not found!")
                    continue

                if method == "mean":
                    self.df[col].fillna(self.df[col].mean(), inplace=True)

                elif method == "median":
                    self.df[col].fillna(self.df[col].median(), inplace=True)

                elif method == "mode":
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)

                else:
                    print("❌ Invalid method!")
                    continue

                print(f"✅ Missing values in '{col}' filled using {method}")

            elif choice == 3:
                self.df.dropna(inplace=True)
                print("✅ Rows with NaN dropped!")

            elif choice == 4:
                col = input("Enter column name: ")
                val = input("Enter value: ")
                self.df[col].fillna(val, inplace=True)
                print(f"✅ Missing values in '{col}' replaced!")

            elif choice == 5:
                break

    # ------------------ DATA VISUALIZATION ------------------

    def data_visualization(self):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        print("\n== Data Visualization ==")

        print("1. Bar plot")
        print("2. Line plot")
        print("3. Scatter plot")
        print("4. Pie chart")
        print("5. Histogram")
        print("6. Stack plot")

        choice = int(input("Enter your choice: "))

        # Common inputs

        if choice in [1, 2, 3, 4, 5, ]:
            xcol = input("Enter x column: ")
            ycol = input("Enter y column: ")
            titels = input("Enter plot title: ")
            xlabel = input("Enter x label: ")
            ylabel = input("Enter y label: ")
            plt.title(titels)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)

            while True:

                print("\nCustomize Visualization Options:")

                print("1. Set custom figure size")
                print("2. Set custom colours")
                print("3. Set custom colours and legends")
                print("on. Use default figure size")
                print("on. Use default colours")
                print("0. to exit")

                choiceother = input("Do you want to set custom thoer function? (yes/no): ")

                if choiceother==1:
                    whidths= input("Enter width (or press Enter for default): ")
                    hights= input("Enter height (or press Enter for default): ")
                    plt.figure(figsize=(int(whidths), int(hights)))

                elif choiceother=="no":
                    plt.figure(figsize=(10, 6))

                elif choiceother==2:
                    colours = input("Enter colours (comma separated): ").split(",")

                elif choiceother=='on':
                    colours = ['blue' ]

                elif choiceother==3:
                    lengends= input("Enter legend labels (comma separated): ").split(",")
                    colours = input("Enter colours (comma separated): ").split(",")

                elif choiceother=='no':
                    colours = ['red']

                elif choiceother==0:
                    break

                else:
                    print("❌ Invalid choice!")

        # ---------------- PLOTS -------------------

        if choice == 1:  # Bar plot
            sns.barplot(data=self.df, x=xcol, y=ycol, color=colours[0])

        elif choice == 2:  # Line plot
            sns.lineplot(data=self.df, x=xcol, y=ycol, color=colours[0])

        elif choice == 3:  # Scatter plot
            sns.scatterplot(data=self.df, x=xcol, y=ycol, color=colours[0])

        elif choice == 4:  # Pie chart
            col = input("Enter column for pie chart: ")
            self.df[col].value_counts().plot.pie(autopct="%1.1f%%")
            plt.title("Pie Chart")

        elif choice == 5:  # Histogram
            col = input("Enter column for histogram: ")
            bins = int(input("Enter bins: "))
            sns.histplot(self.df[col], bins=bins)

        elif choice == 6:  # Stack plot
            plt.stackplot(self.df[xcol], self.df[ycol], colors=colours)

        else:
            print("❌ Invalid choice!")
            return

        plt.show()


    # ------------------ SAVE PLOT ------------------
    
    
    def save_visualization(self):

        if self.df is None:
            print("❌ Load dataset first!")
            return

        print("\n===== Save Visualization =====")

        print("1. Save bar plot")
        print("2. Save line plot")
        print("3. Save scatter plot")
        print("4. Save pie chart")
        print("5. Save histogram")
        print("6. Save stack plot")

        choice = int(input("Enter your choice: "))
        filename = input("Enter filename (.png): ")

        if choice in [1, 2, 3, 4, 5, ]:
            xcol = input("Enter x column: ")
            ycol = input("Enter y column: ")
            titels = input("Enter plot title: ")
            xlabel = input("Enter x label: ")
            ylabel = input("Enter y label: ")
            plt.title(titels)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)

        # ---------------- PLOTS -------------------

        if choice == 1:
            sns.barplot(data=self.df, x=xcol, y=ycol)

        elif choice == 2:
            sns.lineplot(data=self.df, x=xcol, y=ycol)

        elif choice == 3:
            sns.scatterplot(data=self.df, x=xcol, y=ycol)

        elif choice == 4:
            col = input("Enter column: ")
            self.df[col].value_counts().plot.pie(autopct="%1.1f%%")

        elif choice == 5:
            col = input("Enter column: ")
            bins = int(input("Enter bins: "))
            sns.histplot(self.df[col], bins=bins)

        elif choice == 6:
            plt.stackplot(self.df[xcol], self.df[ycol])

        else:
            print("❌ Invalid choice!")
            return

        # Save plot
        plt.savefig(filename)
        print(f"✅ Plot saved as {filename}")

    # ------------------ DATAFRAME OPERATIONS ------------------

    def perform_dataframe_operation(self):

        if self.df is None:
            print("❌ Load dataset first!")
            return

        while True:

            print("\n===== DataFrame Operations =====")

            print("1. Display specific columns")
            print("2. Sort DataFrame")
            print("3. Filter rows by condition")
            print("4. Rename column")
            print("5. Drop column")
            print("6. Add new column")
            print("7. Replace values in a column")
            print("8. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                cols = input("Enter column names (comma separated): ").split(",")
                print(self.df[cols])

            elif choice == 2:
                col = input("Enter column to sort by: ")
                order = input("Ascending? (yes/no): ")
                asc = True if order == "yes" else False
                print(self.df.sort_values(by=col, ascending=asc))

            elif choice == 3:
                col = input("Enter column: ")
                condition = input("Condition (>, <, ==): ")
                val = input("Value: ")
                print(self.df.query(f"{col} {condition} {val}"))

            elif choice == 4:
                col = input("Enter old name: ")
                new = input("Enter new name: ")
                self.df.rename(columns={col: new}, inplace=True)
                print("✅ Column renamed!")

            elif choice == 5:
                col = input("Enter column to drop: ")
                self.df.drop(columns=[col], inplace=True)
                print("✅ Column dropped!")

            elif choice == 6:
                col = input("Enter new column name: ")
                val = input("Default value: ")
                self.df[col] = val
                print("✅ Column added!")

            elif choice == 7:
                col = input("Enter column: ")
                old = input("Replace: ")
                new = input("With: ")
                self.df[col].replace(old, new, inplace=True)
                print("✅ Values replaced!")

            elif choice == 8:
                break

    # ------------------ DESCRIPTIVE STATISTICS ------------------

    def generate_descriptive_statistics(self):

        if self.df is None:
            print("❌ Load dataset first!")
            return

        print("\n===== Descriptive Statistics =====")
        print(self.df.describe())

        while True:
            print("\n1. Mean")
            print("2. Median")
            print("3. Mode")
            print("4. Standard deviation")
            print("5. Variance")
            print("6. Min")
            print("7. Max")
            print("8. Sum")
            print("9. Count")
            print("0. Exit")

            choice = int(input("Enter your choice: "))

            if choice < 0 or choice > 9:
                print("❌ Invalid choice!")
                continue
    
            if choice == 1:
                print(self.df.mean())

            elif choice == 2:
                print(self.df.median())

            elif choice == 3:
                print(self.df.mode())

            elif choice == 4:
                print(self.df.std())

            elif choice == 5:
                print(self.df.var())

            elif choice == 6:
                print(self.df.min())

            elif choice == 7:
                print(self.df.max())

            elif choice == 8:
                print(self.df.sum())

            elif choice == 9:
                print(self.df.count())

            elif choice == 0:
                break


# ------------------ RUN ------------------
obj = NumpyAnalyzer()

while True:

    print("\n======== MAIN MENU ========")

    print("1. enter 1 to Load Dataset")
    print("2. enter 2 to Explore Dataset")
    print("3. enter 3 to Perform DataFrame Operations")
    print("4. enter 4 to Handle Missing Values")
    print("5. enter 5 to Generate Descriptive Statistics")
    print("6. enter 6 to Visualize Data")
    print("7. enter 7 to Save Visualization")
    print("0. Exit")

    main_choice = int(input("Enter choice: "))

    if main_choice < 0 or main_choice > 7:
        print("❌ Invalid choice!")
        continue


    if main_choice == 1:
        obj.load_data_set()

    elif main_choice == 2:
        obj.explore_data_set()

    elif main_choice == 3:
        obj.perform_dataframe_operation()

    elif main_choice == 4:
        obj.handling_missing_values_data()

    elif main_choice == 5:
        obj.generate_descriptive_statistics()

    elif main_choice == 6:
        obj.data_visualization()

    elif main_choice == 7:
        obj.save_visualization()

    elif main_choice == 0:
        print("✅ Exiting program...")
        break


    else:
        print("❌ Invalid choice!")

