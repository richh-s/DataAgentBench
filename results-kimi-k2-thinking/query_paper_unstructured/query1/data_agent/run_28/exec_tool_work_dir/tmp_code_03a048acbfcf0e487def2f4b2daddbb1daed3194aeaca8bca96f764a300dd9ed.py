code = """import json

# Access stored results using string keys
paper_docs_var = locals()['var_functions.query_db:3']
citations_var = locals()['var_functions.query_db:2']

# Check if these are file paths (strings ending with .json) or direct data
if isinstance(paper_docs_var, str) and paper_docs_var.endswith('.json'):
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
    print('Loaded paper_docs from file')
else:
    paper_docs = paper_docs_var
    print('Used paper_docs directly')

if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations = json.load(f)
    print('Loaded citations from file')
else:
    citations = citations_var
    print('Used citations directly')

# Show basic info
print(f'\nNumber of papers: {len(paper_docs)}')
print(f'Number of citations: {len(citations)}')

# Show a sample
if paper_docs:
    print(f'\nSample paper filename: {paper_docs[0].get("filename", "N/A")}')
if citations:
    print(f'Sample citation: {citations[0]}')

# Extract paper titles and domains
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract domain info (check if 'food' appears in the text as per HINTS)
    domain = ''
    if 'food' in text.lower() or 'eating' in text.lower() or 'diet' in text.lower():
        domain = 'food'
    elif 'physical activity' in text.lower() or 'exercise' in text.lower() or 'fitness' in text.lower():
        domain = 'physical activity'
    elif 'sleep' in text.lower():
        domain = 'sleep'
    elif 'mental' in text.lower() or 'stress' in text.lower() or 'mood' in text.lower():
        domain = 'mental'
    elif 'finances' in text.lower() or 'financial' in text.lower():
        domain = 'finances'
    elif 'productivity' in text.lower():
        domain = 'productivity'
    elif 'screen time' in text.lower():
        domain = 'screen time'
    
    paper_info.append({'title': title, 'domain': domain})

# Convert to DataFrame for easier manipulation
import pandas as pd
papers_df = pd.DataFrame(paper_info)
citations_df = pd.DataFrame(citations)

print(f'\nPapers with domain info: {len(papers_df)}')
print(f'Papers by domain:', papers_df['domain'].value_counts())

# Match citations with paper titles
citations_df['title_clean'] = citations_df['title'].str.strip()

# Perform fuzzy matching (in case titles differ slightly)
from difflib import get_close_matches

total_food_citations = 0
matched_papers = []

for _, paper in papers_df[papers_df['domain'] == 'food'].iterrows():
    paper_title = paper['title']
    # Find close matches in citations
    matches = get_close_matches(paper_title, citations_df['title_clean'].tolist(), n=1, cutoff=0.8)
    
    if matches:
        matched_citations = citations_df[citations_df['title_clean'] == matches[0]]
        paper_citations_count = matched_citations['citation_count'].astype(int).sum()
        total_food_citations += paper_citations_count
        matched_papers.append({
            'title': paper_title,
            'citation_count': paper_citations_count
        })

print(f'\nTotal citation count for food papers: {total_food_citations}')
print(f'Number of matched food papers: {len(matched_papers)}')

__RESULT__ = str(total_food_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
