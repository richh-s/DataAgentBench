code = """import json
import pandas as pd

# Read the file path from the variable
file_path = var_functions.query_db:2

# Load the full data from the file
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Convert to DataFrame for easier manipulation
df_papers = pd.DataFrame(papers_data)

# Extract title from filename (remove .txt extension)
df_papers['title'] = df_papers['filename'].str.replace('.txt', '', regex=False)

# Extract year from the text (search for 4-digit numbers around 2010-2025)
import re

def extract_year(text):
    # Look for patterns like '2015', '2016', etc. in the text
    years = re.findall(r'\b(20[12]\d|202[0-5])\b', str(text))
    if years:
        return int(years[0])
    return None

df_papers['year'] = df_papers['text'].apply(extract_year)

# Extract contribution type - look for 'empirical' in the text
def extract_contribution(text):
    text_lower = str(text).lower()
    contributions = []
    
    # Check for empirical contribution
    if 'empirical' in text_lower:
        contributions.append('empirical')
    
    # Check for other contribution types
    if 'artifact' in text_lower or 'system' in text_lower:
        contributions.append('artifact')
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contributions.append('theoretical')
    if 'survey' in text_lower:
        contributions.append('survey')
    if 'methodological' in text_lower or 'method' in text_lower:
        contributions.append('methodological')
    
    return ','.join(contributions) if contributions else None

df_papers['contribution'] = df_papers['text'].apply(extract_contribution)

# Filter papers published after 2016 with empirical contribution
df_filtered = df_papers[
    (df_papers['year'] > 2016) & 
    (df_papers['contribution'].str.contains('empirical', na=False))
]

# Print the filtered results
print('Papers with empirical contribution published after 2016:')
for _, row in df_filtered.iterrows():
    print(f"Title: {row['title']}, Year: {row['year']}, Contribution: {row['contribution']}")

# Count the papers
print(f"\nTotal count: {len(df_filtered)}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
