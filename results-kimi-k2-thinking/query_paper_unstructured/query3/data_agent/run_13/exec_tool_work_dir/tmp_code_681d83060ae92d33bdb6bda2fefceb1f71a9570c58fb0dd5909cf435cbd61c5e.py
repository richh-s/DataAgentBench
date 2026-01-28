code = """import json
import re
import pandas as pd

# Load papers data from the stored file path
papers_file_path = locals()['var_functions.query_db:46']
print('Papers file:', papers_file_path)

with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Load citations data from the stored file path  
citations_file_path = locals()['var_functions.query_db:84']
print('Citations file:', citations_file_path)

with open(citations_file_path, 'r') as f:
    citations = json.load(f)

print('=== DATA OVERVIEW ===')
print('Total papers loaded:', len(papers))
print('Total citation records:', len(citations))

# Extract metadata from papers
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract publication year (look for 4-digit years)
    year = None
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check if paper mentions empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_metadata)

# Show paper statistics
print('\n=== PAPER ANALYSIS ===')
print('Total papers analyzed:', len(df_papers))
print('Papers with extracted year:', df_papers['year'].notna().sum())
print('Year range:', df_papers['year'].min(), '-', df_papers['year'].max())

# Show year distribution
year_counts = df_papers['year'].value_counts().sort_index()
print('\nPapers by year:')
for year, count in year_counts.items():
    if 2015 <= year <= 2025:
        print('  ' + str(year) + ': ' + str(count) + ' papers')

print('\nTotal empirical papers:', df_papers['has_empirical'].sum())

# Show empirical by year
empirical_counts = df_papers[df_papers['has_empirical'] == True]['year'].value_counts().sort_index()
print('\nEmpirical papers by year:')
for year, count in empirical_counts.items():
    if 2015 <= year <= 2025:
        print('  ' + str(year) + ': ' + str(count) + ' empirical papers')

# Filter for papers with empirical contribution published after 2016
filtered_papers = df_papers[
    (df_papers['has_empirical'] == True) & 
    (df_papers['year'] > 2016)
]

print('\n=== FILTERED RESULTS ===')
print('Empirical papers after 2016:', len(filtered_papers))

if len(filtered_papers) > 0:
    print('Years for filtered papers:')
    for year, count in filtered_papers['year'].value_counts().sort_index().items():
        print('  ' + str(year) + ': ' + str(count))
    
    print('\nPaper titles:')
    for title in filtered_papers['title'].tolist():
        print('  - ' + title)
else:
    print('No empirical papers found after 2016')

# Get list of titles to check against citations
titles_to_check = filtered_papers['title'].tolist()
print('\nChecking ' + str(len(titles_to_check)) + ' papers for citations...')

# Process citations data
df_citations = pd.DataFrame(citations)
print('Citation data columns:', df_citations.columns.tolist())

# Convert citation_count to integer
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Group by title to get total citations per paper
paper_citations = df_citations.groupby('title')['citation_count'].sum().reset_index()
paper_citations = paper_citations.rename(columns={'citation_count': 'total_citations'})

print('Unique papers in citations database:', len(paper_citations))

# Find matching papers
matching_papers = paper_citations[paper_citations['title'].isin(titles_to_check)]
print('Matching papers found:', len(matching_papers))

# Merge with paper year information
if len(matching_papers) > 0:
    final_results = pd.merge(
        matching_papers,
        filtered_papers[['title', 'year']],
        on='title',
        how='inner'
    )
    
    # Sort by total citations
    final_results = final_results.sort_values('total_citations', ascending=False)
    
    print('\n=== FINAL RESULTS ===')
    print('Papers with citation data:', len(final_results))
    
    # Display results
    for idx, row in final_results.iterrows():
        print(row['title'] + ' (' + str(row['year']) + '): ' + str(row['total_citations']) + ' total citations')
    
    # Prepare output
    output_data = final_results[['title', 'total_citations', 'year']].to_dict('records')
else:
    print('No empirical papers after 2016 found with citation data')
    output_data = []

print('__RESULT__:')
print(json.dumps(output_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_functions.query_db:92': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}]}

exec(code, env_args)
