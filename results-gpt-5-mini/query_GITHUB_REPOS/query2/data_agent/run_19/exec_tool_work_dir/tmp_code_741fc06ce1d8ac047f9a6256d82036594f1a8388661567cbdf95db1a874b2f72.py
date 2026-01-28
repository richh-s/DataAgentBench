code = """import json, re
# Load both large query results if available
records = []
for key in ['var_call_DOqIQ9EmEmqMdjhKYF5xge2C', 'var_call_x1F7ho40paHqd6gQrRddG274']:
    path = globals().get(key)
    if path:
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    records.extend(data)
        except Exception as e:
            pass

# Pattern to find explicit copy counts like 'repeated 21 times', 'copied 17 times', 'appearing 15 times', 'appears 1 times', 'appearing 7 times', 'appearing 1 times', 'appearing 38 times', 'seen 1 times'
pattern = re.compile(r"(repeated|copied|appearing|appears|appears|appearing|appears|appears|appears|appearing|appears|appears|appearing|seen|appearing|appearing|duplicated)\s+(?:.*?)?(\d+)\s+times", re.IGNORECASE)

# Also capture formats like 'appearing 7 times' or 'appearing 7 times,' and 'appears 1 times'
# Fallback: look for 'appearing (\d+) times' or 'copied (\d+) times' etc already covered.

def extract_copies(desc):
    if not desc:
        return 1
    # first try the explicit pattern
    m = pattern.search(desc)
    if m:
        try:
            return int(m.group(2))
        except:
            pass
    # fallback: look for 'appearing (\d+) times' simpler
    m2 = re.search(r"(\d+)\s+times", desc)
    if m2:
        return int(m2.group(1))
    # other fallback phrases
    m3 = re.search(r"copied\s+(\d+)", desc, re.IGNORECASE)
    if m3:
        return int(m3.group(1))
    m4 = re.search(r"appearing\s+(\d+)", desc, re.IGNORECASE)
    if m4:
        return int(m4.group(1))
    m5 = re.search(r"appears\s+(\d+)", desc, re.IGNORECASE)
    if m5:
        return int(m5.group(1))
    m6 = re.search(r"duplicated\s+(\d+)", desc, re.IGNORECASE)
    if m6:
        return int(m6.group(1))
    # If nothing found, return 1
    return 1

# Compute parsed copies for each record, protect duplicates by id keeping max
id_map = {}
for r in records:
    rid = r.get('id')
    desc = r.get('repo_data_description','') or ''
    copies = extract_copies(desc)
    # Also consider phrasing like 'appearing 1 times, using sample mode 33261' where 'seen 1 times, using sample mode 33261' should parse as 1
    # Use maximum if id repeats
    if rid in id_map:
        if copies > id_map[rid]['copies']:
            id_map[rid] = {'copies': copies, 'any_repo': r.get('any_repo'), 'any_path': r.get('any_path'), 'repo_data_description': desc}
    else:
        id_map[rid] = {'copies': copies, 'any_repo': r.get('any_repo'), 'any_path': r.get('any_path'), 'repo_data_description': desc}

# Find max
if not id_map:
    output = {'max_copies': 0, 'top_ids': []}
else:
    max_copies = max(v['copies'] for v in id_map.values())
    top = [ {'id': k, 'copies': v['copies'], 'any_repo': v['any_repo'], 'any_path': v['any_path'], 'repo_data_description': v['repo_data_description']} for k,v in id_map.items() if v['copies']==max_copies ]
    output = {'max_copies': max_copies, 'top_ids': top}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_QCEF4EENSwc1rWuQhx7QQFyS': [], 'var_call_DOqIQ9EmEmqMdjhKYF5xge2C': 'file_storage/call_DOqIQ9EmEmqMdjhKYF5xge2C.json', 'var_call_EdcoI6Abh0pPUAyTtXxAemox': [], 'var_call_x1F7ho40paHqd6gQrRddG274': 'file_storage/call_x1F7ho40paHqd6gQrRddG274.json', 'var_call_RloITwH3ggQel9JoksjJ8ipZ': [], 'var_call_5HtE6P62FeOLEM1yLMhW7Ek9': {'max_copies': 33261, 'records': [{'id': '9ef2e30e948f45194e614aca0e7a18cef17836e1', 'parsed_copies': 33261, 'any_repo': 'LesCoureurs/Courir', 'any_path': 'Courir/Pods/SwiftyGif/SwiftyGif/UIImageView+SwiftyGif.swift', 'repo_data_description': 'Non-binary content file (7360 bytes) seen 1 times, using sample mode 33261.'}, {'id': 'f6ec334d38084d8ff0ffa388e8550b01e245ea60', 'parsed_copies': 33261, 'any_repo': 'Mozharovsky/CVCalendar', 'any_path': 'CVCalendar Demo/CVCalendar/CVCalendarWeekContentViewController.swift', 'repo_data_description': 'Non-binary content file (20194 bytes) seen 7 times, using sample mode 33261.'}]}}

exec(code, env_args)
