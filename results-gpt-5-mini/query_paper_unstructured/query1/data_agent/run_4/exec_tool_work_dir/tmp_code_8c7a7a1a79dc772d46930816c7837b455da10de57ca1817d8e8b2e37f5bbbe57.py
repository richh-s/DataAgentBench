code = """import json
from pathlib import Path
# Load the Mongo query result stored in var_call_aAIpk8JudSUTsUKhmKgEWf3b
p = Path(var_call_aAIpk8JudSUTsUKhmKgEWf3b)
data = json.loads(p.read_text())

food_titles = []
for doc in data:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    domain_field = doc.get('domain')
    is_food = False
    if domain_field:
        # domain could be a string or list
        if isinstance(domain_field, list):
            for d in domain_field:
                if isinstance(d,str) and 'food' in d.lower():
                    is_food = True
                    break
        elif isinstance(domain_field, str):
            if 'food' in domain_field.lower():
                is_food = True
    # fallback: check text content for substring 'food'
    if not is_food:
        text = doc.get('text','')
        if isinstance(text,str) and 'food' in text.lower():
            is_food = True
    if is_food:
        food_titles.append(title)

# Remove duplicates
food_titles = sorted(list(dict.fromkeys(food_titles)))

import json
print("__RESULT__:")
print(json.dumps(food_titles))"""

env_args = {'var_call_pQOfsy41GlIFD19RbO1TdKkn': ['paper_docs'], 'var_call_aAIpk8JudSUTsUKhmKgEWf3b': 'file_storage/call_aAIpk8JudSUTsUKhmKgEWf3b.json'}

exec(code, env_args)
