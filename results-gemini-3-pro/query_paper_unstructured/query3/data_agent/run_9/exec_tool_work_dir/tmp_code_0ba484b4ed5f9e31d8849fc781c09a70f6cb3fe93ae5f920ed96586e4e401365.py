code = """import json
import re

paper_docs_path = locals()['var_function-call-15160889356619040949']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

doc = paper_docs[0]
text = doc.get('text', '')
header_text = text[:500]

# Test Regex
regex = r'20[0-9]{2}'
matches = re.findall(regex, header_text)

# Test Empirical
has_empirical = 'empirical' in text.lower()

result = {
    "matches": matches,
    "has_empirical": has_empirical,
    "snippet_len": len(text)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15160889356619040949': 'file_storage/function-call-15160889356619040949.json', 'var_function-call-14370993471195573993': 'file_storage/function-call-14370993471195573993.json', 'var_function-call-3936278199097246076': [], 'var_function-call-845286639558883186': 'Done', 'var_function-call-9568601149975010194': {'total_docs': 5, 'count_year_found': 0, 'count_year_gt_2016': 0, 'count_empirical': 2, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'is_empirical': False}]}, 'var_function-call-10596429833444850584': {'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}}

exec(code, env_args)
