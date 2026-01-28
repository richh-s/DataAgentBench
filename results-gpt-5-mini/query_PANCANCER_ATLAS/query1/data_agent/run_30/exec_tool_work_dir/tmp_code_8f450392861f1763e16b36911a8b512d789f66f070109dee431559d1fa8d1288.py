code = """import json
p = var_call_VFhJzWuehfS8BcnXSZQXNHuN
with open(p, 'r') as f:
    expr = json.load(f)
# convert normalized_count to float and simplify barcodes to patient-level (first 12 chars?)
# ParticipantBarcode are like TCGA-XX-YYYY
for r in expr[:5]:
    pass
# load clinical patient mapping: patient_id values are short; but Patient_description contains TCGA-XX-YYYY
pcl = var_call_AxW0rcKU4vamEA59dXBS83AU
with open(pcl, 'r') as f:
    clinical = json.load(f)
# Build mapping from barcode like TCGA-xx-xxxx present in Patient_description to histological_type
import re
barcode_to_hist = {}
for r in clinical:
    pd = r.get('Patient_description','')
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,5})', pd)
    if m:
        barcode = m.group(1)
        hist = r.get('histological_type')
        barcode_to_hist[barcode] = hist
len(barcode_to_hist)
# Now match expression entries where ParticipantBarcode's prefix matches any barcode in mapping
matched = []
for r in expr:
    pb = r.get('ParticipantBarcode')
    # reduce pb to first 12 chars like TCGA-XX-YYYY
    m = re.match(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,5})', pb)
    if m:
        short = m.group(1)
        if short in barcode_to_hist:
            try:
                nc = float(r.get('normalized_count'))
            except:
                continue
            matched.append({'ParticipantBarcode': short, 'normalized_count': nc, 'histological_type': barcode_to_hist[short]})
# summarize counts and sample matched
import statistics
from collections import defaultdict
groups = defaultdict(list)
for m in matched:
    groups[m['histological_type']].append(m['normalized_count'])
summary = {k: {'n': len(v), 'mean_raw': (statistics.mean(v) if v else None)} for k,v in groups.items()}
res = {'mapped_samples': len(matched), 'unique_histologies': len(groups), 'summary_example': dict(list(summary.items())[:20])}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_712rnEX72Xwagvg93fcaojTw': ['clinical_info'], 'var_call_CdTCNUezwXjwKCtVVMmPXEXH': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_4ciXcjLXQEDt4Wv6O50QBdNc': 'file_storage/call_4ciXcjLXQEDt4Wv6O50QBdNc.json', 'var_call_HN6iYcBZ1lrDx1Bkc4xxvXtW': {'matched_count': 0, 'unique_histological_type_sample': [], 'sample_matches': []}, 'var_call_AxW0rcKU4vamEA59dXBS83AU': 'file_storage/call_AxW0rcKU4vamEA59dXBS83AU.json', 'var_call_VFhJzWuehfS8BcnXSZQXNHuN': 'file_storage/call_VFhJzWuehfS8BcnXSZQXNHuN.json'}

exec(code, env_args)
