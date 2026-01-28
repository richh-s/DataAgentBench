code = """import json

with open(locals()['var_function-call-6242695006040143543'], 'r') as f:
    papers_data = json.load(f)

excluded = []
for p in papers_data:
    text_lower = p['text'].lower()
    filename_lower = p['filename'].lower()
    
    is_food = False
    if "food" in filename_lower:
        is_food = True
    else:
        idx = text_lower.find("keywords")
        if idx != -1:
            chunk = text_lower[idx:idx+500]
            if "food" in chunk:
                is_food = True
    
    if not is_food:
        excluded.append(p['filename'])

print("__RESULT__:")
print(json.dumps(excluded[:20]))"""

env_args = {'var_function-call-8429523015460398318': 'file_storage/function-call-8429523015460398318.json', 'var_function-call-495826835805715086': 'file_storage/function-call-495826835805715086.json', 'var_function-call-7751700414245967410': 'file_storage/function-call-7751700414245967410.json', 'var_function-call-6242695006040143543': 'file_storage/function-call-6242695006040143543.json', 'var_function-call-16629806650409149598': {'food_papers_count': 1, 'food_papers_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'total_citations': 270}}

exec(code, env_args)
