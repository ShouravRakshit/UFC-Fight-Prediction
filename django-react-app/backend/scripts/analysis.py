import pandas as pd

def load_data(file_path):
    """Load the dataset from the fighter Excel file."""
    return pd.read_excel(file_path)


def main():
    # Load the data
    file_path = 'fighter_data.xlsx'
    df = load_data(file_path)

    # Print the shape of the data
    print(df['Career Statistics'][5])  

if __name__ == "__main__":
    main()
