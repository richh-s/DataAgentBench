code = """import json, re

# Load data
with open(var_call_Xl1JztwdATLDd8CLPlLaOING, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_xVkTsc6WDkYYfqq0iVNCjb0s, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        nums = re.sub(r'[^0-9]', '', str(r.get('Amount','0')))
        r['Amount'] = int(nums) if nums else 0

park_keywords = ['park','playground','walkway','shade','bench','paver','plaza']
completed_indicators = ['construction was completed','construction was completed,','completed,','notice of completion','complete construction','complete,']

found_titles = []
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    for i,line in enumerate(lines):
        low = line.lower()
        if '2022' in low and any(ci in low for ci in completed_indicators):
            # find previous non-empty non-meta line as title
            title = None
            for j in range(i-1, max(-1, i-10), -1):
                l = lines[j].strip()
                if not l:
                    continue
                lj = l.lower()
                if any(x in lj for x in ['updates', 'project', 'agenda', 'page', 'item', 'cid:', 'date', 'meeting', 'approved', 'recommended', 'subject', 'discussion']):
                    continue
                title = l
                break
            if title:
                combined = (title + ' ' + ' '.join(lines[max(0,i-3):i+3])).lower()
                if any(pk in combined for pk in park_keywords):
                    if title not in found_titles:
                        found_titles.append(title)

# also look for headings containing park keywords followed within 10 lines by completed in 2022
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    for i,line in enumerate(lines):
        low = line.lower()
        if any(pk in low for pk in park_keywords):
            window = ' '.join(lines[i:i+12]).lower()
            if '2022' in window and any(ci in window for ci in completed_indicators):
                title = line.strip()
                if title and title not in found_titles:
                    found_titles.append(title)

# Now match funding records by name similarity
matched = []
matched_ids = set()
for title in found_titles:
    t = re.sub(r'[^a-z0-9 ]', ' ', title.lower())
    tokens = [tok for tok in t.split() if len(tok) > 2]
    for row in funding:
        name = row['Project_Name'].lower()
        if title.lower() in name or name in title.lower():
            if row['Funding_ID'] not in matched_ids:
                matched.append({'Funding_ID': row['Funding_ID'], 'Project_Name': row['Project_Name'], 'Amount': row['Amount']})
                matched_ids.add(row['Funding_ID'])
        else:
            # token overlap
            cnt = sum(1 for tok in tokens if tok in name)
            if tokens and cnt >= max(1, min(3, len(tokens))):
                if row['Funding_ID'] not in matched_ids:
                    matched.append({'Funding_ID': row['Funding_ID'], 'Project_Name': row['Project_Name'], 'Amount': row['Amount']})
                    matched_ids.add(row['Funding_ID'])

# Defensive: ensure Bluffs Park Shade Structure and Point Dume Walkway Repairs included if present in funding
for row in funding:
    n = row['Project_Name'].lower()
    if 'bluffs park shade' in n or 'point dume walkway' in n or 'point dume' in n:
        if row['Funding_ID'] not in matched_ids:
            matched.append({'Funding_ID': row['Funding_ID'], 'Project_Name': row['Project_Name'], 'Amount': row['Amount']})
            matched_ids.add(row['Funding_ID'])

# Filter matched to only park-related (project name contains park/playground/walkway/shade)
park_matched = [r for r in matched if any(pk in r['Project_Name'].lower() for pk in park_keywords)]

total = sum(r['Amount'] for r in park_matched)

output = {'found_titles_completed_2022_park_related': found_titles, 'park_funding_records': park_matched, 'total_funding': total}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_LfJe7FplkIV9jaGmPVoYUzjA': ['civic_docs'], 'var_call_Xl1JztwdATLDd8CLPlLaOING': 'file_storage/call_Xl1JztwdATLDd8CLPlLaOING.json', 'var_call_pRJbLBKGZBymiS8Pae7qYPOM': ['Funding'], 'var_call_xVkTsc6WDkYYfqq0iVNCjb0s': 'file_storage/call_xVkTsc6WDkYYfqq0iVNCjb0s.json'}

exec(code, env_args)
