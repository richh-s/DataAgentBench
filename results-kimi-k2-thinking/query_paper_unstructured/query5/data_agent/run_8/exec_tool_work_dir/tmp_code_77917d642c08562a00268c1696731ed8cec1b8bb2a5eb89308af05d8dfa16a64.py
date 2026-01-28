code = """import json
import pandas as pd
import re

# Load the 2020 citations from the file
citations_file_path = var_functions.query_db:6
citations_2020 = []
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

print('Loaded 2020 citations, count:', len(citations_2020))

# Load the papers from the file
papers_file_path = var_functions.query_db:10
papers = []
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

print('Loaded papers, count:', len(papers))

# Process papers to extract titles and check if CHI venue
chi_paper_titles = []
chi_paper_details = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    text = paper.get('text', '')
    
    # Check for CHI venue patterns
    chi_patterns = [
        r'CHI\s*\'\d{2}',  # CHI '15
        r'CHI\s*20\d{2}',  # CHI 2015
        r'CHI\s+Conference',
        r'Proceedings of the .*CHI',
        r'ACM .*CHI'
    ]
    
    is_chi = any(re.search(pattern, text, re.IGNORECASE) for pattern in chi_patterns)
    
    if is_chi:
        chi_paper_titles.append(title)
        chi_paper_details.append({'title': title})

print('CHI papers found:', len(chi_paper_titles))

# Create DataFrames
citations_df = pd.DataFrame(citations_2020)

# Find CHI papers in 2020 citations
chi_in_citations = citations_df[citations_df['title'].isin(chi_paper_titles)]

if not chi_in_citations.empty:
    # Convert citation_count to numeric
    chi_in_citations['citation_count'] = pd.to_numeric(chi_in_citations['citation_count'], errors='coerce')
    total_citations = chi_in_citations['citation_count'].sum()
    
    result = {
        'total_citations': int(total_citations),
        'chi_papers_count': len(chi_paper_titles),
        'chi_papers_with_citations': len(chi_in_citations)
    }
    
    print('Top 5 CHI papers by 2020 citations:')
    top5 = chi_in_citations.nlargest(5, 'citation_count')[['title', 'citation_count']]
    print(top5.to_string(index=False))
else:
    result = {
        'total_citations': 0,
        'chi_papers_count': len(chi_paper_titles),
        'chi_papers_with_citations': 0
    }

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
