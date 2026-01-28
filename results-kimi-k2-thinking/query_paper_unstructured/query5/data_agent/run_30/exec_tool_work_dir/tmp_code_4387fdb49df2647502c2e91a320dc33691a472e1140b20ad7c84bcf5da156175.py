code = """# Load and analyze the paper data to find CHI papers
import json
import re

# Access the full paper documents data
papers_data = locals().get('var_functions.query_db:9')

# Load from file if needed
if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Let's check how many papers we have and find CHI papers
print(f'Total papers in database: {len(paper_docs)}')

# Look for CHI papers by checking text for venue patterns
chi_papers = []
chi_titles = []

patterns = [
    r'\bCHI\b[\s\'\u2019]\d{2}',
    r'Proceedings of CHI',
    r'Proceedings of the SIGCHI',
    r'CHI Conference',
    r'ACM CHI'
]

chi_count = 0
sample_papers = []

for paper in paper_docs[:200]:  # Check first 200 papers to start
    text = paper.get('text', '')[:2000]  # Check first 2000 chars (header area)
    filename = paper.get('filename', '')
    
    # Check for CHI venue patterns
    is_chi = False
    if re.search(r'\bCHI\b', text):
        # Check if it's a venue marker, not just a word in the text
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                is_chi = True
                break
        
        # Also check specific location in text (usually near the beginning)
        if not is_chi:
            # Check if CHI appears in first 500 chars
            first_500 = text[:500]
            if re.search(r'\bCHI\b', first_500):
                # Exclude some false positives
                if not any(x in filename.lower() for x in ['ubicomp', 'chi-square', 'chi_phi']):
                    is_chi = True
    
    if is_chi:
        chi_count += 1
        title = filename.replace('.txt', '')
        chi_titles.append(title)
        chi_papers.append(paper)
        
        if chi_count <= 5:
            sample_papers.append({
                'title': title,
                'header_preview': text[:200].replace('\n', ' ')
            })

print(f'Found {chi_count} potential CHI papers')
print('Sample papers:')
for sp in sample_papers:
    print(f"- {sp['title']}")
    print(f"  Header: {sp['header_preview'][:150]}")"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_cited_in_2020': 0, 'sample_papers': []}}

exec(code, env_args)
