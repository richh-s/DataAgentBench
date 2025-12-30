code = """import json

with open(locals()['var_function-call-1669477486731597534'], 'r') as f:
    paper_docs = json.load(f)

candidates = []
for doc in paper_docs:
    text = doc.get('text', '')
    if 'physical activity' in text.lower():
        idx = text[:5000].find('2016')
        if idx != -1:
            # Found 2016 in first 5000 chars
            context = text[max(0, idx-50):min(len(text), idx+50)].replace('\n', ' ')
            candidates.append({
                "title": doc['filename'],
                "context": context
            })

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-15838279633175563818': 'file_storage/function-call-15838279633175563818.json', 'var_function-call-1669477486731597489': 'file_storage/function-call-1669477486731597489.json', 'var_function-call-1669477486731597534': 'file_storage/function-call-1669477486731597534.json', 'var_function-call-2579067088761269272': [], 'var_function-call-13126364427078448234': 'Debug Complete', 'var_function-call-13483012681038943566': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_pa': False, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}]}

exec(code, env_args)
