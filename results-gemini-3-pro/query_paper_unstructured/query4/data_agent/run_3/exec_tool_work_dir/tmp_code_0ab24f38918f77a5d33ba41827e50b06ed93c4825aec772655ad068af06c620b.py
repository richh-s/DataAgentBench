code = """import json

with open(locals()['var_function-call-4258120896771591873'], 'r') as f:
    paper_docs = json.load(f)

print(f"Total docs: {len(paper_docs)}")

info = []
for doc in paper_docs:
    text = doc.get('text', '')
    title = doc.get('filename', '')
    
    # Check Year
    # Look for 2016, 2015, etc. in first 500 chars
    header = text[:500]
    
    # Check Domain
    has_pa = 'physical activity' in text.lower()
    
    info.append({
        "title": title,
        "header_snippet": header.replace(chr(10), ' '),
        "has_physical_activity": has_pa
    })

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-15838279633175563818': 'file_storage/function-call-15838279633175563818.json', 'var_function-call-1669477486731597489': 'file_storage/function-call-1669477486731597489.json', 'var_function-call-1669477486731597534': 'file_storage/function-call-1669477486731597534.json', 'var_function-call-2579067088761269272': [], 'var_function-call-13126364427078448234': 'Debug Complete', 'var_function-call-13483012681038943566': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_pa': False, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-16857236882397559169': [], 'var_function-call-8662658670787056330': {'count': 1, 'examples': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'context': 'missions from Permissions@acm.org.  DIS 2016, June 04 - 08, 2016, Brisbane, QLD,'}]}, 'var_function-call-13667809118932674388': {'total': 5, 'pa_count': 4, '2016_anywhere_count': 3, 'intersection_count': 2, 'intersection_titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt']}, 'var_function-call-4258120896771591873': 'file_storage/function-call-4258120896771591873.json'}

exec(code, env_args)
