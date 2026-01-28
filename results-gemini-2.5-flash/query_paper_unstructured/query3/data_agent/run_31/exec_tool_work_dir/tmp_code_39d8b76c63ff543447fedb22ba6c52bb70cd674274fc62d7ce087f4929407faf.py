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
    
    # Extract all 4-digit numbers from the text
    all_4digit_years = [int(y) for y in re.findall(r'\b(19|20)\d{2}\b', text)]
    
    # The publication year is usually the earliest year in the document
    if all_4digit_years:
        publication_year = min(all_4digit_years)

    # Check for 'empirical' in the text (case-insensitive).
    is_empirical = 'empirical' in text.lower()

    # Filter for papers with empirical contribution published after 2016
    if publication_year is not None and publication_year > 2016 and is_empirical:
        papers_data.append({
            'title': title
        })

df_filtered_papers = pd.DataFrame(papers_data)

# Get the list of titles for empirical papers published after 2016
# Check if df_filtered_papers is empty before trying to access 'title'
if not df_filtered_papers.empty:
    empirical_papers_titles = df_filtered_papers['title'].tolist()
else:
    empirical_papers_titles = []

print('__RESULT__:')
print(json.dumps(empirical_papers_titles))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_function-call-10122900059300949010': [], 'var_function-call-13614726233522118016': [], 'var_function-call-14011783932993274675': ['Citations', 'sqlite_sequence'], 'var_function-call-3802482114764520810': 'file_storage/function-call-3802482114764520810.json', 'var_function-call-11167228524830664294': []}

exec(code, env_args)
