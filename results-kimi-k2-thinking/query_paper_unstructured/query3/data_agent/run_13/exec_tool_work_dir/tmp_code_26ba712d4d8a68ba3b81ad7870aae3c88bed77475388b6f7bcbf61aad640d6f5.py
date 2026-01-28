code = """import json
import re
import pandas as pd

# Step 1: Load papers data from MongoDB query result
papers_path = locals()['var_functions.query_db:46']
print('Loading papers from:', papers_path)

with open(papers_path, 'r') as f:
    papers_all = json.load(f)

print('_Total papers:', len(papers_all))

# Step 2: Extract metadata from all papers
papers_metadata = []
for doc in papers_all:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year using regex to find 4-digit years
    year = None
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical contribution
    is_empirical = 'empirical' in text.lower()
    
    papers_metadata.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

# Create DataFrame
df = pd.DataFrame(papers_metadata)

print('_Year distribution:', df['year'].value_counts().sort_index().to_dict())
print('_Total empirical papers:', df['is_empirical'].sum())

# Filter for empirical papers after 2016
empirical_2017plus = df[(df['is_empirical'] == True) & (df['year'] > 2016)]

print('_Empirical papers after 2016:', len(empirical_2017plus))

# Get titles for next step
titles_list = empirical_2017plus['title'].tolist()
print('_Titles:', titles_list)

result = {
    'count': len(titles_list),
    'titles': titles_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': []}

exec(code, env_args)
