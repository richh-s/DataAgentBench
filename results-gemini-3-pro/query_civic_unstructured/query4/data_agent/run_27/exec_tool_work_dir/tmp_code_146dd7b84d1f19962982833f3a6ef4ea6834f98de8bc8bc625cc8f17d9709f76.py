code = """import json

try:
    with open(locals()['var_function-call-640204841284110003'], 'r') as f:
        docs = json.load(f)
    with open(locals()['var_function-call-6371047367361917112'], 'r') as f:
        funding_recs = json.load(f)
except:
    docs = []
    funding_recs = []

funding_names = [r['Project_Name'] for r in funding_recs]
funding_names.sort(key=len, reverse=True)

found = set()
target_months = ['spring', 'march', 'april', 'may']

for doc in docs:
    text = doc.get('text', '')
    if not text: continue
    
    text_lower = text.lower()
    
    keywords = ["begin construction", "start construction"]
    start_indices = []
    for k in keywords:
        pos = text_lower.find(k)
        while pos != -1:
            start_indices.append(pos)
            pos = text_lower.find(k, pos + 1)
            
    for idx in start_indices:
        snippet = text_lower[idx:idx+100]
        if '2022' in snippet:
            is_match = False
            for m in target_months:
                if m in snippet:
                    is_match = True
                    break
            
            if is_match:
                best_proj = None
                best_proj_pos = -1
                
                search_limit = max(0, idx - 5000)
                preceding_text = text[search_limit:idx]
                
                for name in funding_names:
                    pos = preceding_text.rfind(name)
                    if pos != -1:
                        if pos > best_proj_pos:
                            best_proj_pos = pos
                            best_proj = name
                
                if best_proj:
                    found.add(best_proj)

print("__RESULT__:")
print(json.dumps(list(found)))"""

env_args = {'var_function-call-17327225246919229533': 'file_storage/function-call-17327225246919229533.json', 'var_function-call-6904797110646759006': 'file_storage/function-call-6904797110646759006.json', 'var_function-call-15743062509627089682': ['Funding'], 'var_function-call-6371047367361917112': 'file_storage/function-call-6371047367361917112.json', 'var_function-call-640204841284110003': 'file_storage/function-call-640204841284110003.json'}

exec(code, env_args)
