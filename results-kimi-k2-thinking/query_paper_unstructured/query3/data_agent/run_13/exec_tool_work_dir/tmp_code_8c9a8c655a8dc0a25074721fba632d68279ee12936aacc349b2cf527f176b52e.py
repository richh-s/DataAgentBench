code = """import json
import re
import pandas as pd

# Load papers data
papers_path = locals()['var_functions.query_db:46']
papers = json.load(open(papers_path))

# Load citations data
citations_path = locals()['var_functions.query_db:14']
citations = json.load(open(citations_path))

print('=== OVERVIEW ===')
print('Papers:', len(papers))
print('Citations:', len(citations))

# Analyze papers for empirical contributions and years
paper_list = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Extract year
    year = None
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical
    is_empirical = 'empirical' in text.lower()
    
    paper_list.append([title, year, is_empirical])

# Create DataFrame
df = pd.DataFrame(paper_list, columns=['title', 'year', 'is_empirical'])

print('\n=== PAPER ANALYSIS ===')
year_counts = df['year'].value_counts().sort_index()
print('Year distribution (2015+):')
for year, count in year_counts.items():
    if year >= 2015:
        print(str(year) + ': ' + str(count))

print('\nEmpirical papers:', df['is_empirical'].sum())
empirical_by_year = df[df['is_empirical'] == True]['year'].value_counts().sort_index()
print('Empirical by year:')
for year, count in empirical_by_year.items():
    if year >= 2015:
        print(str(year) + ': ' + str(count))

# Filter empirical papers after 2016
empirical_2017plus = df[(df['is_empirical'] == True) & (df['year'] > 2016)]
print('\nEmpirical papers after 2016:', len(empirical_2017plus))

# Get titles for citation lookup
titles = empirical_2017plus['title'].tolist()
print('Titles:', titles)

# Process citations
df_citations = pd.DataFrame(citations)
print('\n=== CITATIONS ===')
print('Columns:', df_citations.columns.tolist())

# Match papers with citations
final_results = []
if len(titles) > 0:
    matching = df_citations[df_citations['title'].isin(titles)]
    print('Matching citations found:', len(matching))
    
    # Add year info and prepare results
    for _, paper in empirical_2017plus.iterrows():
        title = paper['title']
        year = paper['year']
        
        # Find citations for this paper
        paper_citations = matching[matching['title'] == title]
        if len(paper_citations) > 0:
            total_citations = int(paper_citations.iloc[0]['total_citations'])
            final_results.append({
                'title': title,
                'year': year,
                'total_citations': total_citations
            })

print('\nFinal results:', len(final_results))
result = {'papers': final_results}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}}

exec(code, env_args)
