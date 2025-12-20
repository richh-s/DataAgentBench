code = """import json
import pandas as pd

# Load full data from file path
file_path = var_call_c51O2t6EEeNh8O8dKOjyhWmG
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Heuristic to detect sports articles based on title/description keywords
sports_keywords = [
    'football','soccer','nba','nfl','mlb','nhl','tennis','golf','olympic','olympics',
    'world cup','league','final','quarterfinal','semifinal','grand prix','formula one',
    'f1','motogp','cricket','rugby','baseball','basketball','hockey','cup tie','playoff',
    'play-offs','play offs','tournament','championship','coach','manager','striker',
    'midfielder','defender','goalkeeper','goalie','pitcher','slugger','race','rally',
    'track and field','marathon','athletics','boxing','ufc','mixed martial arts','mma',
    'nascar','indycar','shot','goal','touchdown','home run','no-hitter','hat-trick',
    'hat trick','premier league','la liga','bundesliga','serie a','nfl','nba','nhl',
    'major league','pga','wta','atp','cup win','derby','test match','one-day',
    'one day international','odi','innings','wicket','ashesi','tour de france','cycling'
]

pattern = '|'.join([k.replace(' ', '\\s+') for k in sports_keywords])

mask = (
    df['title'].str.lower().str.contains(pattern, regex=True, na=False) |
    df['description'].str.lower().str.contains(pattern, regex=True, na=False)
)

sports_df = df[mask].copy()

# Compute length of description and find max
sports_df['desc_len'] = sports_df['description'].astype(str).str.len()

max_row = sports_df.sort_values('desc_len', ascending=False).iloc[0]

result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_c51O2t6EEeNh8O8dKOjyhWmG': 'file_storage/call_c51O2t6EEeNh8O8dKOjyhWmG.json'}

exec(code, env_args)
