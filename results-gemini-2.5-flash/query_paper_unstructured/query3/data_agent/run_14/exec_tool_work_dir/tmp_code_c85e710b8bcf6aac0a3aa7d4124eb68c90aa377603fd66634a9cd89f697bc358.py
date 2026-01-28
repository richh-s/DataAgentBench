code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-89421489897449482']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

parsed_papers_data = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year = None
    # Search for a 4-digit year in the first 1000 characters of the text
    # Also consider patterns like 'YY (e.g., '15)
    year_match_4digit = re.search(r'\b(19|20)\d{2}\b', text[:1000])
    if year_match_4digit:
        year = int(year_match_4digit.group(0))
    else:
        # Try to find 'YY pattern and convert to 20YY if it's after 00
        year_match_2digit = re.search(r"'(\d{2})", text[:1000])
        if year_match_2digit:
            two_digit_year = int(year_match_2digit.group(1))
            if two_digit_year <= 99:  # Assuming 20xx for recent papers
                year = 2000 + two_digit_year
            else:
                year = 1900 + two_digit_year

    # Check for 'empirical' (case-insensitive) in the entire text
    contribution = None
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        contribution = 'empirical'

    parsed_papers_data.append({'title': title, 'year': year, 'contribution': contribution})

df_papers = pd.DataFrame(parsed_papers_data)

# Filter for papers published after 2016 with 'empirical' contribution
# Ensure 'year' is not None before comparison
filtered_papers = df_papers[(df_papers['year'].notna()) & (df_papers['year'] > 2016) & (df_papers['contribution'] == 'empirical')]

empirical_titles = filtered_papers['title'].tolist()

print('__RESULT__:')
print(json.dumps(empirical_titles))"""

env_args = {'var_function-call-3207410245806214601': ['paper_docs'], 'var_function-call-89421489897449482': 'file_storage/function-call-89421489897449482.json', 'var_function-call-2589591416908310925': [], 'var_function-call-13239531528128313526': [], 'var_function-call-835119119760637705': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}]}

exec(code, env_args)
