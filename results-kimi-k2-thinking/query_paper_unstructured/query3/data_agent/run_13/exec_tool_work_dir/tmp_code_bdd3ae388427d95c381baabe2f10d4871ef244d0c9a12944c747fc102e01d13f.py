code = """import json
import re
import pandas as pd

# Get file paths from stored variables
papers_file_path = locals()['var_functions.query_db:46']
citations_file_path = locals()['var_functions.query_db:14']

# Load papers data (MongoDB documents)
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Load citations data (SQLite query result)
with open(citations_file_path, 'r') as f:
    citations = json.load(f)

print('Loaded', len(papers), 'papers and', len(citations), 'citation records')

# Step 1: Extract paper metadata (title, year, empirical flag)
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year using multiple regex patterns
    year = None
    
    # Pattern 1: Look for full year (20XX)
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)  # Use most recent year found
    
    # Pattern 2: Look for conference format like '15, '16
    if not year:
        short_year_matches = re.findall(r"'([0-9]{2})\b", text)
        if short_year_matches:
            years_from_short = [int('20' + y) for y in short_year_matches if int(y) < 50]
            if years_from_short:
                year = max(years_from_short)
    
    # Check for empirical contribution (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

df_papers = pd.DataFrame(paper_metadata)

# Step 2: Filter empirical papers published after 2016
empirical_papers_2017plus = df_papers[
    (df_papers['has_empirical'] == True) & 
    (df_papers['year'] > 2016)
].copy()

print('Found', len(empirical_papers_2017plus), 'empirical papers after 2016')

# Step 3: Process citations data
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Group citations by title to get total citations per paper
total_citations = df_citations.groupby('title')['citation_count'].sum().reset_index(name='total_citations')

# Step 4: Merge paper metadata with citation counts
# Create a lookup for the empirical papers we found
titles_to_find = empirical_papers_2017plus['title'].tolist()

# Filter citations for our papers and add paper info
matching_papers = total_citations[total_citations['title'].isin(titles_to_find)]

# Merge with paper year info to verify
final_results = pd.merge(
    matching_papers, 
    empirical_papers_2017plus[['title', 'year']], 
    on='title', 
    how='inner'
)

print('Found', len(final_results), 'papers with citation data')

# Sort by total citations descending
final_results = final_results.sort_values('total_citations', ascending=False)

# Prepare output
output = final_results[['title', 'total_citations', 'year']].to_dict('records')

print('Final results:')
for r in output:
    print('-', r['title'], '(', r['year'], '):', r['total_citations'], 'citations')

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}}

exec(code, env_args)
