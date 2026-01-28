code = """import pandas as pd
import json
import re

# Read the full JSON data from the file
with open(locals()['var_function-call-7068351369592816242'], 'r') as f:
    paper_docs_data = json.load(f)

# Prepare a list to store extracted paper information
papers_info = []

# Iterate through each paper document and extract relevant information
for doc in paper_docs_data:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    year = None
    contribution = None

    # Extract year (robust regex for "YYYY" in the first 500 characters)
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:500])
    if year_match:
        year = int(year_match.group(0))

    # Extract contribution (case-insensitive search for 'contribution:' followed by keywords)
    contribution_match = re.search(r'contribution:\s*([^\n]+)', text, re.IGNORECASE)
    if contribution_match:
        contribution_text = contribution_match.group(1).lower()
        if 'empirical' in contribution_text:
            contribution = 'empirical'

    # Only add papers with a valid year and empirical contribution
    if year and contribution == 'empirical':
        papers_info.append({
            'title': title,
            'year': year,
            'contribution': contribution
        })

# Create a DataFrame from the extracted information
papers_df = pd.DataFrame(papers_info)

# Filter for papers published after 2016
filtered_papers_df = papers_df[papers_df['year'] > 2016]

# Convert the filtered DataFrame to JSON string
print('__RESULT__:')
print(filtered_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-18434242260745944216': ['paper_docs'], 'var_function-call-7068351369592816242': 'file_storage/function-call-7068351369592816242.json', 'var_function-call-2782461426140013972': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6837708904110415217': 'file_storage/function-call-6837708904110415217.json'}

exec(code, env_args)
