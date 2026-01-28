code = """import json
import pandas as pd

papers_path = locals()['var_function-call-1470986514462479797']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

rejected_samples = []

for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    lower_text = text.lower()
    
    is_food = False
    if 'food' in title.lower():
        is_food = True
    else:
        keyword_idx = lower_text.find('author keywords')
        if keyword_idx != -1:
            snippet = lower_text[keyword_idx:keyword_idx+500]
            end_idx = snippet.find('introduction')
            if end_idx == -1: end_idx = snippet.find('acm classification')
            if end_idx == -1: end_idx = 300
            keywords_section = snippet[:end_idx]
            if 'food' in keywords_section:
                is_food = True
    
    if not is_food:
        # It has "food" in text (because of Mongo filter) but we rejected it.
        # Let's find where "food" is.
        idx = lower_text.find('food')
        context = text[idx:idx+100] if idx != -1 else ""
        rejected_samples.append({"title": title, "context": context})

print("__RESULT__:")
print(json.dumps(rejected_samples[:5]))"""

env_args = {'var_function-call-2303008597307440717': 'file_storage/function-call-2303008597307440717.json', 'var_function-call-13231219773529852876': 'file_storage/function-call-13231219773529852876.json', 'var_function-call-1470986514462479797': 'file_storage/function-call-1470986514462479797.json', 'var_function-call-2063711702066525845': 270, 'var_function-call-16517891764845827685': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling']}

exec(code, env_args)
