code = """import json, re
# Load clinical query result from storage variable
path = var_call_sr3U50m0gueI782wn5P1q4Gy
with open(path, 'r') as f:
    data = json.load(f)

results = []
seen = set()
pattern = re.compile(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4})')
for rec in data:
    desc = rec.get('Patient_description','')
    hist = rec.get('histological_type', '')
    if not hist:
        continue
    hist_str = hist.strip()
    # exclude histology enclosed in square brackets entirely
    if hist_str.startswith('[') and hist_str.endswith(']'):
        continue
    m = pattern.search(desc)
    if not m:
        # try in patient_id field
        pid = rec.get('patient_id','')
        if pid and pid.startswith('TCGA'):
            code = pid
        else:
            continue
    else:
        code = m.group(1)
    if code in seen:
        continue
    seen.add(code)
    results.append({'ParticipantBarcode': code, 'histological_type': hist_str})

# Output the mapping as JSON string
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QAvxw7s3ZU4ykF0SSRDPAOhG': ['clinical_info'], 'var_call_xFmgT4sC7AzdEEJXSSi3huE3': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_LlUwkwZudcbKIoYqJCR0gneT': 'file_storage/call_LlUwkwZudcbKIoYqJCR0gneT.json', 'var_call_VCqogynOE3C6dz2dkn0ikboD': 'file_storage/call_VCqogynOE3C6dz2dkn0ikboD.json', 'var_call_sr3U50m0gueI782wn5P1q4Gy': 'file_storage/call_sr3U50m0gueI782wn5P1q4Gy.json'}

exec(code, env_args)
