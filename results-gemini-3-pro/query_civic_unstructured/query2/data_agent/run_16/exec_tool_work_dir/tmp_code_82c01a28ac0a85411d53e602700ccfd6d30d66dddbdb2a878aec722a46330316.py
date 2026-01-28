code = """import json
import re

with open(locals()['var_function-call-2466750499459274811'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-3057395287432783199'], 'r') as f:
    civic_docs = json.load(f)

project_names = [r['Project_Name'] for r in funding_data]
project_names.sort(key=len, reverse=True)

completed_2022_projects = set()

# Regex patterns for completion in 2022 (escaped for JSON string)
completion_patterns = [
    r"construction\s+was\s+completed,?\s+([a-zA-Z]+)?\s?2022",
    r"complete\s+construction:?\s+([a-zA-Z]+)?\s?2022",
    r"construction\s+completed\s+([a-zA-Z]+)?\s?2022"
]

def check_park_related(text):
    text_lower = text.lower()
    keywords = ['park', 'playground', 'recreation']
    return any(k in text_lower for k in keywords)

for doc in civic_docs:
    text = doc['text']
    
    for pname in project_names:
        pname_esc = re.escape(pname)
        for match in re.finditer(pname_esc, text, re.IGNORECASE):
            start = match.end()
            context = text[start:start+1000]
            
            is_park = check_park_related(pname) or check_park_related(context)
            
            if is_park:
                is_completed_2022 = False
                for pat in completion_patterns:
                    if re.search(pat, context, re.IGNORECASE):
                        is_completed_2022 = True
                        break
                
                if is_completed_2022:
                    completed_2022_projects.add(pname)

total_funding = 0
for r in funding_data:
    if r['Project_Name'] in completed_2022_projects:
        total_funding += int(r['Amount'])

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(completed_2022_projects)}))"""

env_args = {'var_function-call-2466750499459274811': 'file_storage/function-call-2466750499459274811.json', 'var_function-call-2466750499459274820': 'file_storage/function-call-2466750499459274820.json', 'var_function-call-3057395287432783199': 'file_storage/function-call-3057395287432783199.json'}

exec(code, env_args)
