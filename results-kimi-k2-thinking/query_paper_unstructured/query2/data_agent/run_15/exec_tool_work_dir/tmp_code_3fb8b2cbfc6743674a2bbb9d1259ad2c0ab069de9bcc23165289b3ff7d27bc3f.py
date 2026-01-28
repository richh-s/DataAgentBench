code = """import json
import re

# Load the full citations data
citations_file_path = locals()['var_functions.query_db:9']
with open(citations_file_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the full paper documents
papers_file_path = locals()['var_functions.query_db:5']
with open(papers_file_path, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping from title to paper info
title_to_paper = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    text = doc.get('text', '')
    
    # Extract publication year
    year_match = re.search(r'\b(20\d{2})\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract venue (e.g., CHI, Ubicomp)
    venue_match = re.search(r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['’]?\d{2}", text, re.IGNORECASE)
    venue = venue_match.group(1).upper() if venue_match else None
    
    # Extract source/publisher (look for ACM, IEEE, PubMed)
    source = None
    if 'ACM' in text or 'acm.org' in text:
        source = 'ACM'
    elif 'IEEE' in text or 'ieee.org' in text:
        source = 'IEEE'
    elif 'PubMed' in text:
        source = 'PubMed'
    
    title_to_paper[title] = {
        'source': source,
        'year': year,
        'venue': venue
    }

# Filter citations for ACM papers published before or in 2018
acm_citations_2018 = []
matched_count = 0
unmatched_count = 0

for citation in citations_2018:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    if title in title_to_paper:
        paper = title_to_paper[title]
        if paper['source'] == 'ACM' and paper['year'] and paper['year'] <= 2018:
            acm_citations_2018.append({
                'title': title,
                'citation_count': citation_count,
                'paper_year': paper['year'],
                'venue': paper['venue'],
                'source': paper['source']
            })
            matched_count += 1
    else:
        unmatched_count += 1

print('__RESULT__:')
print(json.dumps({
    'total_citations_2018': len(citations_2018),
    'matched_papers': matched_count,
    'unmatched_papers': unmatched_count,
    'acm_papers_2018': len(acm_citations_2018),
    'acm_papers_sample': acm_citations_2018[:5]
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'citations_2018_count': 158, 'paper_docs_count': 5}}

exec(code, env_args)
