code = """import json
import re

with open(locals()['var_function-call-17632845538165496708'], 'r') as f:
    papers = json.load(f)

def extract_year(text):
    header = text[:3000]
    matches = re.findall(r'20[0-2][0-9]', header)
    if matches:
        return int(matches[0])
    return None

def is_empirical(text):
    return 'empirical' in text.lower()

target_titles = ["Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", "Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing"]

debug_list = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    if title in target_titles:
        year = extract_year(p['text'])
        emp = is_empirical(p['text'])
        debug_list.append({"title": title, "year": year, "empirical": emp})

print("__RESULT__:")
print(json.dumps(debug_list))"""

env_args = {'var_function-call-1840327009665407502': ['paper_docs'], 'var_function-call-12708107300142329': 'file_storage/function-call-12708107300142329.json', 'var_function-call-5269555748610322771': 'file_storage/function-call-5269555748610322771.json', 'var_function-call-17632845538165496708': 'file_storage/function-call-17632845538165496708.json', 'var_function-call-2108981104477433395': 'file_storage/function-call-2108981104477433395.json', 'var_function-call-1161743497919610502': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 265, 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 266, 'year': 2019}], 'var_function-call-3310395966876323144': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'empirical': False}]}

exec(code, env_args)
