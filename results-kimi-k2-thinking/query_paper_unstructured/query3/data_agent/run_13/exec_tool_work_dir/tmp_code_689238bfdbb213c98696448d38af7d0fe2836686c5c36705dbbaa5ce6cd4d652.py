code = """import json
import re
import pandas as pd

# Load papers data
papers_file = locals()['var_functions.query_db:46']
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Total papers from MongoDB:', len(papers))

# Extract metadata from all papers
paper_metadata = []
for i, paper in enumerate(papers[:100]):  # Process first 100 to see patterns
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - multiple patterns
    year = None
    
    # Pattern 1: Look for 20XX years
    matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if matches:
        years = [int(y) for y in matches]
        # Filter reasonable years (2000-2030)
        years = [y for y in years if 2000 <= y <= 2030]
        if years:
            year = max(years)  # Most recent year is likely publication year
    
    # Pattern 2: Look for 'XX format (like '15)
    if not year:
        matches2 = re.findall(r"'([0-9]{2})\b", text)
        if matches2:
            years = [int('20' + y) for y in matches2 if int(y) < 50]
            if years:
                year = max(years)
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    # Sample first few papers for debugging
    if i < 3:
        print(f"Sample {i+1}:")
        print(f"  Title: {title}")
        print(f"  Year found: {year}")
        print(f"  Has empirical: {has_empirical}")
        print(f"  Text preview: {text[:150]}...")
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Process all papers
paper_metadata_all = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year
    year = None
    matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if matches:
        years = [int(y) for y in matches if 2000 <= int(y) <= 2030]
        if years:
            year = max(years)
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata_all.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

df_all = pd.DataFrame(paper_metadata_all)

print('\n=== PAPER STATISTICS ===')
print('Total papers:', len(df_all))
print('Year distribution:')
print(df_all['year'].value_counts().sort_index())
print('\nEmpirical papers:', df_all['has_empirical'].sum())
print('Empirical by year:')
empirical_by_year = df_all[df_all['has_empirical'] == True]['year'].value_counts().sort_index()
print(empirical_by_year)

# Check papers with no year detected
no_year = df_all[df_all['year'].isna()]
print('\nPapers with no year detected:', len(no_year))

# Filter empirical papers after 2016
empirical_after_2016 = df_all[
    (df_all['has_empirical'] == True) & 
    (df_all['year'] > 2016)
]

print('\nEmpirical papers after 2016:', len(empirical_after_2016))
if len(empirical_after_2016) > 0:
    print('Titles:', empirical_after_2016['title'].tolist())

result = {
    'empirical_papers_2017_plus': len(empirical_after_2016),
    'titles': empirical_after_2016['title'].tolist() if len(empirical_after_2016) > 0 else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': []}

exec(code, env_args)
