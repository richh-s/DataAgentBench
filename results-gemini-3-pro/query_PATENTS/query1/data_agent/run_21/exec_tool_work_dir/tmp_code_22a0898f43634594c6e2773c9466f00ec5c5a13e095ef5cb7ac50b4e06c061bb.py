code = """import json
import re

# Load paths
path_cpc = locals()['var_function-call-15650209111599627391']
path_pubs = locals()['var_function-call-13092592968484268973']

debug_info = {}

# Check Level 5 codes
with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)
l5_codes = [item['symbol'] for item in cpc_defs]
debug_info['l5_count'] = len(l5_codes)
debug_info['l5_samples'] = l5_codes[:10]

# Check Publication Data
with open(path_pubs, 'r') as f:
    pubs = json.load(f)

debug_info['pubs_count'] = len(pubs)

date_pattern = re.compile(r'\b(19|20)\d{2}\b')
years = []
sample_dates = []
sample_cpc_extracted = []

for i, p in enumerate(pubs[:100]):
    f_date = p.get('filing_date', '')
    if f_date:
        if len(sample_dates) < 5:
            sample_dates.append(f_date)
        match = date_pattern.search(f_date)
        if match:
            years.append(int(match.group(0)))
            
    cpc_str = p.get('cpc', '')
    if cpc_str:
        try:
            cpc_list = json.loads(cpc_str)
            codes = [x.get('code', '') for x in cpc_list]
            subclasses = [c[:4] for c in codes if len(c) >= 4]
            if len(sample_cpc_extracted) < 5:
                sample_cpc_extracted.append(subclasses)
        except:
            pass

debug_info['sample_dates'] = sample_dates
debug_info['extracted_years'] = years[:10]
if years:
    debug_info['min_year'] = min(years)
    debug_info['max_year'] = max(years)

debug_info['sample_cpc_extracted'] = sample_cpc_extracted

# Check intersection
l5_set = set(l5_codes)
matched_count = 0
for p in pubs[:1000]:
    cpc_str = p.get('cpc', '')
    try:
        cpc_list = json.loads(cpc_str)
        found = False
        for x in cpc_list:
            c = x.get('code', '')
            if len(c) >= 4:
                if c[:4] in l5_set:
                    found = True
                    break
        if found:
            matched_count += 1
    except:
        pass

debug_info['matches_in_1000'] = matched_count

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15650209111599627391': 'file_storage/function-call-15650209111599627391.json', 'var_function-call-13092592968484268973': 'file_storage/function-call-13092592968484268973.json', 'var_function-call-348235414228454795': []}

exec(code, env_args)
