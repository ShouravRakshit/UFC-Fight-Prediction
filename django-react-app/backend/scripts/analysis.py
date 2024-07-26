import pandas as pd
import ast

def load_data(file_path):
    return pd.read_excel(file_path)

def convert_to_dict(career_stats):
    if isinstance(career_stats, str):
        return ast.literal_eval(career_stats)
    return career_stats

def main():
    file_path = 'cleaned_fighter_data.xlsx'  # Update with your file path
    df = load_data(file_path)

    # Convert Career Statistics column to dictionaries
    df['Career Statistics'] = df['Career Statistics'].apply(convert_to_dict)

    # Access a specific value within the first row's Career Statistics dictionary
    first_row_career_stats = df['Career Statistics'][4]
    print(first_row_career_stats)
    
    # Access a specific key's value
    print(first_row_career_stats[''])  # Replace 'SLpM' with the key you want to access

if __name__ == '__main__':
    main()

