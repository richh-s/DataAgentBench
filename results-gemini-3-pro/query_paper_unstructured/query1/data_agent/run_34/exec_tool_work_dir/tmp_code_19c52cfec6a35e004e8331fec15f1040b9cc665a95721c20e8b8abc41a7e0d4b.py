code = """import json

file_path = locals()['var_function-call-4541425889179395715']

with open(file_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text'].lower()
    
    match_found = False
    
    # Check title
    if 'food' in title.lower():
        match_found = True
    
    # Check keywords
    if not match_found:
        start_idx = text.find('author keywords')
        if start_idx != -1:
            snippet = text[start_idx:start_idx+600]
            if 'food' in snippet:
                match_found = True
    
    if match_found:
        food_papers.append(title)

print("__RESULT__:")
print(json.dumps(food_papers))"""

env_args = {'var_function-call-17948406739355176464': 'file_storage/function-call-17948406739355176464.json', 'var_function-call-1041647607165485382': ['Citations', 'sqlite_sequence'], 'var_function-call-1041647607165487633': 'file_storage/function-call-1041647607165487633.json', 'var_function-call-17075501722390720700': [], 'var_function-call-12172120259311764631': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_food': True, 'context': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_food': True, 'context': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_food': False, 'context': ''}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_food': True, 'context': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_food': False, 'context': ''}], 'var_function-call-14126767165602297505': [], 'var_function-call-785007343650812713': [{'title': 'A Lived Informatics Model of Personal Informatics', 'count': 13}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'count': 13}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 1}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'count': 0}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'count': 0}], 'var_function-call-4541425889179395715': 'file_storage/function-call-4541425889179395715.json'}

exec(code, env_args)
