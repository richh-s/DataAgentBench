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
    # Attempt to find year within the first 1000 characters (common for header/metadata)
    year_match = re.search(r'\\b(19\\d{2}|20(?:0\\d|1\\d|2[0-4]))\\b', text[:1000])
    if year_match:
        year = int(year_match.group(0))

    is_empirical = False
    # Broader set of keywords and phrases to identify empirical contributions
    empirical_keywords = [
        'empirical study', 'we conducted an experiment', 'our study involved', 'data collected from',
        'surveyed participants', 'interviews with', 'user study', 'field study', 'observational study',
        'quantitative analysis', 'qualitative analysis', 'experimental design', 'results indicate',
        'participants reported', 'evaluation of', 'investigated through', 'findings suggest',
        'examined the impact', 'tested the hypothesis', 'demonstrated through', 'measured the effect',
        'empirical evidence', 'empirical findings', 'empirical evaluation', 'an empirical exploration'
    ]
    
    # Check for explicit 'contribution' field mentioning 'empirical'
    contribution_match = re.search(r'contribution: (.*?)(?:\\n|\\.|,)', text, re.IGNORECASE)
    if contribution_match and 'empirical' in contribution_match.group(1).lower():
        is_empirical = True
    
    # If not explicitly in 'contribution', check for empirical keywords throughout the entire text
    if not is_empirical:
        if any(keyword in text.lower() for keyword in empirical_keywords):
            is_empirical = True

    if year and year > 2016 and is_empirical:
        extracted_papers_info.append({
            'title': title,
            'year': year
        })

df_filtered_papers = pd.DataFrame(extracted_papers_info)

print('__RESULT__:')
print(df_filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-2783535409203713964': ['paper_docs'], 'var_function-call-11985281394751560404': 'file_storage/function-call-11985281394751560404.json', 'var_function-call-1858781425464915204': [], 'var_function-call-16910803448492452394': 'file_storage/function-call-16910803448492452394.json', 'var_function-call-1569923686048684083': [], 'var_function-call-6290455492128806949': 'file_storage/function-call-6290455492128806949.json', 'var_function-call-15391798736132793423': [], 'var_function-call-6132096007992688768': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_function-call-4315299038744484136': []}

exec(code, env_args)
