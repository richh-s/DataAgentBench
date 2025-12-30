code = """import json
import re

with open(locals()['var_function-call-14323313354234643834'], 'r') as f:
    papers = json.load(f)

year_counts = {}
for p in papers:
    header = p.get('text', '')[:1000]
    years = re.findall(r'20\d{2}', header)
    for y in years:
        year_counts[y] = year_counts.get(y, 0) + 1
    
    # Check for 'YY format too
    short_years = re.findall(r"'\d{2}", header)
    for y in short_years:
        year_counts[y] = year_counts.get(y, 0) + 1

print("__RESULT__:")
print(json.dumps(year_counts))"""

env_args = {'var_function-call-8814252410451424238': ['paper_docs'], 'var_function-call-5259206578733669392': 'file_storage/function-call-5259206578733669392.json', 'var_function-call-14323313354234643834': 'file_storage/function-call-14323313354234643834.json', 'var_function-call-12161874527337870347': ['Citations', 'sqlite_sequence'], 'var_function-call-7764328309385985012': 'file_storage/function-call-7764328309385985012.json', 'var_function-call-3369097710081167039': [], 'var_function-call-6510332609486320018': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [], 'has_pa': True}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [], 'has_pa': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [], 'has_pa': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': [], 'has_pa': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [], 'has_pa': False}], 'var_function-call-5498128891951429973': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'var_function-call-2372319320552918241': [], 'var_function-call-3375896330272505398': []}

exec(code, env_args)
