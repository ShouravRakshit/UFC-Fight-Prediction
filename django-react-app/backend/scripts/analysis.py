import pandas as pd
import ast

def load_data(file_path):
    return pd.read_excel(file_path)

def split_record(record):
    try:
        record = record.replace('RECORD: ', '').split(' (')[0].strip()
        wins, losses = map(int, record.split('-')[:2])
        return [wins, losses]
    except ValueError as e:
        print(f"Error processing record '{record}': {e}")
        return [0, 0]

def calculate_streaks(fight_history):
    fight_history = fight_history[:8]  # Consider only the last 8 fights
    win_streak = loss_streak = 0
    current_streak = 1
    last_result = fight_history[0]['Outcome']

    for fight in fight_history[1:]:
        if fight['Outcome'] == last_result:
            current_streak += 1
        else:
            if last_result == 'WIN' and current_streak >= 3:
                win_streak = max(win_streak, current_streak)
            elif last_result == 'LOSS' and current_streak >= 3:
                loss_streak = max(loss_streak, current_streak)
            current_streak = 1
            last_result = fight['Outcome']

    # Check the final streak
    if last_result == 'WIN' and current_streak >= 3:
        win_streak = max(win_streak, current_streak)
    elif last_result == 'LOSS' and current_streak >= 3:
        loss_streak = max(loss_streak, current_streak)

    return [win_streak if win_streak >= 3 else 0, loss_streak if loss_streak >= 3 else 0]

def main():
    file_path = 'C:\\Work\\GeeksforGeek\\cleaned_fighter_data_updated.xlsx'
    df = load_data(file_path)

    # Ensure 'Fight History' is a list of dicts
    df['Fight History'] = df['Fight History'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # Keep only fighters with at least 8 fights
    df = df[df['Fight History'].apply(len) >= 8]

    # Extract wins and losses
    df[['Wins', 'Losses']] = pd.DataFrame(df['Record'].apply(split_record).tolist(), index=df.index)

    # Calculate streaks for last 8 fights
    df['Win Streak'], df['Loss Streak'] = zip(*df['Fight History'].apply(calculate_streaks))

    # Save the updated data
    df.to_excel("C:\\Work\\GeeksforGeek\\cleaned_fighter_data_updated3.xlsx", index=False)

if __name__ == '__main__':
    main()





















[{'Outcome': 'WIN', 'Opponent': 'Sergei Pavlovich', 'Event': 'UFC 295: Prochazka vs. Pereira', 'Event Date': 'Nov. 11, 2023', 'Method': 'KO/TKO', 'Round': '1', 'Time': '1:09'}, {'Outcome': 'WIN', 'Opponent': 'Marcin Tybura', 'Event': 'UFC Fight Night: Aspinall vs. Tybura', 'Event Date': 'Jul. 22, 2023', 'Method': 'KO/TKO', 'Round': '1', 'Time': '1:13'}, {'Outcome': 'LOSS', 'Opponent': 'Curtis Blaydes', 'Event': 'UFC Fight Night: Blaydes vs. Aspinall', 'Event Date': 'Jul. 23, 2022', 'Method': 'KO/TKO', 'Round': '1', 'Time': '0:15'}, {'Outcome': 'WIN', 'Opponent': 'Alexander Volkov', 'Event': 'UFC Fight Night: Volkov vs. Aspinall', 'Event Date': 'Mar. 19, 2022', 'Method': 'SUB', 'Round': '1', 'Time': '3:45'}, {'Outcome': 'WIN', 'Opponent': 'Serghei Spivac', 'Event': 'UFC Fight Night: Brunson vs. Till', 'Event Date': 'Sep. 04, 2021', 'Method': 'KO/TKO', 'Round': '1', 'Time': '2:30'}, {'Outcome': 'WIN', 'Opponent': 'Andrei Arlovski', 'Event': 'UFC Fight Night: Blaydes vs. Lewis', 'Event Date': 'Feb. 20, 2021', 'Method': 'SUB', 'Round': '2', 'Time': '1:09'}, {'Outcome': 'WIN', 'Opponent': 'Alan Baudot', 'Event': 'UFC Fight Night: Moraes vs. Sandhagen', 'Event Date': 'Oct. 10, 2020', 'Method': 'KO/TKO', 'Round': '1', 'Time': '1:35'}, {'Outcome': 'WIN', 'Opponent': 'Jake Collier', 'Event': 'UFC Fight Night: Whittaker vs. Till', 'Event Date': 'Jul. 25, 2020', 'Method': 'KO/TKO', 'Round': '1', 'Time': '0:45'}]