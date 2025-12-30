code = """import json

file_path = locals()['var_function-call-1041647607165487633']

with open(file_path, 'r') as f:
    papers = json.load(f)

counts = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text'].lower()
    count = text.count('food')
    counts.append({"title": title, "count": count})

# Sort by count descending
counts.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(counts[:10]))"""

env_args = {'var_function-call-17948406739355176464': 'file_storage/function-call-17948406739355176464.json', 'var_function-call-1041647607165485382': ['Citations', 'sqlite_sequence'], 'var_function-call-1041647607165487633': 'file_storage/function-call-1041647607165487633.json', 'var_function-call-17075501722390720700': [], 'var_function-call-12172120259311764631': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_food': True, 'context': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_food': True, 'context': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_food': False, 'context': ''}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_food': True, 'context': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_food': False, 'context': ''}], 'var_function-call-14126767165602297505': []}

exec(code, env_args)
