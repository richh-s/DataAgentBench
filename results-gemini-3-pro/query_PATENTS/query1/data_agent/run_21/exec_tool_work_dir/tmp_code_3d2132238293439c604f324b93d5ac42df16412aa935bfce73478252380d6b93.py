code = """import json
import re

# Load paths
path_cpc = locals()['var_function-call-15650209111599627391']
path_pubs = locals()['var_function-call-13092592968484268973']

# Check Level 5 codes
with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)
l5_codes = [item['symbol'] for item in cpc_defs]
print(f"DEBUG: Number of Level 5 codes: {len(l5_codes)}")
print(f"DEBUG: Sample Level 5 codes: {l5_codes[:10]}")

# Check Publication Data
with open(path_pubs, 'r') as f:
    pubs = json.load(f)

print(f"DEBUG: Number of pubs: {len(pubs)}")

date_pattern = re.compile(r'\b(19|20)\d{2}\b')
years = []
sample_dates = []
sample_cpc_extracted = []

for i, p in enumerate(pubs[:100]): # Check first 100
    f_date = p.get('filing_date', '')
    if f_date:
        sample_dates.append(f_date)
        match = date_pattern.search(f_date)
        if match:
            years.append(int(match.group(0)))
            
    cpc_str = p.get('cpc', '')
    if cpc_str:
        try:
            cpc_list = json.loads(cpc_str)
            codes = [x.get('code', '') for x in cpc_list]
            # Extract potential subclass (4 chars)
            subclasses = [c[:4] for c in codes if len(c) >= 4]
            if i < 5:
                sample_cpc_extracted.append((cpc_str[:50] + "...", subclasses))
        except:
            pass

print(f"DEBUG: Sample Dates: {sample_dates[:5]}")
print(f"DEBUG: Extracted Years: {years[:5]}")
if years:
    print(f"DEBUG: Min Year: {min(years)}, Max Year: {max(years)}")
else:
    print("DEBUG: No years extracted.")

print(f"DEBUG: Sample CPC Extracted: {sample_cpc_extracted}")

# Check intersection
l5_set = set(l5_codes)
matched_count = 0
for p in pubs[:1000]:
    cpc_str = p.get('cpc', '')
    try:
        cpc_list = json.loads(cpc_str)
        for x in cpc_list:
            c = x.get('code', '')
            if len(c) >= 4:
                if c[:4] in l5_set:
                    matched_count += 1
                    break
    except:
        pass

print(f"DEBUG: Matches found in first 1000 pubs: {matched_count}")

print("__RESULT__:")
print("Check logs")"""

env_args = {'var_function-call-15650209111599627391': 'file_storage/function-call-15650209111599627391.json', 'var_function-call-13092592968484268973': 'file_storage/function-call-13092592968484268973.json', 'var_function-call-348235414228454795': []}

exec(code, env_args)
