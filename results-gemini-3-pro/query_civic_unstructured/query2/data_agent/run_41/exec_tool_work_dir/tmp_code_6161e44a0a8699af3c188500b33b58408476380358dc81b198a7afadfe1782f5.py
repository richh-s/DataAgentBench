code = """import json
import re

with open(locals()['var_function-call-4654103334756958724'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-4654103334756962095'], 'r') as f:
    funding_data = json.load(f)

projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('(cid:190) Updates') or line.startswith('(cid:190) Project Description'):
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                p_name = lines[j].strip()
                block_lines = []
                k = i
                while k < len(lines):
                    if k > i and (lines[k].strip().startswith('(cid:190) Updates') or lines[k].strip().startswith('(cid:190) Project Description')):
                        break
                    block_lines.append(lines[k])
                    k += 1
                p_text = ' '.join(block_lines)
                
                is_completed_2022 = False
                # Check for "Construction was completed" and "2022"
                # Use simple substring check first
                if 'Construction was completed' in p_text and '2022' in p_text:
                     is_completed_2022 = True
                # Also check "completed November 2022" etc.
                if 'completed' in p_text.lower() and '2022' in p_text:
                     # Verify with regex for closer proximity if needed, but the text blocks are small.
                     # Let's verify specific phrase from preview: "Construction was completed November 2022"
                     pass
                
                projects.append({'name': p_name, 'completed_2022': is_completed_2022})

total = 0
matched = []
keywords = ['park', 'playground', 'recreation']
# Use set to avoid duplicates if project appears in multiple docs?
# Or assume most recent status?
# If project appears in multiple docs, one might say "completed" and another "in progress" (older).
# The docs have dates. "03-22-23".
# The query asks for projects completed in 2022.
# If a document from 2023 says "Construction was completed Nov 2022", it counts.
# If a document from early 2022 says "in progress", it doesn't contradict.
# So if ANY document says it was completed in 2022, we count it.
# But we should not double count the funding.
# We should collect unique project names that meet the criteria.

unique_projects = set()

for p in projects:
    if p['completed_2022']:
        name_clean = p['name'].strip()
        # Check park
        if any(k in name_clean.lower() for k in keywords):
            unique_projects.add(name_clean)

# Now sum funding
for name in unique_projects:
    amount = 0
    # Find in funding data
    for f in funding_data:
        if f['Project_Name'].strip().lower() == name.lower():
            amount = f['Amount']
            break
    if amount > 0:
        total += amount
        matched.append({'name': name, 'amount': amount})

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': matched}))"""

env_args = {'var_function-call-4654103334756958724': 'file_storage/function-call-4654103334756958724.json', 'var_function-call-4654103334756962095': 'file_storage/function-call-4654103334756962095.json'}

exec(code, env_args)
