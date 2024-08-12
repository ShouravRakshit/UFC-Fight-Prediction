import pandas as pd
import ast

def load_data(file_path):
    return pd.read_excel(file_path)

def convert_to_dict(x):
    try:
        if isinstance(x, str) and x.startswith('RECORD: '):
            return x.replace('RECORD: ', '').strip()
        return ast.literal_eval(x)
    except (ValueError, SyntaxError):
        return x

def split_record(record):
    parts = record.split(' ')
    # Split wins, losses, and draws
    wld = parts[0].split('-')
    if len(wld) == 2:  # If there is no draw part
        wld.append('0')
    # Check for No Contest (NC)
    if len(parts) > 1 and parts[1] == '(1 NC)':
        nc = '1'
    else:
        nc = '0'
    return wld + [nc]

def main():
    file_path = 'cleaned_fighter_data.xlsx'  # Update with your file path
    df = load_data(file_path)

    # Drop the 'Nickname' column
    df.drop(columns=['Nickname'], inplace=True)

    # Convert columns to dictionaries
    df['Career Statistics'] = df['Career Statistics'].apply(convert_to_dict)
    df['Fight History'] = df['Fight History'].apply(convert_to_dict)
    df['Record'] = df['Record'].apply(convert_to_dict)

    # Filter out rows with empty fight history
    df = df[df['Fight History'].map(lambda x: len(x) > 0)]

    # Split the 'Record' column and create new columns for Wins, Losses, Draws, and No Contest
    df['Wins'], df['Losses'], df['Draws'], df['No Contest'] = zip(*df['Record'].apply(split_record))

    # Save cleaned data back to a new Excel file
    df.to_excel('cleaned_fighter_data_updated1.xlsx', index=False)

if __name__ == '__main__':
    main()
