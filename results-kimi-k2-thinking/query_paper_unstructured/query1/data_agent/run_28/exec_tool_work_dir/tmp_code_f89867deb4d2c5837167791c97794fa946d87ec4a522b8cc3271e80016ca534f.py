code = """import json
import pandas as pd
import re

# Access the variables
paper_docs = locals()['var_functions.query_db:22']
citations = locals()['var_functions.query_db:2']

# Load data if needed
if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)
if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

print('Total papers:', len(paper_docs))
print('Total citations:', len(citations))

# Extract detailed paper info
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year from text (look for patterns like 2015, '15, etc.)
    year = ''
    year_match = re.search(r'(20\d{2})', text)
    if year_match:
        year = year_match.group(1)
    
    # Extract venue from text (common HCI venues)
    text_upper = text.upper()
    venue = ''
    venues = ['CHI', 'UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 'WWW', 'IUI', 'OZCHI', 'TEI', 'AH']
    for v in venues:
        if v in text_upper:
            venue = v
            break
    
    # Extract source
    source = ''
    if 'ACM' in text_upper:
        source = 'ACM'
    elif 'IEEE' in text_upper:
        source = 'IEEE'
    elif 'PubMed'.upper() in text_upper:
        source = 'PubMed'
    
    # Extract domain
    text_lower = text.lower()
    domains = []
    if 'food' in text_lower or 'eating' in text_lower or 'diet' in text_lower:
        domains.append('food')
    if 'physical activity' in text_lower or 'exercise' in text_lower or 'fitness' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower or 'stress' in text_lower or 'mood' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower or 'financial' in text_lower:
        domains.append('finances')
    
    domain_str = ', '.join(domains) if domains else ''
    
    paper_info.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain_str
    })

papers_df = pd.DataFrame(paper_info)
print('\nPaper domains found:')
print(papers_df['domain'].value_counts())

# Check food papers specifically
food_papers = papers_df[papers_df['domain'].str.contains('food', na=False)]
print('\nNumber of food papers:', len(food_papers))
print('Food papers titles:')
for _, paper in food_papers.iterrows():
    print(f"- {paper['title']}")

# Process citations
citations_df = pd.DataFrame(citations)
print('\nCitation data columns:', citations_df.columns.tolist())
print('Sample citation titles:')
print(citations_df['title'].head(10).tolist())

# Simple matching by exact title (after normalizing)
food_titles = set(food_papers['title'].tolist())
citation_titles = set(citations_df['title'].tolist())

common_titles = food_titles.intersection(citation_titles)
print('\nCommon titles found:', len(common_titles))

# Calculate total citations for food papers
total_food_citations = 0
for title in common_titles:
    paper_citations = citations_df[citations_df['title'] == title]
    total_food_citations += paper_citations['citation_count'].astype(int).sum()

print('Total food citations:', total_food_citations)

# Alternative: fuzzy matching
from difflib import get_close_matches

matched_food_citations = 0
match_count = 0

for _, paper in food_papers.iterrows():
    paper_title = paper['title']
    matches = get_close_matches(paper_title, list(citation_titles), n=1, cutoff=0.85)
    if matches:
        matched_citations = citations_df[citations_df['title'] == matches[0]]
        citation_sum = matched_citations['citation_count'].astype(int).sum()
        matched_food_citations += citation_sum
        match_count += 1

print('\nUsing fuzzy matching:')
print('Matched papers:', match_count)
print('Total citations:', matched_food_citations)

result = {"total_citation_count": int(matched_food_citations), "matched_papers": match_count}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)
