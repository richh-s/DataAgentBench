code = """import json

# Access the stored data
db_result_28 = globals()['var_functions.query_db:28']
db_result_29 = globals()['var_functions.query_db:29']

chi_papers = db_result_28
citations_file_path = db_result_29

# Load full citations data from the file
with open(citations_file_path, 'r') as f:
    full_citations = json.load(f)

# Extract CHI paper titles
chi_paper_titles = [paper['filename'].replace('.txt', '') for paper in chi_papers]

print(f"Found {len(chi_paper_titles)} papers from CHI venue")
print(f"Looking for CHI titles in {len(full_citations)} citation records...")

chi_citation_count = 0
chi_papers_found = []

# Match titles and sum citations
for citation in full_citations:
    citation_title = citation['title']
    if citation_title in chi_paper_titles:
        count = int(citation['citation_count'])
        chi_citation_count += count
        chi_papers_found.append({
            'title': citation_title,
            'citations_2020': count
        })

chi_papers_found.sort(key=lambda x: x['citations_2020'], reverse=True)

print(f"Found {len(chi_papers_found)} CHI papers in citation data")
print(f"Total citation count for CHI papers in 2020: {chi_citation_count}")

# Prepare final answer
answer = {
    'total_citation_count': chi_citation_count,
    'papers_matched': len(chi_papers_found),
    'citation_details': chi_papers_found
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json'}

exec(code, env_args)
