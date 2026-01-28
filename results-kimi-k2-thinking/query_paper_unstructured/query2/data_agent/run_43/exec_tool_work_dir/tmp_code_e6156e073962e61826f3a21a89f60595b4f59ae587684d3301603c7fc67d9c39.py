code = """import json
import re

# Load the paper documents
papers_file = locals()['var_functions.query_db:2']
paper_docs = []
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Function to extract paper information from text
acm_pattern = r'ACM|Association for Computing Machinery'
acm_papers = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if text contains ACM indicators
    if re.search(acm_pattern, text, re.IGNORECASE):
        # Extract publication year from text
        year_match = re.search(r"'(\d{2})|\b(20\d{2})\b", text)
        year = None
        if year_match:
            year_str = year_match.group(0)
            if year_str.startswith("'"):
                year = int('20' + year_str[1:])  # Convert '15 to 2015
            else:
                year = int(year_str)
        
        # Extract venue (conference/journal)
        venue = 'Unknown'
        venue_patterns = [
            r"(CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?\d{2}|\d{4}",
            r"Proceedings of the (.*?) Conference",
            r"ACM (.*?) Conference"
        ]
        
        for pattern in venue_patterns:
            venue_match = re.search(pattern, text)
            if venue_match:
                venue = venue_match.group(1) if venue_match.lastindex else venue_match.group(0)
                break
        
        acm_papers.append({
            'title': title,
            'publisher': 'ACM',
            'year': year,
            'venue': venue,
            'id': doc.get('_id')
        })

print('__RESULT__:')
print(json.dumps({
    'acm_papers': acm_papers,
    'acm_count': len(acm_papers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'citations_2018_count': 158, 'paper_docs_count': 5}}

exec(code, env_args)
