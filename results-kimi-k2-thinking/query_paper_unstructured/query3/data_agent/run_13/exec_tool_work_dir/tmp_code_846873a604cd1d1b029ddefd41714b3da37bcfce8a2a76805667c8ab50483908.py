code = """import json
import re
import pandas as pd
import os

# Load papers data from MongoDB file
papers_file = locals()['var_functions.query_db:46']
print('Loading papers from:', papers_file)

with open(papers_file, 'r') as f:
    papers = json.load(f)

# Load citations data from SQLite file
citations_file = locals()['var_functions.query_db:84']
print('Loading citations from:', citations_file)

with open(citations_file, 'r') as f:
    citations = json.load(f)

print('=== DATA LOADED ===')
print('Papers:', len(papers))
print('Citation samples:', len(citations))

# Analyze papers to find empirical contributions published after 2016
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract publication year (look for 4-digit years like 2017, 2018, etc.)
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    year = None
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check if paper mentions empirical contribution (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'is_empirical': has_empirical
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_metadata)

# Show analysis results
print('\n=== PAPER ANALYSIS ===')
print('Total papers:', len(df_papers))
print('Papers with extracted year:', df_papers['year'].notna().sum())
print('Year range detected:', df_papers['year'].min(), 'to', df_papers['year'].max())

# Show year distribution
year_counts = df_papers['year'].value_counts().sort_index()
print('\nPapers by year (recent years):')
for year, count in year_counts.items():
    if 2015 <= year <= 2025:
        print(f'  {year}: {count} papers')

print('\nTotal empirical papers found:', df_papers['is_empirical'].sum())

# Show empirical papers by year
empirical_by_year = df_papers[df_papers['is_empirical'] == True]['year'].value_counts().sort_index()
print('\nEmpirical papers by year:')
for year, count in empirical_by_year.items():
    if 2015 <= year <= 2025:
        print(f'  {year}: {count} empirical papers')

# Filter papers: empirical contribution AND published after 2016
empirical_after_2016 = df_papers[
    (df_papers['is_empirical'] == True) & 
    (df_papers['year'] > 2016)
].copy()

print('\n=== FILTERED EMPIRICAL PAPERS AFTER 2016 ===')
print(f'Count: {len(empirical_after_2016)}')

if len(empirical_after_2016) > 0:
    print('\nThese papers will be checked for citations:')
    for idx, paper in empirical_after_2016.iterrows():
        print(f"  - {paper['title']} ({paper['year']})")
else:
    print('No empirical papers found after 2016. Let me check all empirical papers...')
    all_empirical = df_papers[df_papers['is_empirical'] == True]
    print(f'Total empirical papers: {len(all_empirical)}')
    print('Years:', all_empirical['year'].value_counts().sort_index().to_dict())

# Get titles to check in citation database
titles_to_check = empirical_after_2016['title'].tolist()
print(f'\nChecking {len(titles_to_check)} papers for citations...')

# Process citations data
df_citations = pd.DataFrame(citations)
print(f'Citation data shape: {df_citations.shape}')
print(f'Citation columns: {df_citations.columns.tolist()}')

# Convert citation_count to int
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Group by title to get total citations per paper
total_citations_per_paper = df_citations.groupby('title')['citation_count'].sum().reset_index(name='total_citations')

print(f'Total unique papers in citations: {len(total_citations_per_paper)}')

# Match our empirical papers with citations
matching_papers = total_citations_per_paper[total_citations_per_paper['title'].isin(titles_to_check)]

print(f'Matching papers found in citations: {len(matching_papers)}')

# Merge with paper year data
if len(matching_papers) > 0:
    final_results = pd.merge(
        matching_papers,
        empirical_after_2016[['title', 'year']],
        on='title',
        how='inner'
    )
    
    # Sort by total citations descending
    final_results = final_results.sort_values('total_citations', ascending=False)
    
    print('\n=== FINAL RESULTS ===')
    print(f'Total papers found: {len(final_results)}')
    
    # Display results
    for _, row in final_results.iterrows():
        print(f"{row['title']} ({row['year']}): {row['total_citations']} total citations")
    
    # Prepare data for output
    output_data = final_results[['title', 'total_citations', 'year']].to_dict('records')
else:
    print('No empirical papers after 2016 found with citation data')
    output_data = []

print('\n__RESULT__:')
print(json.dumps(output_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_functions.query_db:92': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}]}

exec(code, env_args)
