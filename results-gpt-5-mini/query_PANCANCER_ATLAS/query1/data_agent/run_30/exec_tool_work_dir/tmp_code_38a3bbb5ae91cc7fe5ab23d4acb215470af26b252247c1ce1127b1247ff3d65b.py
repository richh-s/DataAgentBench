code = """import json
p = var_call_ElzSMHsH9PqF05k2tTJvhskS
with open(p, 'r') as f:
    blgg = json.load(f)
# build mapping from ParticipantBarcode (TCGA-XX-XXXX) to histological_type for LGG cohort
import re
barcode_to_hist_lgg = {}
for r in blgg:
    pd = r.get('Patient_description','')
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,5})', pd)
    if m:
        barcode = m.group(1)
        hist = r.get('histological_type')
        # Exclude histology values enclosed in square brackets
        if isinstance(hist, str) and hist.startswith('[') and hist.endswith(']'):
            continue
        barcode_to_hist_lgg[barcode] = hist
# Now load IGF2 expression file path
expr_p = var_call_VFhJzWuehfS8BcnXSZQXNHuN
with open(expr_p, 'r') as f:
    expr = json.load(f)
# match expressions for those barcodes
matches = []
for r in expr:
    pb = r.get('ParticipantBarcode','')
    m = re.match(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,5})', pb)
    if m:
        short = m.group(1)
        if short in barcode_to_hist_lgg:
            try:
                nc = float(r.get('normalized_count'))
            except:
                continue
            hist = barcode_to_hist_lgg[short]
            matches.append({'ParticipantBarcode': short, 'normalized_count': nc, 'histological_type': hist})
# compute log10(normalized_count+1) and average per histology
import math
from collections import defaultdict
vals = defaultdict(list)
for m in matches:
    nc = m['normalized_count']
    # only include valid expression values (non-null, numeric)
    if nc is None:
        continue
    try:
        lg = math.log10(nc+1)
    except:
        continue
    if m['histological_type'] is None:
        continue
    # exclude histology annotations enclosed in square brackets
    h = m['histological_type']
    if isinstance(h, str) and h.startswith('[') and h.endswith(']'):
        continue
    vals[h].append(lg)
# compute means with at least 4 decimal places
result = {}
for h,v in vals.items():
    if v:
        meanv = sum(v)/len(v)
        result[h] = round(meanv, 6)
print('__RESULT__:')
print(json.dumps({'n_samples_matched': len(matches), 'n_lgg_barcodes': len(barcode_to_hist_lgg), 'per_histology_log10_mean': result}))"""

env_args = {'var_call_712rnEX72Xwagvg93fcaojTw': ['clinical_info'], 'var_call_CdTCNUezwXjwKCtVVMmPXEXH': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_4ciXcjLXQEDt4Wv6O50QBdNc': 'file_storage/call_4ciXcjLXQEDt4Wv6O50QBdNc.json', 'var_call_HN6iYcBZ1lrDx1Bkc4xxvXtW': {'matched_count': 0, 'unique_histological_type_sample': [], 'sample_matches': []}, 'var_call_AxW0rcKU4vamEA59dXBS83AU': 'file_storage/call_AxW0rcKU4vamEA59dXBS83AU.json', 'var_call_VFhJzWuehfS8BcnXSZQXNHuN': 'file_storage/call_VFhJzWuehfS8BcnXSZQXNHuN.json', 'var_call_FDhZ9OE0f7wBKYrXB00trrqM': {'mapped_samples': 16, 'unique_histologies': 4, 'summary_example': {'Untreated primary (de novo) GBM': {'n': 4, 'mean_raw': 580.2872500000001}, 'Oligoastrocytoma': {'n': 2, 'mean_raw': 813.024}, 'Oligodendroglioma': {'n': 6, 'mean_raw': 553.0595}, 'Astrocytoma': {'n': 4, 'mean_raw': 494.43375000000003}}}, 'var_call_ElzSMHsH9PqF05k2tTJvhskS': 'file_storage/call_ElzSMHsH9PqF05k2tTJvhskS.json'}

exec(code, env_args)
