code = """import json
import pandas as pd

# Load CHI papers
chi_papers_data = locals().get('var_functions.query_db:18', [])
if isinstance(chi_papers_data, str) and chi_papers_data.endswith('.json'):
    with open(chi_papers_data, 'r') as f:
        chi_papers = json.load(f)
else:
    chi_papers = chi_papers_data

# Load citations 2020
citations_2020_data = locals().get('var_functions.query_db:0', [])
if isinstance(citations_2020_data, str) and citations_2020_data.endswith('.json'):
    with open(citations_2020_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_2020_data

# Extract CHI paper titles
chi_titles = []
for doc in chi_papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    chi_titles.append(title)

# Create citations DataFrame
citations_df = pd.DataFrame(citations_2020)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

# Find intersection of CHI papers and citation records
citation_titles = set(citations_df['title'].tolist())
chi_citation_titles = [t for t in chi_titles if t in citation_titles]

# Sum up citations for CHI papers in 2020
chi_citations_2020 = citations_df[citations_df['title'].isin(chi_citation_titles)]
total_citations = chi_citations_2020['citation_count'].sum()
num_papers = len(chi_citation_titles)

result = {
    'total_citations': int(total_citations),
    'papers_with_citations': int(num_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'status': 'success', 'total_records': 100, 'message': 'Loaded 100 citation records for 2020'}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_papers': 5}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_chi_papers': 5, 'chi_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'venue': 'CHI', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'venue': 'CHI', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'venue': 'CHI', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'venue': 'CHI', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'venue': 'CHI', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}}

exec(code, env_args)
