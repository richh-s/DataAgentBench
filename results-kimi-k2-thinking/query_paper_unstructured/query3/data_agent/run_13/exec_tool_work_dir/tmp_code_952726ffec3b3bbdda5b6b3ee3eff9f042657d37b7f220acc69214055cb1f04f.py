code = """import json
import re
import pandas as pd

# Load papers and citations
papers_file = locals()['var_functions.query_db:46']
citations_file = locals()['var_functions.query_db:14']

with open(papers_file, 'r') as f:
    papers = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Loaded', len(papers), 'papers and', len(citations), 'citation records')

# Step 1: Extract paper metadata
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year
    year = None
    year_matches = re.findall(r'\b(20[0-9]{2})\b', text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({'title': title, 'year': year, 'has_empirical': has_empirical})

df_papers = pd.DataFrame(paper_metadata)
print('Total papers:', len(df_papers))
print('Year distribution:', df_papers['year'].value_counts().sort_index().to_dict())
print('Empirical papers:', df_papers['has_empirical'].sum())

# Filter empirical papers after 2016
empirical_2017plus = df_papers[(df_papers['has_empirical'] == True) & (df_papers['year'] > 2016)]
print('Empirical papers after 2016:', len(empirical_2017plus))

# Step 2: Process citations data
df_citations = pd.DataFrame(citations)
print('Citations columns:', df_citations.columns.tolist())
print('First row:', df_citations.iloc[0].to_dict())

# Step 3: Match empirical papers with citations
titles_to_find = empirical_2017plus['title'].tolist()

# Filter citations for these titles
matching_citations = df_citations[df_citations['title'].isin(titles_to_find)]

# Merge with paper info
final_results = pd.merge(
    matching_citations,
    empirical_2017plus[['title', 'year']],
    on='title',
    how='inner'
)

print('Papers with matching citations:', len(final_results))

# Sort and prepare output
final_results = final_results.sort_values('total_citations', ascending=False)

output = final_results[['title', 'total_citations', 'year']].to_dict('records')

print('Final results count:', len(output))
if output:
    for r in output[:10]:
        print(r['title'], '(', r['year'], '):', r['total_citations'], 'citations')

result = {'papers': output}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}}

exec(code, env_args)
