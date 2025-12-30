code = """import json
import re

with open(locals()['var_function-call-8977914089601309835'], 'r') as f:
    docs = json.load(f)

completed_2022_projects = []

for doc in docs:
    text = doc['text']
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if i + 1 < len(lines) and lines[i+1].startswith('(cid:190)'):
            project_name = line
            project_block = []
            j = i + 1
            while j < len(lines):
                if j + 1 < len(lines) and lines[j+1].startswith('(cid:190)'):
                    break
                project_block.append(lines[j])
                j += 1
            full_text = " ".join(project_block)
            lower_text = full_text.lower()
            
            # Check for completion in 2022
            if re.search(r'(?:completed|complete construction).*?(?:january|february|march|april|may|june|july|august|september|october|november|december)[, ]+2022', lower_text):
                completed_2022_projects.append({"name": project_name, "text": full_text})
            
            i = j
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(completed_2022_projects))"""

env_args = {'var_function-call-14070122848874409329': ['civic_docs'], 'var_function-call-2375620709415017457': ['Funding'], 'var_function-call-15365523151233485332': 'file_storage/function-call-15365523151233485332.json', 'var_function-call-8977914089601309835': 'file_storage/function-call-8977914089601309835.json', 'var_function-call-5412922098617405934': ['Bluffs Park Shade Structure'], 'var_function-call-11008207917599906957': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}]}

exec(code, env_args)
