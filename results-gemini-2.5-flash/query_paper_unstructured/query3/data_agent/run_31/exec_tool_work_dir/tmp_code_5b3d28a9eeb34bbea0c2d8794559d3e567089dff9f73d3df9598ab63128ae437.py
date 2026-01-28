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

    # Extract all potential years (4-digit and 2-digit)
    potential_years = []
    for match in re.finditer(r'\\b(19|20)\\d{2}\\b|\\'(\\d{2})', text):
        if match.group(0).startswith('\''): # 2-digit year like '15
            year = 2000 + int(match.group(2)) if int(match.group(2)) <= 99 else 1900 + int(match.group(2))
        else: # 4-digit year like 2015
            year = int(match.group(0))
        potential_years.append(year)

    publication_year = None
    if potential_years:
        # Find the earliest year that is greater than 2016
        # Sorting ensures we get the earliest if multiple exist, which is likely the publication year
        sorted_years = sorted(list(set(potential_years))) # Use set to remove duplicates
        for y in sorted_years:
            if y > 2016:
                publication_year = y
                break

    # Check for 'empirical' contribution using the specified format
    is_empirical = re.search(r'contribution:\\s*empirical', text, re.IGNORECASE) is not None

    if publication_year is not None and is_empirical:
        papers_data.append({
            'title': title,
            'year': publication_year,
            'is_empirical': is_empirical
        })

df_papers = pd.DataFrame(papers_data)

empirical_papers_titles = df_papers['title'].tolist()

print('__RESULT__:')
print(json.dumps(empirical_papers_titles))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json', 'var_function-call-16217772059205383965': [], 'var_function-call-10815164578185853792': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_function-call-10122900059300949010': [], 'var_function-call-13614726233522118016': []}

exec(code, env_args)
