code = """import json
import pandas as pd

# Load the funding and civic docs results from storage file paths
with open(var_call_pHSFdb8FjdxkeO7wjTzX1JVt, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_iBp1zVlSVLnRgP1f4RpFytUi, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Convert funding to DataFrame
df_f = pd.DataFrame(funding_records)
# Ensure Amount as int
df_f['Amount'] = df_f['Amount'].astype(int)
# Normalize project names
df_f['Project_Name_lower'] = df_f['Project_Name'].str.lower()

# Find completed projects in 2022 from civic docs
completed_titles = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if 'completed' in line.lower() and '2022' in line:
            # search backwards for title
            j = idx-1
            title = None
            while j >= 0:
                lj = lines[j].strip()
                if lj and not lj.lower().startswith('(cid') and 'updates:' not in lj.lower() and 'agenda' not in lj.lower():
                    title = lj
                    break
                j -= 1
            if title:
                # clean title
                title_clean = ' '.join(title.split())
                completed_titles.add(title_clean)

# Also search for lines like "Construction was completed, November 2022" (handled above)
# Filter completed titles for park-related keywords
park_keywords = ['park', 'playground']
completed_park_titles = [t for t in completed_titles if any(k in t.lower() for k in park_keywords)]

# Now match funding records whose Project_Name matches any of these titles (substring match)
matched_rows = []
for _, row in df_f.iterrows():
    pname = row['Project_Name_lower']
    for title in completed_park_titles:
        tl = title.lower()
        if tl in pname or pname in tl or any(k in pname for k in park_keywords):
            # ensure the funding record is park-related and matches the completed list
            # We'll include it if the funding project name contains a park keyword and either contains the title or title contains park keyword
            if any(k in pname for k in park_keywords):
                matched_rows.append({
                    'Funding_ID': int(row['Funding_ID']),
                    'Project_Name': row['Project_Name'],
                    'Amount': int(row['Amount'])
                })
                break

# Deduplicate matched rows by Funding_ID
unique_matches = {r['Funding_ID']: r for r in matched_rows}
matched_list = list(unique_matches.values())

total = sum(r['Amount'] for r in matched_list)

result = {
    'completed_park_titles_found': completed_park_titles,
    'matched_funding_records': matched_list,
    'total_funding': total
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pHSFdb8FjdxkeO7wjTzX1JVt': 'file_storage/call_pHSFdb8FjdxkeO7wjTzX1JVt.json', 'var_call_wWm7D8KHYWdV7hnB7OkLytIF': ['civic_docs'], 'var_call_iBp1zVlSVLnRgP1f4RpFytUi': 'file_storage/call_iBp1zVlSVLnRgP1f4RpFytUi.json'}

exec(code, env_args)
