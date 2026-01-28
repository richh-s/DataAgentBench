code = """import json
import re

file_path = locals()['var_function-call-4290533744407008086']
with open(file_path, 'r') as f:
    docs = json.load(f)

for doc in docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    if title in ["A Trip to the Moon: Personalized Animated Movies for Self-reflection", "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App"]:
        text = doc.get('text', '')
        header = text[:3000]
        years = re.findall(r'20\d{2}', header)
        years = [int(y) for y in years if 2000 <= int(y) <= 2025]
        pub_year = years[0] if years else None
        print(f"Title: {title}, Year: {pub_year}")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-1070528273488687685': ['paper_docs'], 'var_function-call-1070528273488689510': ['Citations', 'sqlite_sequence'], 'var_function-call-3440707792195880886': 'file_storage/function-call-3440707792195880886.json', 'var_function-call-4290533744407008086': 'file_storage/function-call-4290533744407008086.json', 'var_function-call-9474119233572840717': [], 'var_function-call-3308725518524162572': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'empirical': False}], 'var_function-call-11803891483283226719': {'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-14757257538439203850': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-4599478284216626480': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'first_year': 2015, 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'first_year': None, 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'first_year': None, 'has_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'first_year': None, 'has_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'first_year': None, 'has_empirical': False}], 'var_function-call-4521043477466583737': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-7818898384745143981': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}]}

exec(code, env_args)
