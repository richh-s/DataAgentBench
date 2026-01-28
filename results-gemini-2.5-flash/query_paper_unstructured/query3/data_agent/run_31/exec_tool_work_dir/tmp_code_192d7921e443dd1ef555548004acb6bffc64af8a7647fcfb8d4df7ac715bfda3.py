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

    # Extract all 4-digit numbers as potential years
    all_years = [int(y) for y in re.findall(r'\b(19|20)\d{2}\b', text)]
    
    # Try to find the latest year that is after 2016
    year = None
    if all_years:
        # Assuming the latest year in the document is the publication year
        # and that publication year would be present early in the document
        # Let's just take the first year that is greater than 2016
        for y in sorted(all_years):
            if y > 2016:
                year = y
                break

    # Check for 'empirical' in the text content (case-insensitive)
    is_empirical = 'empirical' in text.lower()

    if year is not None and is_empirical:
        papers_data.append({
            'title': title,
            'year': year,
            'is_empirical': is_empirical
        })

df_papers = pd.DataFrame(papers_data)

# Select only the title for the next step (querying citations db)
empirical_papers_titles = df_papers['title'].tolist()

print('__RESULT__:')
print(json.dumps(empirical_papers_titles))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_function-call-10122900059300949010': []}

exec(code, env_args)
