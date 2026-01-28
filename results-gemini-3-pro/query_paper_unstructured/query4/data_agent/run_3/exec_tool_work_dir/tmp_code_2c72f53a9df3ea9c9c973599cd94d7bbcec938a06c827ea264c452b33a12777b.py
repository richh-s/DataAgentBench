code = """import json

with open(locals()['var_function-call-1669477486731597534'], 'r') as f:
    paper_docs = json.load(f)

total_docs = len(paper_docs)
pa_docs = [d for d in paper_docs if 'physical activity' in d['text'].lower()]
year_2016_docs = [d for d in paper_docs if '2016' in d['text']] # Check anywhere

intersection = [d for d in pa_docs if '2016' in d['text']]

print("__RESULT__:")
print(json.dumps({
    "total": total_docs,
    "pa_count": len(pa_docs),
    "2016_anywhere_count": len(year_2016_docs),
    "intersection_count": len(intersection),
    "intersection_titles": [d['filename'] for d in intersection]
}))"""

env_args = {'var_function-call-15838279633175563818': 'file_storage/function-call-15838279633175563818.json', 'var_function-call-1669477486731597489': 'file_storage/function-call-1669477486731597489.json', 'var_function-call-1669477486731597534': 'file_storage/function-call-1669477486731597534.json', 'var_function-call-2579067088761269272': [], 'var_function-call-13126364427078448234': 'Debug Complete', 'var_function-call-13483012681038943566': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_pa': False, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-16857236882397559169': [], 'var_function-call-8662658670787056330': {'count': 1, 'examples': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'context': 'missions from Permissions@acm.org.  DIS 2016, June 04 - 08, 2016, Brisbane, QLD,'}]}}

exec(code, env_args)
