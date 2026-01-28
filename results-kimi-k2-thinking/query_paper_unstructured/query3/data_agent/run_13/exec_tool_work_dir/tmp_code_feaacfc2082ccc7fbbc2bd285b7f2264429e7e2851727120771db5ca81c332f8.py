code = """import json
import pandas as pd

# Load paper data from file
paper_data_file = var_functions.query_db:8
with open(paper_data_file, 'r') as f:
    papers = json.load(f)

# Extract title from filename
for paper in papers:
    paper['title'] = paper['filename'].replace('.txt', '')

print(f"Loaded {len(papers)} papers")
print(f"Sample paper: {papers[0]['title']}")
print(f"Sample paper year in text: {papers[0]['text'][:500]}")

# Look for year patterns in the text
import re

def extract_year(text):
    # Look for year patterns like 2015, 2016, 2017, 2018, 2019, 2020 etc.
    year_match = re.search(r"(201[5-9]|202[0-9])", text)
    if year_match:
        return int(year_match.group(1))
    return None

def extract_contribution(text):
    # Look for contribution keywords - check if 'empirical' appears
    text_lower = text.lower()
    if 'empirical' in text_lower:
        return 'empirical'
    elif 'artifact' in text_lower:
        return 'artifact'
    elif 'theoretical' in text_lower:
        return 'theoretical'
    elif 'survey' in text_lower:
        return 'survey'
    elif 'methodological' in text_lower:
        return 'methodological'
    return 'unknown'

# Extract information from papers
paper_info = []
for paper in papers:
    year = extract_year(paper['text'])
    contribution = extract_contribution(paper['text'])
    paper_info.append({
        'title': paper['title'],
        'year': year,
        'contribution': contribution,
        'text_preview': paper['text'][:200]
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_info)
print(f"\nPaper data extracted:")
print(df_papers.head())
print(f"\nYear distribution:")
print(df_papers['year'].value_counts().head())
print(f"\nContribution distribution:")
print(df_papers['contribution'].value_counts())

# Filter papers: empirical contribution and published after 2016
filtered_papers = df_papers[
    (df_papers['contribution'] == 'empirical') & 
    (df_papers['year'] > 2016)
]

print(f"\nFound {len(filtered_papers)} empirical papers after 2016")
if len(filtered_papers) > 0:
    print("Filtered papers:")
    print(filtered_papers[['title', 'year', 'contribution']].head())

result_json = filtered_papers[['title', 'year', 'contribution']].to_json(orient='records')
----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(result_json)
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
