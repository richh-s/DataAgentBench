code = """import json, pandas as pd

best = var_call_dIu7Tr9FOmxJ2MwKvE46UkeZ
# Load CPC level-4 definitions
file_path_def = var_call_JUKBtYps6dWEHUWqqNQmWVHy
import os, json as js
with open(file_path_def, 'r') as f:
    defs = js.load(f)

# Build map from symbol (e.g., 'B29') to title
sym_map = {d['symbol']: d['titleFull'] for d in defs}

result = []
for rec in best:
    grp = rec['group']
    title = sym_map.get(grp)
    result.append({
        'cpc_group_code_level4': grp,
        'titleFull': title,
        'best_year': rec['year'],
        'ema': rec['ema']
    })

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_O7x0H6MwHWn7bMuOX2zmmWih': 'file_storage/call_O7x0H6MwHWn7bMuOX2zmmWih.json', 'var_call_JUKBtYps6dWEHUWqqNQmWVHy': 'file_storage/call_JUKBtYps6dWEHUWqqNQmWVHy.json', 'var_call_nBUJK6egGwu7GqAvvOgGwacW': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}], 'var_call_dIu7Tr9FOmxJ2MwKvE46UkeZ': [{'group': 'A21', 'year': 2019, 'ema': 1.0}, {'group': 'A43', 'year': 2019, 'ema': 5.0}, {'group': 'A47', 'year': 2019, 'ema': 1.0}, {'group': 'A61', 'year': 2019, 'ema': 13.0}, {'group': 'B29', 'year': 2019, 'ema': 15.0}, {'group': 'B41', 'year': 2019, 'ema': 3.0}, {'group': 'B60', 'year': 2019, 'ema': 4.0}, {'group': 'B63', 'year': 2019, 'ema': 1.0}, {'group': 'B64', 'year': 2019, 'ema': 1.0}, {'group': 'B66', 'year': 2019, 'ema': 1.0}, {'group': 'C04', 'year': 2019, 'ema': 45.0}, {'group': 'C09', 'year': 2019, 'ema': 2.0}, {'group': 'E02', 'year': 2019, 'ema': 6.0}, {'group': 'E21', 'year': 2019, 'ema': 5.0}, {'group': 'F01', 'year': 2019, 'ema': 4.0}, {'group': 'F02', 'year': 2019, 'ema': 30.0}, {'group': 'F04', 'year': 2019, 'ema': 16.0}, {'group': 'F41', 'year': 2019, 'ema': 2.0}, {'group': 'F42', 'year': 2019, 'ema': 2.0}, {'group': 'G01', 'year': 2019, 'ema': 3.0}, {'group': 'G02', 'year': 2019, 'ema': 12.0}, {'group': 'H01', 'year': 2019, 'ema': 20.0}, {'group': 'H02', 'year': 2019, 'ema': 6.0}, {'group': 'Y02', 'year': 2019, 'ema': 3.0}]}

exec(code, env_args)
