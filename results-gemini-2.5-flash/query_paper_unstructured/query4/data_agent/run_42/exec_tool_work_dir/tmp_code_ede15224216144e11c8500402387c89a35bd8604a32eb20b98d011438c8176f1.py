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

    # Attempt to find 2016 in the initial portion of the document, which often contains publication details.
    # Using a larger window (e.g., 2000 characters) to be more flexible, and looking for common patterns like 'Copyright' or conference names preceding the year.
    year_found = False
    match_2016 = re.search(r'\b(?:Copyright|UbiComp|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*\'?\d{2}\s*,?\s*2016\b', text[:2000], re.IGNORECASE)
    if match_2016:
        year_found = True
    else:
        # Fallback: look for 2016 directly within the first 1000 characters (where publication year is likely)
        direct_year_match = re.search(r'\b2016\b', text[:1000])
        if direct_year_match:
            year_found = True

    is_physical_activity_domain = 'physical activity' in text.lower()

    if year_found and is_physical_activity_domain:
        papers_titles_2016_physical_activity.append(title)

print('__RESULT__:')
print(json.dumps(papers_titles_2016_physical_activity))"""

env_args = {'var_function-call-10668140555731164678': ['paper_docs'], 'var_function-call-1020461737059661264': 'file_storage/function-call-1020461737059661264.json', 'var_function-call-18293935031113841746': [], 'var_function-call-2347887543621677021': ['Citations', 'sqlite_sequence'], 'var_function-call-13651244775567562643': [], 'var_function-call-8697211431830606780': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity_domain': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity_domain': False}], 'var_function-call-852955902957413167': [], 'var_function-call-14425437229186978218': [], 'var_function-call-781667464626310912': [], 'var_function-call-4561129352538845863': 'file_storage/function-call-4561129352538845863.json', 'var_function-call-13921114947480944330': [], 'var_function-call-14061200294000552431': [], 'var_function-call-8134151316194436233': 'file_storage/function-call-8134151316194436233.json', 'var_function-call-2586611087207286249': [], 'var_function-call-7630030699160760330': []}

exec(code, env_args)
