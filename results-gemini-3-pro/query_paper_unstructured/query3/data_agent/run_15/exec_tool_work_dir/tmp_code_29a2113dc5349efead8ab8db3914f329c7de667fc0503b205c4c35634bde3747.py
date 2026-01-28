code = """import json
import re

file_path = locals()['var_function-call-2573740285369106607']

with open(file_path, 'r') as f:
    docs = json.load(f)

debug_info = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    
    # Debug Year
    header = text[:500]
    
    # Debug Contribution
    # Find "Contribution"
    idx = text.lower().find("contribution")
    context = ""
    if idx != -1:
        context = text[idx:idx+200].replace(chr(10), " ")
    
    debug_info.append({
        "filename": filename,
        "header_snippet": header.replace(chr(10), " ")[:100],
        "contribution_snippet": context
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-7387203186474718594': 'file_storage/function-call-7387203186474718594.json', 'var_function-call-9551476032774433042': ['paper_docs'], 'var_function-call-7392786003504292061': {'explicit_contribution': '', 'empirical_context': '', 'years': ['2015', '2015', '2015', '2015', '2015', '2015', '2015', '2015', '2014', '2013']}, 'var_function-call-16070472679849682591': 'file_storage/function-call-16070472679849682591.json', 'var_function-call-14838569663088297683': 'file_storage/function-call-14838569663088297683.json', 'var_function-call-2573740285369106607': 'file_storage/function-call-2573740285369106607.json', 'var_function-call-17192200102339754629': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'contrib_context': 'contributions  through  survey  design  and  parti', 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'contrib_context': 'contributions  in  this  paper:  1)  we  identify ', 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'contrib_context': '', 'has_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did n', 'has_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'contrib_context': 'contribution of this research is  a  system  desig', 'has_empirical': False}]}

exec(code, env_args)
