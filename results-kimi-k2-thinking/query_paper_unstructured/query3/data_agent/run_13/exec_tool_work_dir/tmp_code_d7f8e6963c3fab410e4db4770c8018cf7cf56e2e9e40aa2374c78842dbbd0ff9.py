code = """import json
import re
import pandas as pd

# Access the papers data directly from the variable
papers = locals()['var_functions.query_db:46']

print('Total papers loaded:', len(papers))

# Process papers to extract metadata
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - look for 20XX pattern
    year = None
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        years = [int(y) for y in year_matches]
        # Filter reasonable range
        years = [y for y in years if 2000 <= y <= 2030]
        if years:
            year = max(years)
    
    # Check for empirical contribution (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_metadata)

print('\n=== PAPER ANALYSIS ===')
print('Total papers:', len(df_papers))
print('Year distribution:')
year_counts = df_papers['year'].value_counts().sort_index()
print(year_counts.to_dict())

print('\nEmpirical papers:', df_papers['has_empirical'].sum())

# Filter empirical papers published after 2016 (year > 2016)
empirical_after_2016 = df_papers[
    (df_papers['has_empirical'] == True) & 
    (df_papers['year'] > 2016)
]

print('\nEmpirical papers after 2016:', len(empirical_after_2016))

if len(empirical_after_2016) > 0:
    print('\nTitles of empirical papers after 2016:')
    for title in empirical_after_2016['title'].tolist():
        print('-', title)
    
    # Extract titles for citation lookup
    titles_to_check = empirical_after_2016['title'].tolist()
else:
    titles_to_check = []
    print('No empirical papers found after 2016')

result = {
    'empirical_papers_after_2016': len(empirical_after_2016),
    'titles': titles_to_check
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': []}

exec(code, env_args)
