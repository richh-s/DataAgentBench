code = """import json
import pandas as pd
import re

# Load paper data from file - need to use locals() to access the variable
var_key = 'var_functions.query_db:8'  # Use string key to access locals()
if var_key in locals():
    paper_data_file = locals()[var_key]
else:
    print(f"Variable {var_key} not found")
    exit()

with open(paper_data_file, 'r') as f:
    papers = json.load(f)

# Extract information from papers
paper_info = []
for paper in papers:
    # Extract title from filename
    title = paper['filename'].replace('.txt', '')
    
    # Extract year from text - look for patterns like 2015, 2016, etc.
    year = None
    year_match = re.search(r"(201[5-9]|202[0-9])", paper['text'])
    if year_match:
        year = int(year_match.group(1))
    
    # Extract contribution - check if 'empirical' appears in text
    contribution = 'unknown'
    text_lower = paper['text'].lower()
    if 'empirical' in text_lower:
        contribution = 'empirical'
    elif 'artifact' in text_lower:
        contribution = 'artifact'
    elif 'theoretical' in text_lower:
        contribution = 'theoretical'
    elif 'survey' in text_lower:
        contribution = 'survey'
    elif 'methodological' in text_lower:
        contribution = 'methodological'
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_info)
print(f"Total papers: {len(df_papers)}")
print(f"Year distribution: {df_papers['year'].value_counts().sort_index().to_dict()}")
print(f"Contribution distribution: {df_papers['contribution'].value_counts().to_dict()}")

# Filter papers: empirical contribution and published after 2016
filtered_papers = df_papers[
    (df_papers['contribution'] == 'empirical') & 
    (df_papers['year'] > 2016)
]

print(f"Found {len(filtered_papers)} empirical papers after 2016")
if len(filtered_papers) > 0:
    print("First few filtered papers:")
    for idx, paper in filtered_papers.head(3).iterrows():
        print(f"  - {paper['title']} ({paper['year']})")

# Prepare result
result = filtered_papers[['title', 'year']].to_dict('records')

----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps(result))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
