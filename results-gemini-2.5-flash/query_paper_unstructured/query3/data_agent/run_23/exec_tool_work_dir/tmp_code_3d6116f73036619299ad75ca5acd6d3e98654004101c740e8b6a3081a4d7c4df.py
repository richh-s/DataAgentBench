code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-16910803448492452394']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_papers_info = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    year = None
    # Broader search for year, looking for 4 digits that could be a year in the context of publications
    # Prioritize years appearing in the first 500 chars (common for publication info)
    year_match_early = re.search(r'\\b(19\\d{2}|20(?:0\\d|1\\d|2[0-4]))\\b', text[:500])
    if year_match_early:
        year = int(year_match_early.group(0))
    else:
        # If not found early, search the entire text, but be more cautious not to pick random 4-digit numbers
        # This regex looks for years preceded by common publication keywords like 'published', 'year', 'date'
        year_match_late = re.search(r'(?:published|year|date):?.*?\\b(19\\d{2}|20(?:0\\d|1\\d|2[0-4]))\\b', text, re.IGNORECASE)
        if year_match_late:
            year = int(year_match_late.group(1))
        else:
            # As a last resort, try to find any 4-digit number that looks like a year, but still within a reasonable range
            year_match_anywhere = re.search(r'\\b(19\\d{2}|20(?:0\\d|1\\d|2[0-4]))\\b', text)
            if year_match_anywhere:
                year = int(year_match_anywhere.group(0))

    is_empirical = False
    # Check for explicit 'contribution: empirical' or similar phrasing
    contribution_explicit_match = re.search(r'contribution: (.*?empirical.*?)(?:\\n|\\.|,)', text, re.IGNORECASE)
    if contribution_explicit_match:
        is_empirical = True
    else:
        # Check for empirical keywords within the text if no explicit contribution field is found
        empirical_keywords_in_text = [
            'we conducted a study', 'our study shows', 'experimentally evaluated', 
            'user study', 'participants were', 'survey results', 'interviewed users',
            'data collection', 'quantitative analysis', 'qualitative analysis',
            'field study', 'observational study', 'empirical evidence', 'empirical findings'
        ]
        if any(keyword in text.lower() for keyword in empirical_keywords_in_text):
            is_empirical = True

    if year and year > 2016 and is_empirical:
        extracted_papers_info.append({
            'title': title,
            'year': year
        })

df_filtered_papers = pd.DataFrame(extracted_papers_info)

print('__RESULT__:')
print(df_filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-2783535409203713964': ['paper_docs'], 'var_function-call-11985281394751560404': 'file_storage/function-call-11985281394751560404.json', 'var_function-call-1858781425464915204': [], 'var_function-call-16910803448492452394': 'file_storage/function-call-16910803448492452394.json', 'var_function-call-1569923686048684083': [], 'var_function-call-6290455492128806949': 'file_storage/function-call-6290455492128806949.json', 'var_function-call-15391798736132793423': []}

exec(code, env_args)
