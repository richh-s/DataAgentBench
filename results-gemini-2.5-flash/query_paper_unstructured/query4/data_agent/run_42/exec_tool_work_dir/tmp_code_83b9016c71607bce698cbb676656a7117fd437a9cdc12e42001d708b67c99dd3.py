code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-1020461737059661264']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_titles_2016_physical_activity = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year from the first 500 characters, as publication year is usually at the beginning
    # Looking for a 4-digit number that likely represents a year (19xx or 20xx)
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:500])
    publication_year = int(year_match.group(0)) if year_match else None

    # Check if 'physical activity' is in the full text (case-insensitive)
    is_physical_activity_domain = 'physical activity' in text.lower()

    if publication_year == 2016 and is_physical_activity_domain:
        papers_titles_2016_physical_activity.append(title)

print('__RESULT__:')
print(json.dumps(papers_titles_2016_physical_activity))"""

env_args = {'var_function-call-10668140555731164678': ['paper_docs'], 'var_function-call-1020461737059661264': 'file_storage/function-call-1020461737059661264.json', 'var_function-call-18293935031113841746': [], 'var_function-call-2347887543621677021': ['Citations', 'sqlite_sequence'], 'var_function-call-13651244775567562643': [], 'var_function-call-8697211431830606780': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity_domain': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity_domain': False}], 'var_function-call-852955902957413167': [], 'var_function-call-14425437229186978218': [], 'var_function-call-781667464626310912': [], 'var_function-call-4561129352538845863': 'file_storage/function-call-4561129352538845863.json', 'var_function-call-13921114947480944330': [], 'var_function-call-14061200294000552431': [], 'var_function-call-8134151316194436233': 'file_storage/function-call-8134151316194436233.json', 'var_function-call-2586611087207286249': [], 'var_function-call-7630030699160760330': [], 'var_function-call-1310384801259058188': [], 'var_function-call-5629838757280383548': [], 'var_function-call-16785956330050197925': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-17372391694843494030': [], 'var_function-call-15846715091230493913': 'file_storage/function-call-15846715091230493913.json', 'var_function-call-14911253998123745887': []}

exec(code, env_args)
