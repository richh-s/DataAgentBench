code = """import json
import re

# Load citation data for 2020
citations_file = var_functions.query_db:2
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Extract CHI papers from documents
chi_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    # Extract title from filename
    title = filename.replace('.txt', '')
    # Check if it's a CHI paper by looking for CHI venue in text
    if re.search(r'\bCHI\b', text, re.IGNORECASE):
        chi_papers.append(title)

# Create a set for faster lookup
chi_paper_titles = set(chi_papers)

# Filter citations for CHI papers and sum citation counts
total_citations = 0
chi_citations = []

for citation in citations_2020:
    title = citation['title']
    if title in chi_paper_titles:
        count = int(citation['citation_count'])
        total_citations += count
        chi_citations.append({
            'title': title,
            'citation_count': count,
            'citation_year': citation['citation_year']
        })

print('__RESULT__:', json.dumps({
    'total_citations_2020': total_citations,
    'chi_papers_count': len(chi_paper_titles),
    'chi_citations_matched': len(chi_citations)
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
