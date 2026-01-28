code = """import json
import pandas as pd
from difflib import get_close_matches

# Load paper documents
paper_docs_key = 'var_functions.query_db:22'
citations_key = 'var_functions.query_db:2'

paper_docs_path = locals()[paper_docs_key]
citations_path = locals()[citations_key]

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

# Extract paper info
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '').lower()
    
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

# Process citations data
if citations:
    citations_df = pd.DataFrame(citations)
    print('Citation keys:', list(citations_df.columns))
    print('First citation:', citations[0])
    
    # Convert citation_count to numeric
    if 'citation_count' in citations_df.columns:
        citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce')
    
    # Get food papers
    food_papers = papers_df[papers_df['domain'] == 'food']
    print('Food papers found:', len(food_papers))
    
    # Match with citations
    total_citations = 0
    matched_papers = 0
    
    citation_titles = citations_df['title'].tolist() if 'title' in citations_df.columns else []
    
    for _, paper in food_papers.iterrows():
        if citation_titles:
            matches = get_close_matches(paper['title'], citation_titles, n=1, cutoff=0.8)
            if matches:
                matched_citations = citations_df[citations_df['title'] == matches[0]]
                if 'citation_count' in matched_citations.columns:
                    citation_sum = matched_citations['citation_count'].sum()
                    total_citations += citation_sum
                    matched_papers += 1
    
    result = {"total_citation_count": int(total_citations), "matched_papers": matched_papers}
else:
    result = {"total_citation_count": 0, "matched_papers": 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
