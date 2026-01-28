code = """import json
import re

# Access the variables
citations_file_path = locals()['var_functions.query_db:18']
chi_papers = locals()['var_functions.query_db:19']

# Load the citations data from the file path
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Now process the data
# Extract CHI paper titles (remove .txt extension)
chi_titles = []
for paper in chi_papers:
    filename = paper['filename']
    title = filename[:-4] if filename.endswith('.txt') else filename
    chi_titles.append(title)

chi_titles_set = set(chi_titles)

# Match citations with CHI papers
total_citations = 0
matched = []

for citation in citations_2020:
    citation_title = citation['title']
    if citation_title in chi_titles_set:
        count = int(citation['citation_count'])
        total_citations += count
        matched.append({
            'title': citation_title,
            'count': count
        })

result = {
    'total_citations_2020_for_chi_papers': total_citations,
    'number_of_chi_papers_cited': len(matched),
    'papers': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'citations_count': 188, 'papers_count': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'citations_type': "<class 'str'>", 'chi_type': "<class 'list'>", 'citations_sample': 'file_storage/functions.query_db:18.json', 'chi_sample': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}]}}

exec(code, env_args)
