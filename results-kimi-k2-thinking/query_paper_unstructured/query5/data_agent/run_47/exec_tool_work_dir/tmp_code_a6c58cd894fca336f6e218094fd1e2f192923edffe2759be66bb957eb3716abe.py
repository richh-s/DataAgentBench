code = """import json

# Read some sample data to understand patterns
citations_file = locals()['var_functions.query_db:0']
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

papers_file = locals()['var_functions.query_db:4']
papers_data = []
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Sample the data to see what's there
print('Sample of citation titles:')
for i, citation in enumerate(citations_data[:10]):
    print(f"  {i+1}. {citation['title']}")

print('\nSample of paper filenames:')
for i, paper in enumerate(papers_data[:10]):
    print(f"  {i+1}. {paper['filename']}")

# Check if any papers have CHI in their text
chi_papers_samples = []
for paper in papers_data[:20]:
    if 'CHI' in paper['text'][:2000]:
        chi_papers_samples.append({
            'filename': paper['filename'],
            'text_snippet': paper['text'][:500]
        })

print(f"\nFound {len(chi_papers_samples)} papers with CHI in first 2000 chars:")
for i, paper in enumerate(chi_papers_samples[:5]):
    print(f"  {i+1}. {paper['filename']}")
    print(f"     Snippet: {paper['text_snippet'][:200]}")

result = {'sample_citations': len(citations_data), 'sample_papers': len(papers_data)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}, 'var_functions.execute_python:14': {'total_citation_count': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:16': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'matched_papers_sample': []}, 'var_functions.execute_python:20': {'total_citation_count': 0, 'papers_analyzed': 188, 'chi_papers_identified': 0, 'chi_papers': []}, 'var_functions.execute_python:22': {'total_citations_for_chi_papers_in_2020': 0, 'number_of_chi_papers_cited': 0}}

exec(code, env_args)
