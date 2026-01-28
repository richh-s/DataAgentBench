code = """import json

with open('var_function-call-16068548023573727845.json', 'r') as f:
    civic_docs = json.load(f)

extracted = []

def check_date(line):
    l = line.lower()
    if 'spring 2022' in l or 'spring, 2022' in l or 'march 2022' in l or 'april 2022' in l or 'may 2022' in l:
        return True
    return False

def check_start(line):
    l = line.lower()
    if 'complete' in l or 'finish' in l:
        return False
    if 'begin' in l or 'start' in l or 'advertise' in l:
        return True
    return True

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        if 'Updates:' in line:
            k = i - 1
            while k >= 0 and not lines[k].strip():
                k -= 1
            if k >= 0:
                p_name = lines[k].strip()
                j = i + 1
                while j < len(lines):
                    if 'Updates:' in lines[j]:
                        break
                    l_content = lines[j].strip()
                    if check_date(l_content) and check_start(l_content):
                        extracted.append({'name': p_name, 'line': l_content})
                    j += 1

print("__RESULT__:")
print(json.dumps(extracted))"""

env_args = {'var_function-call-16068548023573727845': 'file_storage/function-call-16068548023573727845.json', 'var_function-call-9691267540857789545': 'file_storage/function-call-9691267540857789545.json'}

exec(code, env_args)
