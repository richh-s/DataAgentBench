code = """import json
import re

with open(locals()['var_function-call-12792815428648479832'], 'r') as f:
    paper_docs = json.load(f)

diagnostics = []
for doc in paper_docs[:10]:
    text = doc['text']
    filename = doc['filename']
    header_text = text[:1000]
    
    # Try finding any 4 digit number
    numbers = re.findall(r'20[0-9]{2}', header_text)
    
    diagnostics.append({
        "filename": filename,
        "found_years": numbers,
        "snippet": header_text[:50].replace(chr(10), ' ')
    })

print("__RESULT__:")
print(json.dumps(diagnostics))"""

env_args = {'var_function-call-9689432006532158130': 'file_storage/function-call-9689432006532158130.json', 'var_function-call-7106794807816664619': 'file_storage/function-call-7106794807816664619.json', 'var_function-call-12792815428648479832': 'file_storage/function-call-12792815428648479832.json', 'var_function-call-15343514597715386657': 'file_storage/function-call-15343514597715386657.json', 'var_function-call-16410926222375514887': [], 'var_function-call-17506932778829537594': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [], 'has_empirical': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  "}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [], 'has_empirical': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [], 'has_empirical': True, 'snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': [], 'has_empirical': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [], 'has_empirical': False, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '}]}

exec(code, env_args)
