code = """import json
import re

# Get the citations data from storage
citations_key = 'var_functions.query_db:2'
citations_file = locals()[citations_key]

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Get the paper docs data from storage
paper_docs_key = 'var_functions.query_db:5'
paper_docs_file = locals()[paper_docs_key]

with open(paper_docs_file, 'r') as f:
    paper_docs_data = json.load(f)

# Process paper docs to find CHI papers
chi_titles = set()

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check if this is a CHI paper by looking for CHI in the text
    text_start = text[:2000].upper()
    if 'CHI' in text_start:
        # Additional check to avoid false positives
        chi_indicators = ['PROCEEDINGS OF THE SIGCHI', 'ACM CHI', 'CHI ', 'CHI\'']
        for indicator in chi_indicators:
            if indicator in text_start:
                chi_titles.add(title)
                break

# Sum citations for CHI papers from 2020
total_citations = 0
matched_count = 0

for citation in citations_data:
    citation_title = citation.get('title', '')
    citation_count_str = citation.get('citation_count', '0')
    
    try:
        citation_count = int(citation_count_str)
    except:
        citation_count = 0
    
    if citation_title in chi_titles:
        total_citations += citation_count
        matched_count += 1

result = {
    'total_citation_count': total_citations,
    'matched_papers': matched_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
