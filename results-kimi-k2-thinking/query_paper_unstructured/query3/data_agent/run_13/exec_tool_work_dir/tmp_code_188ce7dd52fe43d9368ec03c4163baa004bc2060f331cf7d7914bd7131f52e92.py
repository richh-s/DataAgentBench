code = """import json
import re
import pandas as pd

# Load papers data
with open(locals()['var_functions.query_db:46'], 'r') as f:
    papers = json.load(f)

# Load citations data
with open(locals()['var_functions.query_db:14'], 'r') as f:
    citations = json.load(f)

# Extract paper metadata
paper_list = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - look for various patterns
    year = None
    # Pattern 1: Conference format like '15, '16
    conf_pattern = re.findall(r"(?:CHI|Ubicomp|CSCW|DIS|TEI|IUI|WWW|OSAKA).+?'(\d{2})[\b\s,]", text, re.IGNORECASE)
    if conf_pattern:
        years = [int('20' + y) for y in conf_pattern if int(y) < 50]
        if years:
            year = max(years)
    
    # Pattern 2: Full year format
    if not year:
        year_matches = re.findall(r"\b(201[5-9]|202[0-9])\b", text)
        if year_matches:
            year = max([int(y) for y in year_matches])
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    paper_list.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Create DataFrames
df_papers = pd.DataFrame(paper_list)
df_citations = pd.DataFrame(citations)

# Convert citation_count to int
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Filter empirical papers after 2016
filtered_papers = df_papers[
    (df_papers['has_empirical'] == True) & 
    (df_papers['year'] > 2016)
].copy()

print(f"Empirical papers after 2016: {len(filtered_papers)}")

# Get total citations for these papers
titles_to_check = filtered_papers['title'].tolist()

# Filter citations for our papers and sum by title
total_citations = df_citations[df_citations['title'].isin(titles_to_check)]
    .groupby('title')['citation_count']
    .sum()
    .reset_index(name='total_citations')

# Merge with paper info
final_result = pd.merge(filtered_papers, total_citations, on='title', how='inner')

print(f"Papers with citation data: {len(final_result)}")

# Sort by total citations descending
final_result = final_result.sort_values('total_citations', ascending=False)

print("\nTop results:")
print(final_result.head())

# Prepare final output
output = final_result[['title', 'total_citations']].to_dict('records')
print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}}

exec(code, env_args)
