code = """import json
import re
import pandas as pd

# Load clinical_info query result
with open(var_call_Aqx3og4knI7XgSyuA3gd75Lf, 'r') as f:
    clinical = json.load(f)

# Make DataFrame
df = pd.DataFrame(clinical)

# Function to extract TCGA barcode from Patient_description
barcode_re = re.compile(r'TCGA[-][0-9A-Z]{2}[-][0-9A-Z]{4}', re.IGNORECASE)

lgd_mask = df['Patient_description'].astype(str).str.contains('Lower Grade Glioma', case=False, na=False) | df['Patient_description'].astype(str).str.contains('Lower grade glioma', case=False, na=False) | df['Patient_description'].astype(str).str.contains('Brain Lower Grade', case=False, na=False) | df['Patient_description'].astype(str).str.contains('LGG', case=False, na=False)

matches = []
for idx, row in df[lgd_mask].iterrows():
    desc = str(row.get('Patient_description', ''))
    m = barcode_re.search(desc)
    if m:
        barcode = m.group(0)
        hist = row.get('histological_type', None)
        matches.append({'ParticipantBarcode': barcode, 'histological_type': hist})

# Also attempt to find by histological_type containing glioma keywords
hist_mask = df['histological_type'].astype(str).str.contains('glioma', case=False, na=False) | df['histological_type'].astype(str).str.contains('astrocytoma', case=False, na=False) | df['histological_type'].astype(str).str.contains('oligodendroglioma', case=False, na=False)
for idx, row in df[hist_mask].iterrows():
    desc = str(row.get('Patient_description', ''))
    m = barcode_re.search(desc)
    if m:
        barcode = m.group(0)
        hist = row.get('histological_type', None)
        # avoid duplicates
        if not any(d['ParticipantBarcode']==barcode for d in matches):
            matches.append({'ParticipantBarcode': barcode, 'histological_type': hist})

# Filter out entries where histological_type contains square brackets or is None/empty or equals 'None'
clean_matches = []
for d in matches:
    hist = d['histological_type']
    if hist is None:
        continue
    hs = str(hist)
    if '[' in hs or ']' in hs:
        continue
    if hs.strip()=='' or hs.strip().upper()=='NONE' or hs.strip().upper()=='NOT APPLICABLE':
        continue
    clean_matches.append(d)

# Prepare output
participant_barcodes = [d['ParticipantBarcode'] for d in clean_matches]
barcode_to_hist = {d['ParticipantBarcode']: d['histological_type'] for d in clean_matches}

out = {'num_lgg_matches_raw': int(lgd_mask.sum()), 'num_matches_after_hist_filter': len(clean_matches), 'participant_barcodes': participant_barcodes, 'barcode_to_hist': barcode_to_hist}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CTiuVYQ0GzbevuBkPuuokkjQ': ['clinical_info'], 'var_call_HmLQhigU0Pu3WEKpxZ5We0HE': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Aqx3og4knI7XgSyuA3gd75Lf': 'file_storage/call_Aqx3og4knI7XgSyuA3gd75Lf.json', 'var_call_qwlEvjfagCOisqlBUmRH2FPF': 'file_storage/call_qwlEvjfagCOisqlBUmRH2FPF.json'}

exec(code, env_args)
