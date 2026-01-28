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
    # Broader search for any 4-digit number that could be a year in the first 2000 characters to be more robust
    year_matches = re.findall(r'\\b(19\\d{2}|20(?:0\\d|1\\d|2[0-4]))\\b', text[:2000])
    valid_years = [int(ym) for ym in year_matches if 1990 <= int(ym) <= 2024] # Filter for reasonable range
    if valid_years:
        year = min(valid_years) # Take the earliest valid year found in the initial part of the paper

    is_empirical = False
    # Check for explicit 'contribution' field mentioning 'empirical'
    contribution_match = re.search(r'contribution: (.*?)(?:\\n|\\.|,)', text, re.IGNORECASE)
    if contribution_match and 'empirical' in contribution_match.group(1).lower():
        is_empirical = True
    
    # Even more comprehensive list of keywords and phrases to identify empirical contributions if not explicitly stated
    if not is_empirical:
        empirical_keywords_in_text = [
            'empirical study', 'we conducted an experiment', 'our study involved', 'data collected from',
            'surveyed participants', 'interviews with', 'user study', 'field study', 'observational study',
            'quantitative analysis', 'qualitative analysis', 'experimental design', 'results indicate',
            'participants reported', 'evaluation of', 'investigated through', 'findings suggest',
            'examined the impact', 'tested the hypothesis', 'demonstrated through', 'measured the effect',
            'empirical evidence', 'empirical findings', 'empirical evaluation', 'an empirical exploration',
            'pilot study', 'case study', 'research methods', 'methodology section', 'data analysis', 
            'statistical analysis', 'the participants', 'study design', 'data-driven', 'evidence-based', 
            'experimental results', 'user feedback', 'observing users', 'gathered data', 'research questions',
            'participant recruitment', 'collected data', 'performed an analysis', 'conducted a series of experiments',
            'quantitative data', 'qualitative data', 'statistical methods', 'human subjects', 'experiment group',
            'control group', 'hypothesis testing', 'observed behaviors', 'measured variables', 'effect of'
        ]
        if any(keyword in text.lower() for keyword in empirical_keywords_in_text):
            is_empirical = True

    if year and year > 2016 and is_empirical:
        extracted_papers_info.append({
            'title': title
        })

df_filtered_papers = pd.DataFrame(extracted_papers_info)

print('__RESULT__:')
print(df_filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-2783535409203713964': ['paper_docs'], 'var_function-call-11985281394751560404': 'file_storage/function-call-11985281394751560404.json', 'var_function-call-1858781425464915204': [], 'var_function-call-16910803448492452394': 'file_storage/function-call-16910803448492452394.json', 'var_function-call-1569923686048684083': [], 'var_function-call-6290455492128806949': 'file_storage/function-call-6290455492128806949.json', 'var_function-call-15391798736132793423': [], 'var_function-call-6132096007992688768': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_function-call-4315299038744484136': [], 'var_function-call-7402946793141852739': [], 'var_function-call-17784596592726517006': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_function-call-7089471432629544821': [], 'var_function-call-14965344820861257744': [], 'var_function-call-12874905180232078639': []}

exec(code, env_args)
