code = """import json

with open(locals()['var_function-call-17971925795973344162'], 'r') as f:
    docs = json.load(f)

food_in_title = []
food_in_keywords = []
food_in_text_samples = []

newline = chr(10)
double_newline = newline + newline

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_in_title.append(title)
        
    # Check keywords extraction again
    start_idx = -1
    keywords_headers = ['Author Keywords', 'Keywords', 'Index Terms']
    for kw_header in keywords_headers:
        idx = text.find(kw_header)
        if idx != -1:
            start_idx = idx
            break
    
    keywords_block = ""
    if start_idx != -1:
        subtext = text[start_idx:]
        end_idx = subtext.find(double_newline)
        if end_idx == -1: end_idx = 1000
        keywords_block = subtext[:end_idx].lower()
        if 'food' in keywords_block:
            food_in_keywords.append(title)
            
    # Check text context
    if 'food' in text.lower():
        # find where
        idx = text.lower().find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)].replace('\n', ' ')
        if len(food_in_text_samples) < 5:
            food_in_text_samples.append({"title": title, "snippet": snippet})

print('__RESULT__:')
print(json.dumps({
    "food_in_title": food_in_title,
    "food_in_keywords": food_in_keywords,
    "food_in_text_samples": food_in_text_samples
}))"""

env_args = {'var_function-call-8748244462217434689': ['paper_docs'], 'var_function-call-8748244462217434842': ['Citations', 'sqlite_sequence'], 'var_function-call-10817664668211665430': 'file_storage/function-call-10817664668211665430.json', 'var_function-call-4112176734939169200': 'file_storage/function-call-4112176734939169200.json', 'var_function-call-17971925795973344162': 'file_storage/function-call-17971925795973344162.json', 'var_function-call-17971925795973342135': 'file_storage/function-call-17971925795973342135.json', 'var_function-call-5998872397712651256': {'food_titles': [], 'total_citations': 0, 'debug': []}, 'var_function-call-4583320178821864395': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords': 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers '}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords': 'Author Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords': 'Author Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  '}]}

exec(code, env_args)
