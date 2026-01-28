code = """import json, re
path = var_call_557VZrPhqUrgO6CAofXjAEsq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # check for physical activity mention: exact phrase or words within 50 chars
    if re.search(r'physical activity', text, re.I) or re.search(r'physical\W{0,50}activity', text, re.I) or (re.search(r'physical', text, re.I) and re.search(r'activity', text, re.I)):
        # find first occurrence of a 4-digit year in first 1000 chars
        head = text[:1000]
        year_match = re.search(r'\b(19|20)\d{2}\b', head)
        pub_year = None
        if year_match:
            pub_year = int(year_match.group(0))
        else:
            # look for patterns like 'CHI 2016' anywhere
            ym = re.search(r'\b(19|20)\d{2}\b', text)
            if ym:
                pub_year = int(ym.group(0))
        # additional heuristic: look for 'Proceedings of the .* 2016' near top
        if pub_year == 2016:
            candidates.append(title)

# remove duplicates
candidates = list(dict.fromkeys(candidates))
import json
print('__RESULT__:')
print(json.dumps(candidates))"""

env_args = {'var_call_VNEvq032PXm1hSsPWSIEbAc4': 'file_storage/call_VNEvq032PXm1hSsPWSIEbAc4.json', 'var_call_VAXyipWQI6VX8cowdguGGkry': [], 'var_call_557VZrPhqUrgO6CAofXjAEsq': 'file_storage/call_557VZrPhqUrgO6CAofXjAEsq.json'}

exec(code, env_args)
