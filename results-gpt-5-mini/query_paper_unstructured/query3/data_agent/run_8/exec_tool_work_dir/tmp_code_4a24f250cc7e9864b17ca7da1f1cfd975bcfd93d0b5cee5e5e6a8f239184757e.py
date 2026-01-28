code = """import json, re
# Load the Mongo query result from storage variable
path = var_call_V3l4c1FCV6d0XAEGwntcPIui
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

selected_titles = []
selected_records = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    contribution = d.get('contribution')
    text = d.get('text','')
    year = d.get('year')
    # Normalize
    has_empirical = False
    if contribution:
        try:
            if 'empirical' in contribution.lower():
                has_empirical = True
        except Exception:
            pass
    if not has_empirical:
        if text and 'empirical' in text.lower():
            has_empirical = True
    # Extract year if missing or invalid
    year_int = None
    if isinstance(year, int):
        year_int = year
    else:
        # search for 4-digit years in text between 2017 and 2026
        matches = re.findall(r"20(1[7-9]|2[0-6])", text)
        if matches:
            # matches are like '17','18' etc due to grouping; reconstruct full year from matches
            # But re captured only last two digits; we can find full matches using a different approach
            full_matches = re.findall(r"20(?:1[7-9]|2[0-6])", text)
            if full_matches:
                try:
                    year_int = int(full_matches[0])
                except:
                    year_int = None
    if has_empirical and year_int and year_int > 2016:
        selected_titles.append(title)
        selected_records.append({'title': title, 'year': year_int})

# dedupe
unique_titles = []
seen = set()
for r in selected_records:
    t = r['title']
    if t not in seen:
        seen.add(t)
        unique_titles.append(r)

import json
print("__RESULT__:")
print(json.dumps(unique_titles))"""

env_args = {'var_call_V3l4c1FCV6d0XAEGwntcPIui': 'file_storage/call_V3l4c1FCV6d0XAEGwntcPIui.json'}

exec(code, env_args)
