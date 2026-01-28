code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_plNiYG8p4W4ASOxHbnUDjHE7
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path_funding = var_call_AqV75yZrkE4qz1C72Cio584Z
with open(path_funding, 'r') as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Heuristic project extraction: split texts on double newlines and treat all-caps or title-like lines as project headers
project_infos = []
for doc in civic_docs:
    text = doc.get('text','')
    # find lines that look like project names, followed by "Updates" and maybe schedule
    lines = [l.strip() for l in text.split('\n')]
    for i, line in enumerate(lines):
        if not line or len(line) > 120: 
            continue
        # candidate project line if it appears also in Funding.Project_Name prefix
        for pname in funding_df['Project_Name']:
            if pname.lower().startswith(line.lower()) or line.lower().startswith(pname.lower()):
                # collect context window
                context = " ".join(lines[i:i+15])
                topic = []
                if re.search(r'park', context, re.I):
                    topic.append('park')
                if re.search(r'playground', context, re.I):
                    topic.append('playground')
                status = None
                if re.search(r'construction was completed[, ]+([A-Za-z]+)?\s*2022', context, re.I):
                    status = 'completed'
                elif re.search(r'Construction was completed', context, re.I):
                    status = 'completed'
                elif re.search(r'Notice of completion', context, re.I):
                    status = 'completed'
                # find completion date tokens like 'November 2022'
                m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', context)
                et = m.group(0) if m else None
                # also generic year mentions
                if not et:
                    m2 = re.search(r'2022', context)
                    et = '2022' if m2 else None
                # classify type
                ptype = 'capital'
                if re.search(r'FEMA|CalOES|disaster', context, re.I):
                    ptype = 'disaster'
                project_infos.append({
                    'Project_Name': pname,
                    'topic': ','.join(sorted(set(topic))) if topic else None,
                    'type': ptype,
                    'status': status,
                    'st': None,
                    'et': et
                })
                break

proj_df = pd.DataFrame(project_infos).drop_duplicates(subset=['Project_Name','topic','status','et'])

# Filter park-related projects completed in 2022
mask_park = proj_df['topic'].fillna('').str.contains('park')
mask_completed = proj_df['status'].eq('completed')
mask_2022 = proj_df['et'].fillna('').str.contains('2022')
selected_proj = proj_df[mask_park & mask_completed & mask_2022]

# Join with funding
result = selected_proj.merge(funding_df, on='Project_Name', how='inner')

total_funding = int(result['Amount'].sum()) if not result.empty else 0

answer_obj = {
    'total_funding_park_completed_2022': total_funding,
    'matched_projects': result[['Project_Name','Amount']].to_dict(orient='records')
}

out = json.dumps(answer_obj)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_plNiYG8p4W4ASOxHbnUDjHE7': 'file_storage/call_plNiYG8p4W4ASOxHbnUDjHE7.json', 'var_call_AqV75yZrkE4qz1C72Cio584Z': 'file_storage/call_AqV75yZrkE4qz1C72Cio584Z.json'}

exec(code, env_args)
