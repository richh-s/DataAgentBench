code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-16910803448492452394']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_papers_info = []

empirical_keywords = ['empirical study', 'we conducted an experiment', 'our study involved', 'data collected from', 'surveyed participants', 'interviews with', 'user study']

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    year = None
    # Try to find a year within the first 500 characters of the paper, as it is often near the beginning
    year_match = re.search(r'\\b(20(?:0[0-9]|1[0-9]|2[0-4]))\\b', text[:500])
    if year_match:
        year = int(year_match.group(0))

    is_empirical = False
    # Check for strong empirical keywords throughout the entire text
    if any(keyword in text.lower() for keyword in empirical_keywords):
        is_empirical = True
    
    # Also, check for the 'contribution' field specifically mentioning 'empirical'
    contribution_match = re.search(r'contribution: (.*?)(?:\\n|\\.|,)', text, re.IGNORECASE)
    if contribution_match and 'empirical' in contribution_match.group(1).lower():
        is_empirical = True

    if year and year > 2016 and is_empirical:
        extracted_papers_info.append({
            'title': title,
            'year': year
        })

df_filtered_papers = pd.DataFrame(extracted_papers_info)

print('__RESULT__:')
print(df_filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-2783535409203713964': ['paper_docs'], 'var_function-call-11985281394751560404': 'file_storage/function-call-11985281394751560404.json', 'var_function-call-1858781425464915204': [], 'var_function-call-16910803448492452394': 'file_storage/function-call-16910803448492452394.json', 'var_function-call-1569923686048684083': [], 'var_function-call-6290455492128806949': 'file_storage/function-call-6290455492128806949.json'}

exec(code, env_args)
