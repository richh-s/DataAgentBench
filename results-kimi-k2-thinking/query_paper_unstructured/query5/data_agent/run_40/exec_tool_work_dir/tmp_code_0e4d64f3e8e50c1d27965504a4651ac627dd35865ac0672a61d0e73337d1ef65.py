code = """import json
import pandas as pd

# Load the CHI papers and citations data from previous queries
chi_papers_data = locals().get('var_functions.query_db:18', [])
citations_2020_data = locals().get('var_functions.query_db:0', [])

# Load CHI papers if it's a file path
if isinstance(chi_papers_data, str) and chi_papers_data.endswith('.json'):
    with open(chi_papers_data, 'r') as f:
        chi_papers = json.load(f)
else:
    chi_papers = chi_papers_data

# Load citations if it's a file path  
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

print(f"CHI papers: {len(chi_titles)}")
print("CHI titles:")
for t in chi_titles[:5]:
    print(f"  - {t}")

# Create citations DataFrame
citations_df = pd.DataFrame(citations_2020)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

# Check which CHI papers have citation records
citation_titles = set(citations_df['title'].tolist())
chi_citation_titles = [t for t in chi_titles if t in citation_titles]

print(f"\nCHI papers with citation records: {len(chi_citation_titles)}")

# Get citation counts for CHI papers in 2020
chi_2020_citations = []
total_citations = 0
for title in chi_citation_titles:
    citation_rows = citations_df[citations_df['title'] == title]
    for _, row in citation_rows.iterrows():
        count = row['citation_count']
        chi_2020_citations.append({
            'title': title,
            'citation_count': count,
            'citation_year': row['citation_year']
        })
        total_citations += count

print(f"Sample CHI citations in 2020:")
for citation in chi_2020_citations[:5]:
    print(f"  {citation['title']}: {citation['citation_count']} citations")

print(f"\nTotal citations for CHI papers in 2020: {total_citations}")

# Create final result
result = {
    'total_citations': total_citations,
    'total_chi_papers_with_citations': len(chi_2020_citations),
    'sample_citations': chi_2020_citations[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'status': 'success', 'total_records': 100, 'message': 'Loaded 100 citation records for 2020'}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_papers': 5}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_chi_papers': 5, 'chi_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'venue': 'CHI', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'venue': 'CHI', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'venue': 'CHI', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'venue': 'CHI', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'venue': 'CHI', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}}

exec(code, env_args)
