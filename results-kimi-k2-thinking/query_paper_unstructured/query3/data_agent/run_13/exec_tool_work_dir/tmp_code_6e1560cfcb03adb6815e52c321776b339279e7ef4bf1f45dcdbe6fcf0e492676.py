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

print('=== DATA LOADED ===')
print('Papers:', len(papers))
print('Citation samples:', len(citations))

# Extract paper metadata
metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Find all 4-digit years 2000-2030
    years = re.findall(r"\b(20[0-9]{2})\b", text)
    year = None
    if years:
        valid = [int(y) for y in years]
        if valid:
            year = max(valid)
    
    # Check for empirical keyword
    empirical = 'empirical' in text.lower()
    
    metadata.append([title, year, empirical])

# Create DataFrame
df = pd.DataFrame(metadata, columns=['title', 'year', 'empirical'])

# Show statistics
print('\nPaper Analysis:')
print('Total papers:', len(df))
print('Papers with year:', df['year'].notna().sum())

# Show recent years
year_counts = df['year'].value_counts().sort_index()
print('\nPapers by year (2015+):')
for year, count in year_counts.items():
    if year >= 2015 and year <= 2025:
        print('  ' + str(year) + ': ' + str(count))

print('\nTotal empirical papers:', df['empirical'].sum())

# Filter empirical papers after 2016
filtered = df[(df['empirical'] == True) & (df['year'] > 2016)]
print('Empirical papers after 2016:', len(filtered))

# Get titles and years
filter_titles = filtered['title'].tolist()
filter_years = filtered['year'].tolist()

# Process citations
citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

# Group by title for total citations
paper_citations = citations_df.groupby('title')['citation_count'].sum().reset_index()
paper_citations = paper_citations.rename(columns={'citation_count': 'total_citations'})

# Merge results
final_data = []
for i in range(len(filter_titles)):
    title = filter_titles[i]
    year = filter_years[i]
    
    # Find citation record
    matching = paper_citations[paper_citations['title'] == title]
    if not matching.empty:
        total_cites = int(matching.iloc[0]['total_citations'])
        final_data.append({'title': title, 'year': year, 'total_citations': total_cites})

print('Results with citations:', len(final_data))

# Prepare output
output = json.dumps(final_data)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_functions.query_db:92': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}]}

exec(code, env_args)
