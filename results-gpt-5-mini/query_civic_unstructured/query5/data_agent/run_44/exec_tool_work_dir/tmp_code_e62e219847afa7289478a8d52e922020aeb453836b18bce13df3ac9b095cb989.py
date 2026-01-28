code = """import json, re

# Load data from storage-provided file paths
with open(var_call_700c4RNVqoERyBs7mYYUhrdx, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_rQPtKlALSoTvo7VB8bJjUV50, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Prepare disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'recovery', 'federal assistance', 'woolsey', 'caljpia']

matches = []

# Iterate funding records
for row in funding_rows:
    proj = row.get('Project_Name', '')
    proj_lower = proj.lower()
    amount = row.get('Amount')
    try:
        amount_val = int(amount)
    except:
        try:
            amount_val = int(float(amount))
        except:
            amount_val = 0

    # Quick check: if project name itself references FEMA/CalOES/CalJPIA => disaster candidate
    proj_name_disaster = bool(re.search(r'\b(fema|caloes|caljpia)\b', proj, flags=re.I))

    found_disaster = False
    found_2022 = False
    found_any = False

    # Search through each civic doc for occurrences of the project name
    for doc in civic_docs:
        text = doc.get('text', '')
        text_lower = text.lower()
        if proj_lower in text_lower:
            found_any = True
            # find all occurrences
            for m in re.finditer(re.escape(proj_lower), text_lower):
                start = m.start()
                end = m.end()
                context_start = max(0, start-300)
                context_end = min(len(text), end+300)
                context = text_lower[context_start:context_end]
                # Check for 2022 in context
                if '2022' in context:
                    found_2022 = True
                # Check disaster keywords in context
                for kw in disaster_keywords:
                    if kw in context:
                        found_disaster = True
                        break
                if found_2022 and found_disaster:
                    break
            if found_2022 and found_disaster:
                break

    # If project name didn't appear in docs but project name itself flagged as disaster,
    # try a looser check: search docs for project base words (split by parentheses)
    if not found_any:
        base_name = re.split(r"\(|\\-\\(|\\/", proj)[0].strip()
        base_lower = base_name.lower()
        if base_lower and base_lower in ' '.join([d.get('text','').lower() for d in civic_docs]):
            # set found_any true and perform simpler checks
            found_any = True
            for doc in civic_docs:
                text = doc.get('text','').lower()
                if base_lower in text:
                    context = text
                    if '2022' in context:
                        found_2022 = True
                    for kw in disaster_keywords:
                        if kw in context:
                            found_disaster = True
                            break
                    if found_2022 and found_disaster:
                        break

    # Combine conditions: project is considered disaster-related if either name indicates or context indicates
    is_disaster = proj_name_disaster or found_disaster

    if is_disaster and found_2022:
        matches.append({
            'Project_Name': proj,
            'Amount': amount_val,
            'Funding_Source': row.get('Funding_Source')
        })

# Sum total
total = sum(m['Amount'] for m in matches)

result = {
    'total_funding': total,
    'matching_projects': matches
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JqEkj06PqqT9vxs2WACQElKm': ['civic_docs'], 'var_call_sgt5V7VAHDZL1U2g6euqA5Dr': ['Funding'], 'var_call_700c4RNVqoERyBs7mYYUhrdx': 'file_storage/call_700c4RNVqoERyBs7mYYUhrdx.json', 'var_call_rQPtKlALSoTvo7VB8bJjUV50': 'file_storage/call_rQPtKlALSoTvo7VB8bJjUV50.json'}

exec(code, env_args)
