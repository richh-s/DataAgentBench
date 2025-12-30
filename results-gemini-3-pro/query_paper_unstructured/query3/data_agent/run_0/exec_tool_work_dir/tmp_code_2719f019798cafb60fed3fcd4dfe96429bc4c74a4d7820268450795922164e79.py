code = """import json
import re

file_path = locals()['var_function-call-4290533744407008086']
with open(file_path, 'r') as f:
    docs = json.load(f)

count_after_2016 = 0
empirical_after_2016 = 0
matches = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Year extraction
    header = text[:3000]
    years = re.findall(r'20\d{2}', header)
    years = [int(y) for y in years if 2000 <= int(y) <= 2025]
    
    pub_year = None
    if years:
        pub_year = years[0]
        
    if pub_year and pub_year > 2016:
        count_after_2016 += 1
        has_empirical = 'empirical' in text.lower()
        if has_empirical:
            empirical_after_2016 += 1
            matches.append(filename.replace('.txt', ''))
        else:
            # Print title of non-empirical post-2016 paper to check
            if count_after_2016 - empirical_after_2016 <= 3:
                print(f"Post-2016 Non-Empirical: {filename}, Year: {pub_year}")

print(f"Papers > 2016: {count_after_2016}")
print(f"Empirical & > 2016: {empirical_after_2016}")
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-1070528273488687685': ['paper_docs'], 'var_function-call-1070528273488689510': ['Citations', 'sqlite_sequence'], 'var_function-call-3440707792195880886': 'file_storage/function-call-3440707792195880886.json', 'var_function-call-4290533744407008086': 'file_storage/function-call-4290533744407008086.json', 'var_function-call-9474119233572840717': [], 'var_function-call-3308725518524162572': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'empirical': False}], 'var_function-call-11803891483283226719': {'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-14757257538439203850': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-4599478284216626480': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'first_year': 2015, 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'first_year': None, 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'first_year': None, 'has_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'first_year': None, 'has_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'first_year': None, 'has_empirical': False}]}

exec(code, env_args)
