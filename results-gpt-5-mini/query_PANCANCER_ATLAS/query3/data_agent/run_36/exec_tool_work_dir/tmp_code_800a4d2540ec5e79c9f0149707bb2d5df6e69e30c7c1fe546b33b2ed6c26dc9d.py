code = """import json, re
import pandas as pd

clinical_path = var_call_SZWtI8VXZWrjWsr94fvHxDva
mut_path = var_call_7FWy9AkScfQSBbOSiTSaGCcS

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(mut_path, 'r') as f:
    muts = json.load(f)

# regex to capture TCGA barcodes like TCGA-XX-XXXX or longer
barcode_re = re.compile(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{3,6})')

# build patient -> histological_type map from clinical
patient_hist = {}
for r in clinical:
    desc = r.get('Patient_description', '')
    m = barcode_re.search(desc)
    if not m:
        continue
    barcode = m.group(1)
    hist = r.get('histological_type')
    if hist is None:
        continue
    hist_norm = hist.strip()
    if hist_norm == '' or hist_norm.upper().startswith('[NOT'):
        continue
    # keep first observed
    if barcode not in patient_hist:
        patient_hist[barcode] = hist_norm

# build set of mutated participants from mutation data (FILTER='PASS' already in query result)
mutated_participants = set()
for r in muts:
    pb = r.get('ParticipantBarcode')
    if not pb:
        continue
    m = barcode_re.search(pb)
    if m:
        mutated_participants.add(m.group(1))
    else:
        mutated_participants.add(pb)

# Build counts per hist type
from collections import defaultdict
counts = defaultdict(lambda: {'mutated': 0, 'not_mutated': 0})
for barcode, hist in patient_hist.items():
    is_mut = barcode in mutated_participants
    if is_mut:
        counts[hist]['mutated'] += 1
    else:
        counts[hist]['not_mutated'] += 1

# Compute row totals and separate included/excluded
included = {}
excluded = []
for hist, vals in counts.items():
    row_total = vals['mutated'] + vals['not_mutated']
    if row_total > 10:
        included[hist] = {'mutated': vals['mutated'], 'not_mutated': vals['not_mutated'], 'row_total': row_total}
    else:
        excluded.append({'histological_type': hist, 'mutated': vals['mutated'], 'not_mutated': vals['not_mutated'], 'row_total': row_total})

# Compute chi-square
grand_total = sum(v['row_total'] for v in included.values())
mutated_total = sum(v['mutated'] for v in included.values())
not_mutated_total = sum(v['not_mutated'] for v in included.values())
chi2 = None
if grand_total == 0:
    chi2 = None
else:
    chi2_val = 0.0
    for hist, v in included.items():
        row_total = v['row_total']
        obs_mut = v['mutated']
        obs_not = v['not_mutated']
        exp_mut = (row_total * mutated_total) / grand_total
        exp_not = (row_total * not_mutated_total) / grand_total
        if exp_mut > 0:
            chi2_val += (obs_mut - exp_mut) ** 2 / exp_mut
        if exp_not > 0:
            chi2_val += (obs_not - exp_not) ** 2 / exp_not
    chi2 = round(chi2_val, 6)

result = {
    'chi2': chi2,
    'grand_total': int(grand_total),
    'mutated_total': int(mutated_total),
    'not_mutated_total': int(not_mutated_total),
    'included_histological_types_count': len(included),
    'included_contingency': included,
    'excluded_histological_types': excluded
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_J8cq91Qkykr7BmOMwRiN41M3': ['clinical_info'], 'var_call_ieTXnMdiVrVRJFhMg9brgKK2': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_TCYUIakYKMmCmy1cTDzmJsFS': 'file_storage/call_TCYUIakYKMmCmy1cTDzmJsFS.json', 'var_call_Ofi87woW9fv2wFDGgz6Tk0LF': [], 'var_call_SZWtI8VXZWrjWsr94fvHxDva': 'file_storage/call_SZWtI8VXZWrjWsr94fvHxDva.json', 'var_call_7FWy9AkScfQSBbOSiTSaGCcS': 'file_storage/call_7FWy9AkScfQSBbOSiTSaGCcS.json', 'var_call_2sFJDui22QqUcyZrgjq4IIiU': {'clinical_records_processed': 500, 'patient_hist_count': 500, 'mutated_participants_count': 247, 'df_rows': 500, 'unique_hist_top20': [['Infiltrating Ductal Carcinoma', 331], ['Infiltrating Lobular Carcinoma', 117], ['Other  specify', 28], ['Mucinous Carcinoma', 10], ['Metaplastic Carcinoma', 6], ['Mixed Histology (please specify)', 4], ['Medullary Carcinoma', 2], ['Infiltrating Carcinoma NOS', 1], ['Leiomyosarcoma (LMS)', 1]], 'df_sample': [{'barcode': 'TCGA-AC-A5EH', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}, {'barcode': 'TCGA-LL-A7SZ', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}, {'barcode': 'TCGA-AN-A0FY', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}, {'barcode': 'TCGA-AC-A2FB', 'histological_type': 'Infiltrating Lobular Carcinoma', 'mutated': True}, {'barcode': 'TCGA-AO-A1KR', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}, {'barcode': 'TCGA-GM-A2DA', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}, {'barcode': 'TCGA-3C-AAAU', 'histological_type': 'Infiltrating Lobular Carcinoma', 'mutated': False}, {'barcode': 'TCGA-A7-A26I', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}, {'barcode': 'TCGA-A7-A5ZW', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}, {'barcode': 'TCGA-C8-A26Z', 'histological_type': 'Infiltrating Ductal Carcinoma', 'mutated': False}]}}

exec(code, env_args)
