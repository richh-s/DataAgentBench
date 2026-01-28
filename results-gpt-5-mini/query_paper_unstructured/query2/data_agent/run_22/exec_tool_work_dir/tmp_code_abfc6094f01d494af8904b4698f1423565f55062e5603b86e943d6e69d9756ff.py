code = """import json
import re

# Load the MongoDB query result from storage variable
path = var_call_oum8fEP9La2Fq9G8QzYIelui
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

acm_titles = []
for doc in docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # Consider it ACM if 'ACM' appears as a whole word or 'Copyright' followed by ACM
    if re.search(r'\bACM\b', text, re.IGNORECASE) or re.search(r'Copyright.*ACM', text, re.IGNORECASE):
        acm_titles.append(title)

# Deduplicate
acm_titles = sorted(list(dict.fromkeys(acm_titles)))

output = json.dumps({"acm_titles": acm_titles}, ensure_ascii=False)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_oum8fEP9La2Fq9G8QzYIelui': 'file_storage/call_oum8fEP9La2Fq9G8QzYIelui.json'}

exec(code, env_args)
