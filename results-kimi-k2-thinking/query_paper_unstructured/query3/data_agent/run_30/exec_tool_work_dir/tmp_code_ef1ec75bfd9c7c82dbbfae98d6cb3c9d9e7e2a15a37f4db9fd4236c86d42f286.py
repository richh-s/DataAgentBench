code = """import json
import re

# Load paper documents data
paper_docs_file = '/tmp/tmsnz4d9.json'  # This should be the path from var_functions.query_db:22
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load citation data
citations_file = '/tmp/tm2t6n9n.json'  # This should be the path from var_functions.query_db:24
with open(citations_file, 'r') as f:
    citations = json.load(f)

print(f"Paper documents: {len(paper_docs)}")
print(f"Citation totals: {len(citations)}")

# Process papers
papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    # Look for conference patterns
    patterns = [
        r"(?:UbiComp|CHI|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth)\s+'?(\d{2})\b",
        r"(?:20\d{2})",
        r"'?(\d{2})\b.*?\b(20\d{2})\b"
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                if isinstance(match, tuple):
                    year_str = match[1] if len(match) > 1 else match[0]
                else:
                    year_str = match
                
                if year_str.startswith('20'):
                    year_candidate = int(year_str)
                else:
                    year_val = int(year_str)
                    year_candidate = 2000 + year_val if year_val < 50 else 1900 + year_val
                
                if 2000 <= year_candidate <= 2100:
                    year = year_candidate
                    break
            if year:
                break
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

print(f"Processed {len(papers)} papers")
print("Sample:", papers[0])

# Create citations lookup
citations_dict = {c['title']: int(c['total_citations']) for c in citations}

# Find empirical papers after 2016
results = []
for p in papers:
    if p['has_empirical'] and p['year'] and p['year'] > 2016:
        citations = citations_dict.get(p['title'], 0)
        if citations > 0:
            results.append({
                'title': p['title'],
                'total_citations': citations
            })

print(f"Found {len(results)} empirical papers after 2016 with citations")
print("__RESULT__:")
print(json.dumps(results[:20]))  # Return first 20"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
