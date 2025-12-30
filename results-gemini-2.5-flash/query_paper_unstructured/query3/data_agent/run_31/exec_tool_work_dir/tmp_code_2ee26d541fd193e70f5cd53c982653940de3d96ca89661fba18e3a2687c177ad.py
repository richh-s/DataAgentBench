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
    # Find all 4-digit numbers that could be years
    all_potential_years = [int(y) for y in re.findall(r'\\b(19|20)\\d{2}\\b', text)]
    
    # Sort them to find the earliest valid publication year after 2016
    for year in sorted(all_potential_years):
        if year > 2016:
            publication_year = year
            break

    # Check for 'empirical' in the text (case-insensitive)
    is_empirical = 'empirical' in text.lower()

    if publication_year is not None and is_empirical:
        papers_data.append({
            'title': title,
            'year': publication_year
        })

df_filtered_papers = pd.DataFrame(papers_data)

empirical_papers_titles = df_filtered_papers['title'].tolist()

print('__RESULT__:')
print(json.dumps(empirical_papers_titles))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_function-call-10122900059300949010': [], 'var_function-call-13614726233522118016': []}

exec(code, env_args)
