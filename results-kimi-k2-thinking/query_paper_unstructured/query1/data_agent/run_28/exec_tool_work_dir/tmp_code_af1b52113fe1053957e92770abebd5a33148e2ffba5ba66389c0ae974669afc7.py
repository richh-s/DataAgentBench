code = """import json
import pandas as pd
from difflib import get_close_matches

# Load data from storage
paper_docs_path = locals()['var_functions.query_db:22']
citations_path = locals()['var_functions.query_db:2']

# Load paper documents
if isinstance(paper_docs_path, str) and paper_docs_path.endswith('.json'):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_path

# Load citations
if isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_path

# Extract paper information (title and domain)
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '').lower()
    
    # Determine domain based on text content
    domain = ''
    if 'food' in text or 'eating' in text or 'diet' in text:
        domain = 'food'
    elif 'physical activity' in text or 'exercise' in text or 'fitness' in text:
        domain = 'physical activity'
    elif 'sleep' in text:
        domain = 'sleep'
    elif 'mental' in text or 'stress' in text or 'mood' in text:
        domain = 'mental'
    elif 'finances' in text or 'financial' in text:
        domain = 'finances'
    elif 'productivity' in text:
        domain = 'productivity'
    elif 'screen time' in text:
        domain = 'screen time'
    
    paper_info.append({'title': title, 'domain': domain})

papers_df = pd.DataFrame(paper_info)
citations_df = pd.DataFrame(citations)

# Identify food papers
food_papers = papers_df[papers_df['domain'] == 'food']
print('Number of food papers found:', len(food_papers))

# Filter out food papers with citations
citations_df['title_clean'] = citations_df['title'].str.strip()
total_citations = 0
matched_count = 0

for _, paper in food_papers.iterrows():
    paper_title = paper['title']
    matches = get_close_matches(paper_title, citations_df['title_clean'].tolist(), n=1, cutoff=0.8)
    
    if matches:
        matched_citations = citations_df[citations_df['title_clean'] == matches[0]]
        citation_sum = matched_citations['citation_count'].astype(int).sum()
        total_citations += citation_sum
        matched_count += 1

print('Total citations for food papers:', total_citations)
print('Number of matched food papers:', matched_count)

result = {"total_citation_count": int(total_citations)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
