import pandas as pd
import ast

def load_data(file_path):
    return pd.read_excel(file_path)

def convert_to_dict(fighting_career):
    if isinstance(fighting_career, str):
        return ast.literal_eval(fighting_career)
    return fighting_career

def main():
    file_path = 'cleaned_fighter_data.xlsx'  # Update with your file path
    df = load_data(file_path)
    
    df.drop(columns=['Nickname'], inplace=True)
    # Convert Career Statistics column to dictionaries
    df['Career Statistics'] = df['Career Statistics'].apply(convert_to_dict)
    df['Fight History'] = df['Fight History'].apply(convert_to_dict)
    # Access a specific value within the first row's Career Statistics dictionary
    first_row_career_stats = df['Career Statistics'][4]
    # print(first_row_career_stats)
    # print(df.head())
    # print(first_row_career_stats[''])  

if __name__ == '__main__':
    main()

