code = """import json
import re

with open(locals()['var_function-call-17959813920400142644'], 'r') as f:
    paper_docs = json.load(f)

debug_list = []
food_in_title = []
food_in_text_count = 0

for doc in paper_docs[:10]:
    text = doc['text']
    filename = doc['filename']
    lower_text = text.lower()
    
    match = re.search(r'(author\s+keywords|index\s+terms|keywords)', lower_text)
    extracted = "NOT FOUND"
    if match:
        start = match.end()
        chunk = lower_text[start:start+500]
        extracted = chunk
    
    debug_list.append({
        "filename": filename,
        "keywords_snippet": extracted[:200].replace('\n', ' ')
    })

for doc in paper_docs:
    filename = doc['filename']
    if 'food' in filename.lower():
        food_in_title.append(filename)
    if 'food' in doc['text'].lower():
        food_in_text_count += 1

print("__RESULT__:")
print(json.dumps({
    "debug_snippets": debug_list,
    "food_in_title": food_in_title,
    "food_in_text_count": food_in_text_count
}))"""

env_args = {'var_function-call-12772568682444921532': 'file_storage/function-call-12772568682444921532.json', 'var_function-call-268740664748096753': 'file_storage/function-call-268740664748096753.json', 'var_function-call-17959813920400142644': 'file_storage/function-call-17959813920400142644.json', 'var_function-call-14824333924694724411': 'file_storage/function-call-14824333924694724411.json', 'var_function-call-6392359925411315977': {'food_papers_count': 0, 'food_papers': [], 'total_citations': 0}}

exec(code, env_args)
