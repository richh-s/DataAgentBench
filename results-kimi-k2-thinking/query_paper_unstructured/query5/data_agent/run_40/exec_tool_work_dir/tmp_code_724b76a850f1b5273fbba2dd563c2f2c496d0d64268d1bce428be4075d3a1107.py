code = """import json
import pandas as pd

# Load all CHI papers from MongoDB query
chi_papers_data = locals().get('var_functions.query_db:18', [])
if isinstance(chi_papers_data, str) and chi_papers_data.endswith('.json'):
    with open(chi_papers_data, 'r') as f:
        chi_papers = json.load(f)
else:
    chi_papers = chi_papers_data

# Load all 2020 citations
all_citations_data = locals().get('var_functions.query_db:28', [])
if isinstance(all_citations_data, str) and all_citations_data.endswith('.json'):
    with open(all_citations_data, 'r') as f:
        all_citations_2020 = json.load(f)
else:
    all_citations_2020 = all_citations_data

# Extract CHI paper titles
chi_titles = []
for doc in chi_papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    chi_titles.append(title)

# Create citations DataFrame
citations_df = pd.DataFrame(all_citations_2020)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

# Find CHI papers with citations in 2020
chi_citations = citations_df[citations_df['title'].isin(chi_titles)]

# Calculate total citations
total_citations = chi_citations['citation_count'].sum()
num_papers = len(chi_citations)

# Create detailed result
result = {
    'total_citations': int(total_citations),
    'chi_papers_with_citations': int(num_papers),
    'papers': chi_citations[['title', 'citation_count']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'status': 'success', 'total_records': 100, 'message': 'Loaded 100 citation records for 2020'}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_papers': 5}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_chi_papers': 5, 'chi_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'venue': 'CHI', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'venue': 'CHI', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'venue': 'CHI', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'venue': 'CHI', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'venue': 'CHI', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}, 'var_functions.execute_python:24': {'total_citations': 243, 'papers_with_citations': 4}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
