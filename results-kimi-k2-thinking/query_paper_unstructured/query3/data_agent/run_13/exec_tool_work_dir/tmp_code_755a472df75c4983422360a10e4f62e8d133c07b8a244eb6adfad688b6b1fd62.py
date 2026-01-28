code = """import json
import re
import pandas as pd

# Load the data
papers_file = locals()['var_functions.query_db:46']
citations_file = locals()['var_functions.query_db:14']

with open(papers_file, 'r') as f:
    papers = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

print('=== DATA OVERVIEW ===')
print('Papers:', len(papers))
print('Citations:', len(citations))

# Debug: Check first paper structure
print('\nFirst paper keys:', list(papers[0].keys()))
print('First paper filename:', papers[0]['filename'])
print('First paper text (first 200 chars):', papers[0]['text'][:200])

# Step 1: Analyze all papers for year patterns and empirical mentions
paper_analysis = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract years using multiple methods
    years_found = []
    
    # Method 1: Full years like 2015, 2016, 2020
    full_years = re.findall(r"\b(20[0-9]{2})\b", text)
    for y in full_years:
        year_int = int(y)
        if 2000 <= year_int <= 2030:
            years_found.append(year_int)
    
    # Method 2: Conference format like '15, '16, '17
    short_years = re.findall(r"'([0-9]{2})\b", text)
    for y in short_years:
        year_int = int('20' + y)
        if 2000 <= year_int <= 2030:
            years_found.append(year_int)
    
    # Get most recent year
    year = max(years_found) if years_found else None
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Sample some papers for debugging
    if len(paper_analysis) < 3:
        print(f"\nSample paper {len(paper_analysis) + 1}:")
        print(f"  Title: {title}")
        print(f"  Years found: {years_found}")
        print(f"  Selected year: {year}")
        print(f"  Has empirical: {has_empirical}")
    
    paper_analysis.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'years_found': years_found
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_analysis)

print('\n=== PAPER ANALYSIS RESULTS ===')
print('Total papers:', len(df_papers))
print('Years found:', df_papers['year'].notna().sum())
print('Year distribution:')
print(df_papers['year'].value_counts().sort_index().to_dict())

print('\nEmpirical papers:', df_papers['has_empirical'].sum())
print('Empirical by year:')
empirical_by_year = df_papers[df_papers['has_empirical'] == True]['year'].value_counts().sort_index()
print(empirical_by_year.to_dict())

# Check papers with no year
no_year = df_papers[df_papers['year'].isna()]
print(f'\nPapers with no year detected: {len(no_year)}')

# Filter empirical papers after 2016
empirical_after_2016 = df_papers[
    (df_papers['has_empirical'] == True) & 
    (df_papers['year'] > 2016)
]

print('\nEmpirical papers after 2016:', len(empirical_after_2016))
if len(empirical_after_2016) > 0:
    print('Titles:')
    for title in empirical_after_2016['title'].tolist():
        print('-', title)
else:
    print('No empirical papers found after 2016')
    print('Checking for ANY empirical papers...')
    any_empirical = df_papers[df_papers['has_empirical'] == True]
    print(f'Found {len(any_empirical)} empirical papers total')
    if len(any_empirical) > 0:
        print('Years for empirical papers:')
        print(any_empirical['year'].value_counts().sort_index().to_dict())

# Step 2: Check citations
print('\n=== CITATIONS ANALYSIS ===')
df_citations = pd.DataFrame(citations)
print('Citations columns:', df_citations.columns.tolist())
print('First few citation records:')
for i, row in enumerate(citations[:3]):
    print(f"  {i+1}. {row}")

# Check if 'total_citations' column exists
if 'total_citations' in df_citations.columns:
    df_citations['total_citations'] = df_citations['total_citations'].astype(int)
    print('Total citation records:', len(citations))
    print('Unique papers with citations:', df_citations['title'].nunique())
    print('Sample citation titles:', df_citations['title'].head().tolist())
else:
    print('ERROR: total_citations column not found')
    print('Available columns:', df_citations.columns.tolist())

result = {
    'empirical_after_2016': len(empirical_after_2016),
    'total_empirical': len(any_empirical) if len(empirical_after_2016) == 0 else None,
    'empirical_titles': empirical_after_2016['title'].tolist() if len(empirical_after_2016) > 0 else any_empirical['title'].tolist() if len(any_empirical) > 0 else []
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}}

exec(code, env_args)
