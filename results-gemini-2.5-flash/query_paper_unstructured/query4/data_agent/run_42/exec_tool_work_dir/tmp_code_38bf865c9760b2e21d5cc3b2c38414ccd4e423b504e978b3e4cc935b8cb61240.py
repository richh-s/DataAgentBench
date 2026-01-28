code = """import json
import re

file_path = locals()['var_function-call-1020461737059661264']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_2016_physical_activity_titles = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # More robust year extraction for 2016 specifically
    # Look for '2016' in the first 2000 characters, trying to capture publication year
    year_match = re.search(r'\b2016\b', text[:2000])
    year = int(year_match.group(0)) if year_match else None

    is_physical_activity_domain = 'physical activity' in text.lower()

    if year == 2016 and is_physical_activity_domain:
        papers_2016_physical_activity_titles.append(title)

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity_titles))"""

env_args = {'var_function-call-10668140555731164678': ['paper_docs'], 'var_function-call-1020461737059661264': 'file_storage/function-call-1020461737059661264.json', 'var_function-call-18293935031113841746': [], 'var_function-call-2347887543621677021': ['Citations', 'sqlite_sequence'], 'var_function-call-13651244775567562643': [], 'var_function-call-8697211431830606780': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity_domain': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity_domain': False}], 'var_function-call-852955902957413167': [], 'var_function-call-14425437229186978218': []}

exec(code, env_args)
