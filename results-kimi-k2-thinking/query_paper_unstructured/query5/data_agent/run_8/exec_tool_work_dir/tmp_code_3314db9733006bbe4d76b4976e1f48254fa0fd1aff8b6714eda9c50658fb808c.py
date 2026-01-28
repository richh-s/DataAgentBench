code = """import json
import pandas as pd
import re

# Load the 2020 citations from the file
citations_file_path = '/tmp/tmp_z5f1h1u.json'
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

print(f'Number of citations in 2020: {len(citations_2020)}')

# Load the papers from the file (this is the full paper_docs collection)
papers_file_path = '/tmp/tmp1_jn5t0d.json'
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

print(f'Number of papers: {len(papers)}')

# Process papers to extract title and check if CHI venue
chi_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if CHI venue by looking in the text for CHI conference mentions
    text = paper.get('text', '')
    # Look for patterns like "CHI 'YY", "CHI 20YY", "CHI Conference", etc.
    chi_patterns = [
        r"CHI\s*'\d{2}",
        r"CHI\s*20\d{2}",
        r"CHI\s+Conference",
        r"Proceedings of the .*CHI",
        r"ACM .*CHI"
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        chi_papers.append({'title': title, 'filename': filename})

print(f'Number of CHI papers: {len(chi_papers)}')

# Create DataFrames
citations_df = pd.DataFrame(citations_2020)
chi_papers_df = pd.DataFrame(chi_papers)

if not chi_papers_df.empty:
    # Merge on title
    merged_df = pd.merge(chi_papers_df, citations_df, on='title', how='inner')
    print(f'Number of CHI papers with 2020 citations: {len(merged_df)}')
    
    if not merged_df.empty:
        # Convert citation_count to numeric
        merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'], errors='coerce')
        total_citations = merged_df['citation_count'].sum()
        print(f'Total citations for CHI papers in 2020: {total_citations}')
        
        # Show some examples
        print('\nTop CHI papers by 2020 citations:')
        top_papers = merged_df.nlargest(5, 'citation_count')[['title', 'citation_count']]
        print(top_papers.to_string(index=False))
        
        # Also show papers with no citations
        chi_papers_with_citations = set(merged_df['title'])
        chi_papers_without_citations = chi_papers_df[~chi_papers_df['title'].isin(chi_papers_with_citations)]
        print(f'\nCHI papers without 2020 citations: {len(chi_papers_without_citations)}')
    else:
        print('No CHI papers found in 2020 citations')
        total_citations = 0
else:
    print('No CHI papers found')
    total_citations = 0

# Print final result
print('__RESULT__:')
print(json.dumps({"total_citations": int(total_citations), "chi_papers_count": len(chi_papers)}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
