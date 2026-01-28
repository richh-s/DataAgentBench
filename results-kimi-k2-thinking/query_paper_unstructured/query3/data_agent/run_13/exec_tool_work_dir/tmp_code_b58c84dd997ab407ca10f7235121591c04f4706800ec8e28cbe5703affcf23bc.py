code = """import json
import re
import pandas as pd

# Load papers data
papers_path = locals()['var_functions.query_db:46']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations data  
citations_path = locals()['var_functions.query_db:84']
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Loaded', len(papers), 'papers and', len(citations), 'citations')

# Extract paper metadata
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
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({'title': title, 'year': year, 'empirical': has_empirical})

df_papers = pd.DataFrame(paper_metadata)

# Statistics
print('Papers by year:')
year_counts = df_papers['year'].value_counts().sort_index()
for year, count in year_counts.items():
    if year >= 2015:
        print(str(year) + ': ' + str(count) + ' papers')

print('\nEmpirical papers:', df_papers['empirical'].sum())

# Filter empirical papers after 2016
filtered = df_papers[(df_papers['empirical'] == True) & (df_papers['year'] > 2016)]
print('Empirical papers after 2016:', len(filtered))

# Get titles for citation lookup
titles = filtered['title'].tolist()
years = filtered['year'].tolist()
print('Titles found:', len(titles))

# Match with citations
df_citations = pd.DataFrame(citations)
final_results = []

for i in range(len(titles)):
    title = titles[i]
    year = years[i]
    
    # Find citation record
    citation_rows = df_citations[df_citations['title'] == title]
    if not citation_rows.empty:
        total_citations = int(citation_rows.iloc[0]['citation_count'])
        final_results.append({'title': title, 'year': year, 'total_citations': total_citations})

print('Final results count:', len(final_results))

# Format output
output = json.dumps(final_results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}]}

exec(code, env_args)
