code = """import json

# Load papers
with open(locals()['var_function-call-12774124181016147194'], 'r') as f:
    papers_data = json.load(f)

debug_info = []
count = 0
for p in papers_data:
    if 'food' in p['text'].lower():
        count += 1
        if count <= 5:
            info = f"--- Match in: {p['filename']} ---"
            # Find context
            text_lower = p['text'].lower()
            idx = text_lower.find('food')
            context = p['text'][max(0, idx-50):min(len(p['text']), idx+50)].replace('\n', ' ')
            info += f" Context: ...{context}..."
            debug_info.append(info)

result = {
    "count": count,
    "examples": debug_info
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2229407460365091455': 'file_storage/function-call-2229407460365091455.json', 'var_function-call-12774124181016146207': 'file_storage/function-call-12774124181016146207.json', 'var_function-call-12774124181016147194': 'file_storage/function-call-12774124181016147194.json', 'var_function-call-12375458960310420055': '0', 'var_function-call-10051261772612968329': 'done'}

exec(code, env_args)
