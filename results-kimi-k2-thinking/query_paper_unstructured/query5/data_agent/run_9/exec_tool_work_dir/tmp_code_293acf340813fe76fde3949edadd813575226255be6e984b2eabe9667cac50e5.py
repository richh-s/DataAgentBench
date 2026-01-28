code = """import json
import re

# Load citation data for 2020
citation_file_path = locals()['var_functions.query_db:4']
with open(citation_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
paper_file_path = locals()['var_functions.query_db:6']
with open(paper_file_path, 'r') as f:
    paper_docs = json.load(f)

# Create a list to store paper information
paper_info = []

for doc in paper_docs:
    # Extract title from filename (remove .txt extension)
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    text = doc['text']
    
    # Search for venue information - look for CHI mentions
    # Common patterns for CHI papers
    chi_patterns = [
        r'CHI\s*\'\d{2}',  # CHI '15, CHI '16, etc.
        r'CHI\s*\d{4}',   # CHI 2015, CHI 2016, etc.
        r'Conference on Human Factors in Computing Systems',
        r'Proceedings of the .*CHI',
        r'ACM.*CHI'
    ]
    
    venue = None
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = 'CHI'
            break
    
    if venue == 'CHI':
        paper_info.append({
            'title': title,
            'venue': venue
        })

# Create a dictionary for easy lookup of citation counts
citation_dict = {item['title']: int(item['citation_count']) for item in citations_2020}

# Find CHI papers that have citation data in 2020
total_citations = 0
chi_papers_with_citations = []

for paper in paper_info:
    title = paper['title']
    if title in citation_dict:
        citation_count = citation_dict[title]
        total_citations += citation_count
        chi_papers_with_citations.append({
            'title': title,
            'citation_count': citation_count
        })

# Print the result in the required format
result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(chi_papers_with_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
