code = """import json
import re

with open(locals()['var_function-call-9673377435246489263'], 'r') as f:
    papers_data = json.load(f)

food_counts = []
for p in papers_data:
    count = p['text'].lower().count('food')
    food_counts.append({'filename': p['filename'], 'count': count})

# Sort by count descending
food_counts.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(food_counts[:5]))"""

env_args = {'var_function-call-16442091982687073941': 'file_storage/function-call-16442091982687073941.json', 'var_function-call-8772526442893089747': 'file_storage/function-call-8772526442893089747.json', 'var_function-call-9673377435246489263': 'file_storage/function-call-9673377435246489263.json', 'var_function-call-17486704262329443494': 'file_storage/function-call-17486704262329443494.json', 'var_function-call-1266494665686074399': 0, 'var_function-call-4508597791168486055': 'done', 'var_function-call-13604048881481762108': {'titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'keywords_sample': [{'file': 'A Lived Informatics Model of Personal Informatics.txt', 'kw': 'Lived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location.'}, {'file': 'A Stage-based Model of Personal Informatics Systems.txt', 'kw': 'Personal informatics, collection, reflection, model, barriers'}, {'file': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'kw': 'Personalization; animation; emotion; engagement; empathy;\nself-reﬂection.'}, {'file': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'kw': 'None'}, {'file': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'kw': 'Wearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy'}], 'food_titles': []}, 'var_function-call-15055726266802828220': {'count': 0, 'papers': []}}

exec(code, env_args)
