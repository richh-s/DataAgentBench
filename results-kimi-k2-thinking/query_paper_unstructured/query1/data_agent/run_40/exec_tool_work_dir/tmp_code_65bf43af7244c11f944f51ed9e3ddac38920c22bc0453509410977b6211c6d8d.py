code = """import json
import pandas as pd
import re

# Load paper documents from the file
paper_docs_file = locals()['var_functions.query_db:14']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load citation data from the file
citations_file = locals()['var_functions.query_db:2']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract title and domain from each paper document
paper_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Extract domain information - look for domain mentions in the text
    # Common domains from the hint: "food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"
    domains = []
    domain_keywords = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]
    
    text_lower = text.lower()
    for keyword in domain_keywords:
        if keyword in text_lower:
            domains.append(keyword)
    
    # Also check for "food" specifically in various contexts
    if 'food' in text_lower:
        domains.append('food')
    
    paper_info.append({
        'title': title,
        'domains': list(set(domains)),  # Remove duplicates
        'filename': filename
    })

# Create DataFrames
papers_df = pd.DataFrame(paper_info)
citations_df = pd.DataFrame(citations)

# Add a column to track papers with food domain
papers_df['is_food'] = papers_df['domains'].apply(lambda x: 'food' in x)

# Get titles of food papers
food_paper_titles = papers_df[papers_df['is_food']]['title'].tolist()

print('__RESULT__:')
print(json.dumps({
    "total_papers": len(paper_docs),
    "food_papers": len(food_paper_titles),
    "food_paper_titles": food_paper_titles,
    "sample_papers": papers_df[['title', 'domains', 'is_food']].head(3).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_citations': 1405, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies']}, 'var_functions.list_db:8': ['paper_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'paper_docs_count': 5, 'citations_count': 1405, 'sample_paper': 'A Lived Informatics Model of Personal Informatics.txt'}}

exec(code, env_args)
