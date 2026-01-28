code = """import json

# Load citations data (2020 citations)
citations_file = locals()['var_functions.query_db:26']
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load CHI papers data
chi_papers_file = locals()['var_functions.query_db:19']
with open(chi_papers_file, 'r') as f:
    chi_papers = json.load(f)

# Extract titles of CHI papers (remove .txt extension from filename)
chi_titles = []
for paper in chi_papers:
    filename = paper['filename']
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
    else:
        title = filename
    chi_titles.append(title)

# Create a set for faster lookup
chi_titles_set = set(chi_titles)

# Find CHI papers that have citations in 2020 and sum the counts
total_citations = 0
matched_papers = []

for citation in citations_2020:
    cite_title = citation['title']
    if cite_title in chi_titles_set:
        count = int(citation['citation_count'])
        total_citations += count
        matched_papers.append({
            'title': cite_title,
            'citation_count': count
        })

# Return the result
result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(matched_papers),
    'matched_papers': matched_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'citations_count': 188, 'papers_count': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
