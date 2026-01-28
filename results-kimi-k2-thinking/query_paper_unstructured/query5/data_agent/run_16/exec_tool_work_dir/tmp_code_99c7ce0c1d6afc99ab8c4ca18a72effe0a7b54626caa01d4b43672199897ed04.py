code = """import json
import os

# Get the data from stored variables
citations_data = locals()['var_functions.query_db:6']
paper_docs_data = locals()['var_functions.query_db:2']

# Check if data is stored as file path strings
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)
        
if isinstance(paper_docs_data, str) and os.path.exists(paper_docs_data):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

# Filter citations for 2020
citations_2020 = [c for c in citations_data if int(c.get('citation_year', 0)) == 2020]

print('Total citation records:', len(citations_data))
print('Citations in 2020:', len(citations_2020))

# Show sample citation titles
if citations_2020:
    print('Sample 2020 citation titles:')
    for c in citations_2020[:3]:
        print('  -', c['title'])

# Process paper docs to find CHI papers
chi_paper_titles = set()

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '').strip()
    
    # Check if this is a CHI paper by looking for CHI in text or filename
    is_chi = False
    
    # Check if text contains CHI conference indicators
    text_upper = text.upper()
    chi_indicators = [' CHI ', "CHI '", 'CHI20', 'CHI 20', 'CHI19', 'CHI 19', 'CHI18', 'CHI 18']
    for indicator in chi_indicators:
        if indicator in text_upper or indicator in text:
            is_chi = True
            break
    
    # Check filename for CHI
    if 'chi' in filename.lower():
        is_chi = True
    
    if is_chi:
        chi_paper_titles.add(title)

print('\nIdentified CHI papers:', len(chi_paper_titles))
if chi_paper_titles:
    print('Sample CHI paper titles:')
    for t in list(chi_paper_titles)[:5]:
        print('  -', t)

__result__ = {"chi_papers_identified": len(chi_paper_titles), "citations_2020_count": len(citations_2020)}
print('__RESULT__:')
print(json.dumps(__result__))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'status': 'data_loaded'}}

exec(code, env_args)
