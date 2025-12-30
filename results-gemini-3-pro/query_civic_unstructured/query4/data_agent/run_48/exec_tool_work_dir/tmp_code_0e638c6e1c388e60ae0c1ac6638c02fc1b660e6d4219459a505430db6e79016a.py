code = """import json

with open('var_function-call-16068548023573727845.json', 'r') as f:
    civic_docs = json.load(f)

projects_found = []

def check_date(line):
    l = line.lower()
    # Check for Spring 2022
    if 'spring 2022' in l or 'spring, 2022' in l or 'march 2022' in l or 'april 2022' in l or 'may 2022' in l:
        return True
    return False

def check_start(line):
    l = line.lower()
    if 'complete' in l or 'finish' in l:
        return False
    # If explicitly says Begin/Start/Advertise
    if 'begin' in l or 'start' in l or 'advertise' in l:
        return True
    # If no keyword, assume it might be a schedule item
    return True # Be generous, filtering later if needed

extracted = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Simple state machine
    # Store lines between "Updates:" markers
    # The line BEFORE "Updates:" is the Project Name.
    
    for i, line in enumerate(lines):
        if 'Updates:' in line:
            # Look back for name
            # Skip empty lines backwards
            k = i - 1
            while k >= 0 and not lines[k].strip():
                k -= 1
            if k >= 0:
                p_name = lines[k].strip()
                
                # Now look forward for dates until next "Updates:"
                # or end of file
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
