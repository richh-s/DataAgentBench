code = """import json
import re
import pandas as pd

# Load papers data
papers_file = locals()['var_functions.query_db:46']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Load citations data
citations_file = locals()['var_functions.query_db:84']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print('=== DATA OVERVIEW ===')
print(f'Papers: {len(papers)}')
print(f'Citation records: {len(citations)}')

# Analyze papers for years and empirical mentions
paper_data = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract publication year
    year = None
    # Look for 4-digit years 2000-2030
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)  # Most recent year is likely publication year
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    paper_data.append({
        'title': title,
        'year': year,
        'is_empirical': has_empirical
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_data)

# Show statistics
print('\n=== PAPER ANALYSIS ===')
print(f'Total papers: {len(df_papers)}')
print(f'Papers with year detected: {df_papers["year"].notna().sum()}')
print(f'Year range: {df_papers["year"].min()} to {df_papers["year"].max()}')

# Show year distribution
year_counts = df_papers['year'].value_counts().sort_index()
print('\nPapers by year (2015-2025):')
for year, count in year_counts.items():
    if 2015 <= year <= 2025:
        print(f'  {year}: {count}')

print(f'\nTotal empirical papers: {df_papers["is_empirical"].sum()}')

# Show empirical papers by year
empirical_by_year = df_papers[df_papers['is_empirical'] == True]['year'].value_counts().sort_index()
print('\nEmpirical papers by year:')
for year, count in empirical_by_year.items():
    if 2015 <= year <= 2025:
        print(f'  {year}: {count}')

# Filter empirical papers published after 2016
empirical_after_2016 = df_papers[
    (df_papers['is_empirical'] == True) & 
    (df_papers['year'] > 2016)
].copy()

print(f'\n=== EMPIRICAL PAPERS AFTER 2016 ===')
print(f'Count: {len(empirical_after_2016)}')

if len(empirical_after_2016) > 0:
    print('\nTitles:')
    for idx, row in empirical_after_2016.iterrows():
        print(f"  - {row['title']} ({row['year']})")
    
    # Get titles for citation lookup
    titles_to_check = empirical_after_2016['title'].tolist()
else:
    print('No empirical papers found after 2016. Checking if any empirical papers exist...')
    all_empirical = df_papers[df_papers['is_empirical'] == True]
    print(f'Total empirical papers: {len(all_empirical)}')
    if len(all_empirical) > 0:
        print('Years for empirical papers:', all_empirical['year'].value_counts().sort_index().to_dict())
    titles_to_check = []

# Step 2: Process citations data
print('\n=== CITATIONS ANALYSIS ===')
df_citations = pd.DataFrame(citations)
print(f'Citation data columns: {df_citations.columns.tolist()}')
print(f'Sample record: {citations[0] if citations else "No data"}')

# Convert citation_count to int
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Group by title to get total citations per paper
total_citations = df_citations.groupby('title')['citation_count'].sum().reset_index(name='total_citations')

print(f'Unique papers with citations: {len(total_citations)}')

# Filter for our empirical papers
citations_for_empirical = total_citations[total_citations['title'].isin(titles_to_check)]

print(f'\nMatching empirical papers with citations: {len(citations_for_empirical)}')

# Step 3: Merge with paper year information
if len(citations_for_empirical) > 0:
    # Merge with paper data to get year
    final_results = pd.merge(
        citations_for_empirical,
        empirical_after_2016[['title', 'year']],
        on='title',
        how='inner'
    )
    
    # Sort by total citations
    final_results = final_results.sort_values('total_citations', ascending=False)
    
    print('\n=== FINAL RESULTS ===')
    print(f'Found {len(final_results)} papers with citation data')
    
    # Display results
    for _, row in final_results.iterrows():
        print(f"{row['title']} ({row['year']}): {row['total_citations']} citations")
    
    # Prepare output
    output = final_results[['title', 'total_citations', 'year']].to_dict('records')
else:
    print('No empirical papers after 2016 found with citation data')
    output = []

print('\n__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_functions.query_db:92': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}]}

exec(code, env_args)
