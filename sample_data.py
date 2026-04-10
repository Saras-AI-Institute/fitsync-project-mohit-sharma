import pandas as pd

def main():
    # Load the dataset
    file_path = "data/health_data.csv"
    
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    # Print first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head())

    print("\n" + "="*50 + "\n")

    # Print number of missing values in each column
    print("Number of missing values in each column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    main()