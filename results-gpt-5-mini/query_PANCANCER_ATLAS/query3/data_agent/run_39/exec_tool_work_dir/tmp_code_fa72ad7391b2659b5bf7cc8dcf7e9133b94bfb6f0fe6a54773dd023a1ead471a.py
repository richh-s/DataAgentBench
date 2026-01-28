code = """import json
import re

# Load data files from storage variables
with open(var_call_v3yYTUSXSqHq9jWXvBYObKLm, 'r') as f:
    clinical = json.load(f)
with open(var_call_k8rMvs5eqBv8KII9fPmAsXiH, 'r') as f:
    muts = json.load(f)

# Helper to extract patient barcode (first three segments) from Patient_description
barcode_re = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)')

# Build clinical patient dict: barcode -> histological_type
patients = {}
for row in clinical:
    desc = row.get('Patient_description','')
    m = barcode_re.search(desc)
    if not m:
        continue
    bc = m.group(1)
    hist = row.get('histological_type')
    if hist is None:
        continue
    hist_str = str(hist).strip()
    # Exclude unknown/None entries
    if hist_str == '' or hist_str.lower() in ('none','[not applicable]','not applicable'):
        continue
    # Normalize some odd entries
    hist_str = hist_str
    # Keep only first occurrence per patient
    if bc not in patients:
        patients[bc] = hist_str

# Build set of patients with PASS CDH1 mutations (use first three segments)
mutated = set()
for row in muts:
    p = row.get('ParticipantBarcode')
    if not p:
        continue
    parts = p.split('-')
    if len(parts) < 3:
        continue
    pb = '-'.join(parts[:3])
    mutated.add(pb)

# Build contingency counts per histological type
from collections import defaultdict
counts = defaultdict(lambda: [0,0])  # [mut, nonmut]
for bc, hist in patients.items():
    if bc in mutated:
        counts[hist][0] += 1
    else:
        counts[hist][1] += 1

# Remove categories with marginal totals <= 10
filtered_counts = {h: v for h,v in counts.items() if (v[0]+v[1]) > 10}

# If no categories remain, prepare message
if not filtered_counts:
    result = {
        'message': 'No histological categories with total > 10 after filtering; cannot compute chi-square.'
    }
else:
    # Compute grand total and column totals
    grand_total = sum(sum(v) for v in filtered_counts.values())
    col_totals = [sum(v[i] for v in filtered_counts.values()) for i in (0,1)]
    row_totals = {h: sum(v) for h,v in filtered_counts.items()}

    # Compute chi-square
    chi2 = 0.0
    for h, (o_mut, o_non) in filtered_counts.items():
        row_total = o_mut + o_non
        # expected mut
        e_mut = row_total * col_totals[0] / grand_total if grand_total>0 else 0
        e_non = row_total * col_totals[1] / grand_total if grand_total>0 else 0
        # avoid division by zero
        if e_mut>0:
            chi2 += (o_mut - e_mut)**2 / e_mut
        if e_non>0:
            chi2 += (o_non - e_non)**2 / e_non

    result = {
        'chi2': chi2,
        'grand_total': grand_total,
        'col_totals': {'mutated': col_totals[0], 'non_mutated': col_totals[1]},
        'row_totals': row_totals,
        'contingency_table': {h: {'mutated': v[0], 'non_mutated': v[1]} for h,v in filtered_counts.items()},
        'included_histological_types': list(filtered_counts.keys())
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WV8NC3H6uD7NUF8HcqoS4tQi': ['clinical_info'], 'var_call_L9yAKLOwVfvml79oLBOGrJMT': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_dwnhdigl4g24XEv3JWUKRepH': 'file_storage/call_dwnhdigl4g24XEv3JWUKRepH.json', 'var_call_v3yYTUSXSqHq9jWXvBYObKLm': 'file_storage/call_v3yYTUSXSqHq9jWXvBYObKLm.json', 'var_call_k8rMvs5eqBv8KII9fPmAsXiH': 'file_storage/call_k8rMvs5eqBv8KII9fPmAsXiH.json'}

exec(code, env_args)
