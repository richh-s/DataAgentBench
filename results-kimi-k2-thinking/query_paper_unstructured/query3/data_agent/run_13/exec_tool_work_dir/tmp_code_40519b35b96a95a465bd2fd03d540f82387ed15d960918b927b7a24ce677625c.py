code = """import json
import re
import pandas as pd

# Load the full papers data from MongoDB
papers_path = locals()['var_functions.query_db:46']
papers_data = json.load(open(papers_path))

# Load the full citations data from SQLite
citations_path = locals()['var_functions.query_db:14']
citations_data = json.load(open(citations_path))

print('=== DATA LOADED ===')
print(f'Papers: {len(papers_data)} documents')
print(f'Citations: {len(citations_data)} records')

# Analyze the papers structure
print(f'\nPaper keys: {papers_data[0].keys()}')
print(f'Sample paper: {papers_data[0]["filename"]}')

# Extract paper metadata
paper_metadata = []
for paper in papers_data:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - look for 4-digit years 2000-2030
    year = None
    year_matches = re.findall(r"\b(20[0-2][0-9])\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical keyword
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'is_empirical': has_empirical
    })

df_papers = pd.DataFrame(paper_metadata)

print('\n=== PAPER YEAR DISTRIBUTION ===')
year_counts = df_papers['year'].value_counts().sort_index()
for year, count in year_counts.items():
    if year >= 2015 and year <= 2025:
        print(f'{year}: {count} papers')

print('\n=== EMPIRICAL PAPERS ===')
empirical_papers = df_papers[df_papers['is_empirical'] == True]
print(f'Total empirical papers: {len(empirical_papers)}')

# Show empirical papers by year
empirical_by_year = empirical_papers['year'].value_counts().sort_index()
for year, count in empirical_by_year.items():
    if year >= 2015 and year <= 2025:
        print(f'{year}: {count} empirical')

# Filter empirical papers after 2016
empirical_after_2016 = empirical_papers[empirical_papers['year'] > 2016]
print(f'\nEmpirical papers after 2016: {len(empirical_after_2016)}')

if len(empirical_after_2016) > 0:
    print('\n=== EMPIRICAL PAPERS AFTER 2016 ===')
    for _, paper in empirical_after_2016.iterrows():
        print(f"- {paper['title']} ({paper['year']})")
else:
    print('No empirical papers found after 2016')
    print('Let me check papers around 2017-2020:')
    recent_papers = df_papers[
        (df_papers['year'] >= 2017) & 
        (df_papers['year'] <= 2020)
    ]
    print(f'Recent papers (2017-2020): {len(recent_papers)}')
    recent_empirical = recent_papers[recent_papers['is_empirical'] == True]
    print(f'Recent empirical papers: {len(recent_empirical)}')

# Check citations data structure
print('\n=== CITATIONS ANALYSIS ===')
print(f'Citation sample: {citations_data[0]}')

df_citations = pd.DataFrame(citations_data)
print(f'Citation columns: {df_citations.columns.tolist()}')

# Check for papers that have citations
titles_to_check = empirical_after_2016['title'].tolist()
matching_citations = df_citations[df_citations['title'].isin(titles_to_check)]
print(f'Found {len(matching_citations)} matching citation records')

result = {
    'empirical_after_2016_count': len(empirical_after_2016),
    'empirical_after_2016_titles': empirical_after_2016['title'].tolist() if len(empirical_after_2016) > 0 else [],
    'all_empirical_count': len(empirical_papers),
    'matching_citations_count': len(matching_citations)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}]}

exec(code, env_args)
