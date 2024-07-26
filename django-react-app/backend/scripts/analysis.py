import pandas as pd
import ast

def load_data(file_path):
    return pd.read_excel(file_path)

def convert_to_dict(x):
    try:
        # For 'Record' we need to strip "RECORD: " and then convert to dictionary
        if isinstance(x, str) and x.startswith('RECORD: '):
            return x.replace('RECORD: ', '').strip()
        return ast.literal_eval(x)
    except (ValueError, SyntaxError):
        return x


def main():
    file_path = 'cleaned_fighter_data.xlsx'  # Update with your file path
    df = load_data(file_path)
    
    df.drop(columns=['Nickname'], inplace=True)
    # Convert Career Statistics column to dictionaries
    # df['First Name'] = df['First Name'].apply(convert_to_dict)
    # df['Last Name'] = df['Last Name'].apply(convert_to_dict)
    df['Career Statistics'] = df['Career Statistics'].apply(convert_to_dict)
    df['Fight History'] = df['Fight History'].apply(convert_to_dict)
    df['Record'] = df['Record'].apply(convert_to_dict)

    print(df['First Name'][3])
    # print(first_row_career_stats[''])  

if __name__ == '__main__':
    main()

