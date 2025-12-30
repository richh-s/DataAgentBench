code = """import json

with open(locals()['var_function-call-12792815428648479832'], 'r') as f:
    paper_docs = json.load(f)

doc = paper_docs[3] # A Wee Bit More Interaction...
print("__RESULT__:")
print(json.dumps({
    "filename": doc['filename'],
    "text_preview": doc['text'][:2000].replace(chr(10), ' ')
}))"""

env_args = {'var_function-call-9689432006532158130': 'file_storage/function-call-9689432006532158130.json', 'var_function-call-7106794807816664619': 'file_storage/function-call-7106794807816664619.json', 'var_function-call-12792815428648479832': 'file_storage/function-call-12792815428648479832.json', 'var_function-call-15343514597715386657': 'file_storage/function-call-15343514597715386657.json', 'var_function-call-16410926222375514887': [], 'var_function-call-17506932778829537594': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [], 'has_empirical': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  "}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [], 'has_empirical': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [], 'has_empirical': True, 'snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': [], 'has_empirical': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [], 'has_empirical': False, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '}], 'var_function-call-14463308120016227623': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'snippet': 'A Stage-Based Model of Personal Informatics System'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpe'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'snippet': 'A Wee Bit More Interaction: Designing and Evaluati'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'snippet': 'ArmSleeve: a Patient Monitoring System to Support '}]}

exec(code, env_args)
