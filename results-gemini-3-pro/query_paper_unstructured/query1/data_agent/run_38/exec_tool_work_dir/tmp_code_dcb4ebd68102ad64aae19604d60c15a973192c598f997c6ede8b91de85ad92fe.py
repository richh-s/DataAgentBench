code = """import json

with open(locals()['var_function-call-17043150740226976793'], 'r') as f:
    citations = json.load(f)

matches = []
for c in citations:
    if 'food' in c['title'].lower():
        if c['title'] not in matches:
            matches.append(c['title'])

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-3676184941267040123': 'file_storage/function-call-3676184941267040123.json', 'var_function-call-6873213907714452995': 'file_storage/function-call-6873213907714452995.json', 'var_function-call-17043150740226976793': 'file_storage/function-call-17043150740226976793.json', 'var_function-call-7459141219968339162': 'file_storage/function-call-7459141219968339162.json', 'var_function-call-4763535483607380': {'total_citations': 0, 'papers': []}, 'var_function-call-6447564677428063804': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'snippet': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'snippet': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-9339925368458638974': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords': 'Lived Informatics; Personal Informatics; Self-Tracking;  Lapsing; Physical Activity; Finances; Location.'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords': 'Personal informatics, collection, reflection, model, barriers'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords': 'Personalization; animation; emotion; engagement; empathy; self-reﬂection.'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords': 'Wearable technology; dashboard; information visualization;  stroke rehabilitation; occupational therapy'}], 'var_function-call-9131310492286456350': {'total_citations': 0, 'papers': []}}

exec(code, env_args)
