code = """import json

with open(locals()['var_function-call-17971925795973344162'], 'r') as f:
    docs = json.load(f)

matches = []
debug_failures = []

for doc in docs:
    text = doc.get('text', '')
    title = doc.get('filename', '').replace('.txt', '')
    
    # improved extraction
    start_idx = -1
    for h in ['Author Keywords', 'Keywords', 'Index Terms']:
        idx = text.find(h)
        if idx != -1:
            start_idx = idx
            break
    
    if start_idx != -1:
        # Take a chunk
        chunk = text[start_idx:start_idx+500]
        # Normalize
        chunk_lower = chunk.lower()
        
        # Check for food terms in this chunk
        if 'food' in chunk_lower or 'diet' in chunk_lower or 'nutrition' in chunk_lower or 'eating' in chunk_lower:
            matches.append({'title': title, 'chunk': chunk})
    else:
        debug_failures.append(title)

print('__RESULT__:')
print(json.dumps({'matches': matches, 'failures': debug_failures}))"""

env_args = {'var_function-call-8748244462217434689': ['paper_docs'], 'var_function-call-8748244462217434842': ['Citations', 'sqlite_sequence'], 'var_function-call-10817664668211665430': 'file_storage/function-call-10817664668211665430.json', 'var_function-call-4112176734939169200': 'file_storage/function-call-4112176734939169200.json', 'var_function-call-17971925795973344162': 'file_storage/function-call-17971925795973344162.json', 'var_function-call-17971925795973342135': 'file_storage/function-call-17971925795973342135.json', 'var_function-call-5998872397712651256': {'food_titles': [], 'total_citations': 0, 'debug': []}, 'var_function-call-4583320178821864395': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords': 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers '}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords': 'Author Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords': 'Author Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  '}], 'var_function-call-4734933450304784714': {'food_in_title': [], 'food_in_keywords': [], 'food_in_text_samples': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}]}, 'var_function-call-9499828237160051961': [{'title': 'A Lived Informatics Model of Personal Informatics', 'kw': 'Author Keywords  Lived Informatics; Personal Informatics; Self-Tracking;  Lapsing; Physical Activity; Finances; Location. '}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'kw': 'Author Keywords  Personal informatics, collection, reflection, model, barriers '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'kw': 'Author Keywords Personalization; animation; emotion; engagement; empathy; self-reﬂection.'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'kw': ''}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'kw': 'Author Keywords  Wearable technology; dashboard; information visualization;  stroke rehabilitation; occupational therapy  '}]}

exec(code, env_args)
