import pandas as pd
import ast

def load_data(file_path):
    return pd.read_excel(file_path)

def split_record(record):
    try:
        # Strip any prefix and remove the 'NC' part if present
        record = record.replace('RECORD: ', '').split(' (')[0].strip()
        parts = record.split('-')
        wins = int(parts[0])
        losses = int(parts[1])
        # Exclude draws for simplification
        return [wins, losses]
    except Exception as e:
        print(f"Error processing record '{record}': {e}")
        return [0, 0]  # Return default values in case of any parsing error

def calculate_streaks(fight_history):
    # Calculate streaks of wins and losses
    wins, losses = 0, 0
    max_wins, max_losses = 0, 0
    
    for fight in fight_history:
        if fight['Outcome'] == 'WIN':
            wins += 1
            losses = 0
        elif fight['Outcome'] == 'LOSS':
            losses += 1
            wins = 0
        max_wins = max(max_wins, wins)
        max_losses = max(max_losses, losses)
    
    return max_wins, max_losses

def main():
    file_path = 'C:\\Work\\GeeksforGeek\\cleaned_fighter_data.xlsx'  # Update with your file path
    df = load_data(file_path)

    # Convert 'Fight History' from string to list if needed
    df['Fight History'] = df['Fight History'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # Filter out fighters with fewer than 8 fights
    df = df[df['Fight History'].apply(lambda x: len(x) >= 8)]

    # Apply the modified split_record function
    records = df['Record'].apply(split_record)
    df[['Wins', 'Losses']] = pd.DataFrame(records.tolist(), index=df.index)

    # Calculate win/loss streaks
    df['Win Streak'], df['Loss Streak'] = zip(*df['Fight History'].apply(calculate_streaks))

    # Get results of the last 8 fights
    df['Last 8 Fights'] = df['Fight History'].apply(lambda x: x[-8:])

    # Save the cleaned data
    df.to_excel("C:\\Work\\GeeksforGeek\\cleaned_fighter_data_updated2.xlsx", index=False)

if __name__ == '__main__':
    main()
