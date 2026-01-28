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

    # Try to extract year using a more general regex
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Check for 'empirical' in the text content (case-insensitive)
    is_empirical = 'empirical' in text.lower()

    papers_data.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

df_papers = pd.DataFrame(papers_data)

# Filter papers for 'empirical' contribution and year > 2016
filtered_papers = df_papers[
    (df_papers['is_empirical'] == True) &
    (df_papers['year'] > 2016)
]

# Select only the title for the next step (querying citations db)
empirical_papers_titles = filtered_papers['title'].tolist()

print('__RESULT__:')
print(json.dumps(empirical_papers_titles))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}]}

exec(code, env_args)
