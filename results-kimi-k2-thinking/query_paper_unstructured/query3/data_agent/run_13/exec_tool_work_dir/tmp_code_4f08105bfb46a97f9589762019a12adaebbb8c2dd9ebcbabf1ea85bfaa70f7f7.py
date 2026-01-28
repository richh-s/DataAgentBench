code = """import json
import re
import pandas as pd

# Load data
papers_path = locals()['var_functions.query_db:46']
citations_path = locals()['var_functions.query_db:84']

with open(papers_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Debug: Show what we have
print('Papers:', len(papers))
print('Citations:', len(citations))
print('\nSample citation:', citations[0] if citations else 'No data')

# Process papers to find empirical papers after 2016
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year
    year = None
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

df_papers = pd.DataFrame(paper_metadata)

# Statistics
print('\n=== PAPER STATISTICS ===')
print('Total papers:', len(df_papers))
print('Papers with detected year:', df_papers['year'].notna().sum())
print('Year range:', df_papers['year'].min(), 'to', df_papers['year'].max())

# Show year distribution for recent years
year_counts = df_papers['year'].value_counts().sort_index()
print('\nYear distribution (2015+):')
for year, count in year_counts.items():
    if year >= 2015:
        print(f'  {year}: {count} papers')

print('\nTotal empirical papers:', df_papers['has_empirical'].sum())

# Show empirical by year
empirical_counts = df_papers[df_papers['has_empirical'] == True]['year'].value_counts().sort_index()
print('\nEmpirical papers by year:')
for year, count in empirical_counts.items():
    if year >= 2015:
        print(f'  {year}: {count} papers')

# Filter empirical papers after 2016
filtered_papers = df_papers[
    (df_papers['has_empirical'] == True) & 
    (df_papers['year'] > 2016)
].copy()

print('\nFiltered empirical papers after 2016:', len(filtered_papers))
if len(filtered_papers) > 0:
    print('Years for filtered papers:', filtered_papers['year'].value_counts().sort_index().to_dict())
    print('\nTitles:')
    for title in filtered_papers['title'].tolist():
        print('-', title)
else:
    print('No empirical papers found after 2016')
    print('Let me check ALL papers to see what years are available...')
    print('\nAll papers by year:')
    for year, count in df_papers['year'].value_counts().sort_index().items():
        print(f'  {year}: {count}')

result = {
    'filtered_papers': len(filtered_papers),
    'titles': filtered_papers['title'].tolist() if len(filtered_papers) > 0 else []
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}]}

exec(code, env_args)
