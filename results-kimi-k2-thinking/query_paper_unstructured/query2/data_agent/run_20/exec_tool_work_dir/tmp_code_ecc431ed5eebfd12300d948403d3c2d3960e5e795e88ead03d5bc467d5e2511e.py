code = """import json

# Load the 2018 citations data from the file
citations_file = locals()['var_functions.query_db:0']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load the ACM papers data from the file
acm_papers_file = locals()['var_functions.query_db:2']
with open(acm_papers_file, 'r') as f:
    acm_papers = json.load(f)

# Create a dictionary from ACM papers for quick lookup by filename (without .txt)
acm_papers_dict = {}
for paper in acm_papers:
    filename = paper['filename']
    # Remove .txt extension to match with citation titles
    title = filename.replace('.txt', '')
    acm_papers_dict[title] = paper

# Find citation records that match ACM papers
matched_citations = []
for citation in citations_data:
    citation_title = citation['title']
    if citation_title in acm_papers_dict:
        matched_citations.append({
            'title': citation_title,
            'citation_count': int(citation['citation_count']),
            'citation_year': citation['citation_year']
        })

# Calculate average citation count
if matched_citations:
    total_citations = sum(c['citation_count'] for c in matched_citations)
    average_citation = total_citations / len(matched_citations)
    result = {
        'average_citation_count': round(average_citation, 2),
        'total_matched_papers': len(matched_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_matched_papers': 0,
        'message': 'No matching papers found'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
