code = """import pandas as pd
import re
import json

# Load the full MongoDB result from the file
with open(locals()['var_function-call-16572885030136982066'], 'r') as f:
    mongo_docs = json.load(f)

papers_data = []
for doc in mongo_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    publication_year = None
    
    # Find all potential year strings: 4-digit (e.g., 2018) or 2-digit (e.g., '18)
    # The regex below will find either 'YYYY' or ''YY' occurrences.
    # Using non-capturing groups (?:...) to make sure findall returns full matches.
    all_year_strings = re.findall(r'\\b(?:19|20)\\d{2}\\b|\\'\\d{2}', text)

    current_doc_years = []
    for year_str in all_year_strings:
        if year_str.startswith('\''): # It's a 2-digit year like '18
            # Convert 'YY' to 20YY. Assuming all relevant 2-digit years are for 2000s
            year = 2000 + int(year_str[1:])
        else: # It's a 4-digit year like 2018
            year = int(year_str)
        current_doc_years.append(year)

    # Filter for years strictly greater than 2016 and find the earliest one.
    valid_years_after_2016 = sorted(list(set([y for y in current_doc_years if y > 2016])))
    if valid_years_after_2016:
        publication_year = valid_years_after_2016[0] # Earliest year after 2016

    # Check for 'empirical' in the text (case-insensitive) as a general contribution type
    is_empirical = 'empirical' in text.lower()

    if publication_year is not None and is_empirical:
        papers_data.append({
            'title': title,
            'year': publication_year,
            'is_empirical': is_empirical
        })

df_filtered_papers = pd.DataFrame(papers_data)

if not df_filtered_papers.empty:
    empirical_papers_titles = df_filtered_papers['title'].tolist()
else:
    empirical_papers_titles = []

print('__RESULT__:')
print(json.dumps(empirical_papers_titles))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_function-call-10122900059300949010': [], 'var_function-call-13614726233522118016': [], 'var_function-call-14011783932993274675': ['Citations', 'sqlite_sequence'], 'var_function-call-3802482114764520810': 'file_storage/function-call-3802482114764520810.json'}

exec(code, env_args)
