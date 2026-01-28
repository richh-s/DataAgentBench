code = """import json
path = var_call_bFWevv3m4UiSTymHbwzrNNrc
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

# Convert Amount strings to integers
for r in rows:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

# load civic park-related completed-in-2022 project names from previous result
park_projects = var_call_38i97AxeFe4LtdSqT17QEvSZ
# Normalize names for matching: lower and strip
park_norm = [p.lower().strip() for p in park_projects]

# We'll match funding records whose Project_Name lower contains any of the park_norm as substring,
# or funding Project_Name contains 'park' and project name also in civic docs matching variants.
matched = []
for r in rows:
    pname = r['Project_Name']
    plow = pname.lower()
    for p in park_norm:
        if p in plow:
            matched.append(r)
            break
    else:
        # also match if both contain 'park' and first two words match
        if 'park' in plow:
            for p in park_norm:
                if 'park' in p:
                    # compare first two words
                    if ' '.join(p.split()[:2]) == ' '.join(plow.split()[:2]):
                        matched.append(r)
                        break

# Deduplicate matched by Project_Name
uniq = {}
for m in matched:
    uniq[m['Project_Name']] = m['Amount']

total = sum(uniq.values())
print('__RESULT__:')
print(json.dumps({'park_projects_found': park_projects, 'matched_funding_records': list(uniq.items()), 'total_funding': total}))"""

env_args = {'var_call_V4vF7nwAMnAbiopKMftn913k': ['civic_docs'], 'var_call_zhqmXNrCRCQ3GsnKQ7jhMenX': ['Funding'], 'var_call_V2Ly6OD6obg5ajtxJc9hBho4': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json', 'var_call_hpPReWfvyf7lehCWFK0cGfHh': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json', 'var_call_38i97AxeFe4LtdSqT17QEvSZ': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements', 'need of replacing at Malibu Bluffs Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'the Malibu Park Drainage', 'to Malibu Bluffs Park. The project would include parking and additional site'], 'var_call_bFWevv3m4UiSTymHbwzrNNrc': 'file_storage/call_bFWevv3m4UiSTymHbwzrNNrc.json'}

exec(code, env_args)
