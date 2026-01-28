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

    # Extract all 4-digit years from the text
    all_4digit_years = [int(y) for y in re.findall(r'\b(19|20)\d{2}\b', text)]
    
    # Get the earliest year in the document. This is often the publication year.
    publication_year = min(all_4digit_years) if all_4digit_years else None

    # Check for 'empirical' in the text content (case-insensitive)
    is_empirical = 'empirical' in text.lower()

    papers_data.append({
        'title': title,
        'year': publication_year,
        'is_empirical': is_empirical
    })

df_papers = pd.DataFrame(papers_data)

# Filter for empirical papers published after 2016
filtered_papers = df_papers[
    (df_papers['is_empirical'] == True) &
    (df_papers['year'] > 2016)
]

# Get the list of titles for empirical papers published after 2016
empirical_papers_titles = filtered_papers['title'].tolist()

print('__RESULT__:')
print(json.dumps(empirical_papers_titles))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_function-call-10122900059300949010': []}

exec(code, env_args)
