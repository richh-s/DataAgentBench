code = """import json
import re
import pandas as pd

# Load papers data
with open(locals()['var_functions.query_db:46']) as f:
    papers = json.load(f)

# Load citations data
with open(locals()['var_functions.query_db:14']) as f:
    citations = json.load(f)

print('=== DATA SETUP ===')
print('Papers:', len(papers))
print('Citations:', len(citations))

# Analyze papers
paper_data = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year
    year = None
    years = re.findall(r"\b(20[0-9]{2})\b", text)
    if years:
        valid = [int(y) for y in years if 2000 <= int(y) <= 2030]
        if valid:
            year = max(valid)
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    paper_data.append({'title': title, 'year': year, 'has_empirical': has_empirical})

df_papers = pd.DataFrame(paper_data)

print('\n=== PAPERS ANALYSIS ===')
print('Year range:', df_papers['year'].min(), 'to', df_papers['year'].max())
print('Year distribution:')
year_counts = df_papers['year'].value_counts().sort_index()
for year, count in year_counts.items():
    if year >= 2015:  # Recent years
        print(f"  {year}: {count} papers")

print('\nEmpirical papers:', df_papers['has_empirical'].sum())

# Check empirical by year
empirical_by_year = df_papers[df_papers['has_empirical'] == True]['year'].value_counts().sort_index()
print('Empirical papers by year:')
for year, count in empirical_by_year.items():
    if year >= 2015:
        print(f"  {year}: {count} empirical papers")

# Filter empirical papers after 2016
empirical_2017plus = df_papers[(df_papers['has_empirical'] == True) & (df_papers['year'] > 2016)]
print('\nEmpirical papers after 2016:', len(empirical_2017plus))

# List them
if len(empirical_2017plus) > 0:
    print('Titles:')
    for title in empirical_2017plus['title'].tolist():
        print('-', title)
else:
    print('No empirical papers found after 2016. Showing all empirical papers:')
    all_empirical = df_papers[df_papers['has_empirical'] == True]
    if len(all_empirical) > 0:
        print('All empirical papers:')
        for year, count in all_empirical['year'].value_counts().sort_index().items():
            print(f'  {year}: {count} papers')
        
        print('\nAll empirical titles:')
        for title in all_empirical['title'].tolist():
            print('-', title)

# Prepare citation lookup
titles_for_citations = empirical_2017plus['title'].tolist() if len(empirical_2017plus) > 0 else []

print('\n=== CITATIONS ANALYSIS ===')
df_citations = pd.DataFrame(citations)
print('Columns:', df_citations.columns.tolist())
print('First entry:', citations[0] if citations else 'No data')

result = {
    'empirical_after_2016': len(empirical_2017plus),
    'titles_for_citation_lookup': titles_for_citations,
    'all_empirical_count': len(df_papers[df_papers['has_empirical'] == True])
}

print('__RESULT__:')
json_result = json.dumps(result, indent=2)
print(json_result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}}

exec(code, env_args)
