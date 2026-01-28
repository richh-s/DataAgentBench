code = """import json
import re

# Read the CHI papers data
chi_papers_file = var_functions.query_db:14
with open(chi_papers_file, 'r') as f:
    chi_papers_data = json.load(f)

# Read the 2020 citations data
citations_2020_file = var_functions.query_db:15
with open(citations_2020_file, 'r') as f:
    citations_2020_data = json.load(f)

# Create a dictionary for fast lookup of citation counts by title
citations_dict = {}
for citation in citations_2020_data:
    title = citation.get('title', '').lower().strip()
    count = int(citation.get('citation_count', 0))
    citations_dict[title] = count

# Process CHI papers and find their 2020 citations
total_citations = 0
chi_papers_with_citations = []

for paper in chi_papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    title_key = title.lower().strip()
    
    # Check if this paper has citations in 2020
    if title_key in citations_dict:
        citation_count = citations_dict[title_key]
        if citation_count > 0:
            total_citations += citation_count
            chi_papers_with_citations.append({
                'title': title,
                'citation_count': citation_count
            })

# Sort by citation count descending
chi_papers_with_citations.sort(key=lambda x: x['citation_count'], reverse=True)

result = {
    'total_citations': total_citations,
    'number_of_chi_papers_cited': len(chi_papers_with_citations),
    'chi_papers': chi_papers_with_citations
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
