code = """import json

# Load and parse the citation data
citation_file = locals()['var_functions.query_db:2']
paper_file = locals()['var_functions.query_db:6']

# Read the entire JSON arrays
citation_data = []
with open(citation_file, 'r') as f:
    content = f.read().strip()
    citation_data = json.loads(content)

paper_data = []
with open(paper_file, 'r') as f:
    content = f.read().strip()
    paper_data = json.loads(content)

# Create a set of CHI paper titles
chi_titles = set()
for doc in paper_data:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Check if this is a CHI paper by looking for CHI in the text
    if text and 'chi' in text.lower():
        chi_titles.add(title)

# Sum up citations for CHI papers in 2020
total_citations = 0
chi_papers_cited = 0

for citation in citation_data:
    title = citation.get('title', '')
    if title in chi_titles:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        chi_papers_cited += 1

result = {
    'total_citation_count': total_citations,
    'chi_papers_count': chi_papers_cited
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
