code = """import json
import pandas as pd
import sqlite3

# Load citations data
citations_file = locals()['var_functions.query_db:14']
print('Loading citations from:', citations_file)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Convert to DataFrame
df_citations = pd.DataFrame(citations)
print('Total citation records:', len(df_citations))
print('Unique titles:', df_citations['title'].nunique())
print('Sample titles:')
print(df_citations['title'].head().tolist())

# Show titles that might be empirical and recent
sample_titles = df_citations['title'].head(10).tolist()
result = {
    'total_records': len(df_citations),
    'unique_titles': df_citations['title'].nunique(),
    'sample_titles': sample_titles
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': []}

exec(code, env_args)
