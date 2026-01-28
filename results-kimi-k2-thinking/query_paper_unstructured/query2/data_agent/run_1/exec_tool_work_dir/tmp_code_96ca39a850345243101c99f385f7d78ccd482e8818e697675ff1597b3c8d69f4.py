code = """import json

# Get the stored results
citations_2018_file = locals()['var_functions.query_db:0']
akm_papers_file = locals()['var_functions.query_db:22']

# Load the data
with open(citations_2018_file, 'r') as f:
    citations_2018 = json.load(f)

with open(akm_papers_file, 'r') as f:
    acm_papers = json.load(f)

# Create a mapping of paper titles from ACM papers
acm_titles = set()
for paper in acm_papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    acm_titles.add(title)

# Filter citations to only include ACM papers from 2018
acm_citations = []
for citation in citations_2018:
    citation_title = citation['title']
    if citation_title in acm_titles:
        acm_citations.append(int(citation['citation_count']))

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        "average_citation_count": round(avg_citations, 2),
        "total_acm_papers_cited_in_2018": len(acm_citations),
        "total_citations_2018": len(citations_2018)
    }
else:
    result = {
        "average_citation_count": 0,
        "total_acm_papers_cited_in_2018": 0,
        "total_citations_2018": len(citations_2018)
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': "['var_functions.query_db:0', '__builtins__', 'json', 'sys']", 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
