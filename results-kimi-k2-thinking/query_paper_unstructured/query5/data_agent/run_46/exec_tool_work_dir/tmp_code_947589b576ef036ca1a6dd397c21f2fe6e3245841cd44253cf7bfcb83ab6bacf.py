code = """import json
import re

# Load citation data for 2020
citations_file = locals()['var_functions.query_db:2']
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
papers_file = locals()['var_functions.query_db:5']
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary mapping titles to paper documents for faster lookup
# Title from filename (without .txt extension)
papers_dict = {}
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    papers_dict[title] = doc

# Now find CHI papers among the papers that have citations in 2020
chi_citations = []
total_citations = 0

for citation in citations_2020:
    title = citation['title']
    if title in papers_dict:
        paper_doc = papers_dict[title]
        text = paper_doc['text']
        
        # Check if this is a CHI paper by looking for CHI in the text
        # Look for patterns like CHI, CHI Conference, CHI '20, etc.
        if re.search(r'CHI', text, re.IGNORECASE):
            count = int(citation['citation_count'])
            total_citations += count
            chi_citations.append({
                'title': title,
                'citation_count': count,
                'citation_year': citation['citation_year']
            })

result_data = {
    'total_citations_chi_2020': total_citations,
    'chi_papers_with_citations': len(chi_citations),
    'total_chi_papers_in_db': len([doc for doc in paper_docs if re.search(r'CHI', doc['text'], re.IGNORECASE)])
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_citations_2020': 0, 'chi_papers_count': 0, 'chi_citations_matched': 0}}

exec(code, env_args)
