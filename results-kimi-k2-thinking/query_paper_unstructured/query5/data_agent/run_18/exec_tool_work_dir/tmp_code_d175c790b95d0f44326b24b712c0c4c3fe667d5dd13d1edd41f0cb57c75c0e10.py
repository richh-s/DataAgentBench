code = """import json

# Load the full 2020 citations data
citations_file_path = locals()['var_functions.query_db:7']
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Load the full paper documents data
paper_docs_file_path = locals()['var_functions.query_db:14']
with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

# Create a set of available paper titles
paper_titles = set(doc.get('filename', '').replace('.txt', '') for doc in paper_docs)

print(f'Available paper titles in paper_docs: {len(paper_titles)}')
for title in sorted(paper_titles):
    print(f'  - {title}')

print(f'\nTotal citations in 2020: {len(citations_2020)}')

# Find which 2020-cited papers are in our paper_docs collection
found_citations = []
missing_citations = []

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in paper_titles:
        found_citations.append(citation_title)
    else:
        missing_citations.append(citation_title)

print(f'\n2020-cited papers found in paper_docs: {len(found_citations)}')
print(f'2020-cited papers NOT in paper_docs: {len(missing_citations)}')

# Check if any of the missing papers might be CHI papers
# Since we can't determine venue for missing papers, we can only report on what we have

# For the papers we have, check which are CHI and their citations
chi_papers_with_citations = []

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in paper_titles:
        # Check if it's a CHI paper
        for doc in paper_docs:
            if doc.get('filename', '').replace('.txt', '') == citation_title:
                text = doc.get('text', '')
                if 'CHI' in text:
                    chi_papers_with_citations.append({
                        'title': citation_title,
                        'citations': int(citation.get('citation_count', 0))
                    })

total_chi_citations = sum(p['citations'] for p in chi_papers_with_citations)

print(f'\nCHI papers cited in 2020: {len(chi_papers_with_citations)}')
print(f'Total citations for CHI papers in 2020: {total_chi_citations}')
print('\nCHI papers and their citation counts:')
for paper in chi_papers_with_citations:
    print(f"  - {paper['title']}: {paper['citations']}")

result = {
    'total_chi_citations_2020': total_chi_citations,
    'num_chi_papers_cited': len(chi_papers_with_citations),
    'available_paper_docs': len(paper_titles),
    'total_2020_citations': len(citations_2020),
    'papers_found_in_collection': len(found_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:10': 188, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'paper_docs_count': 5, 'citations_2020_count': 188}, 'var_functions.execute_python:20': {'citations_2020_count': 188, 'paper_docs_count': 5}, 'var_functions.execute_python:26': {'total_chi_citations_2020': 243, 'num_chi_papers_cited': 4}, 'var_functions.execute_python:30': {'total_citations': 243, 'paper_count': 4, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 16}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citations': 77}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citations': 98}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': 52}]}}

exec(code, env_args)
