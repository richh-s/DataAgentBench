code = """import json
import re
from collections import defaultdict

# Load clinical data (file path provided in var_call_gTfbAaKkyQYKaUrejq2sPyBh)
with open(var_call_gTfbAaKkyQYKaUrejq2sPyBh, 'r') as f:
    clinical = json.load(f)

# Load mutation data for CDH1
with open(var_call_iSLLMjcFhtpkVHC6hBVVuJCT, 'r') as f:
    mutations = json.load(f)

# Extract participant barcode from Patient_description using regex
barcode_re = re.compile(r"(TCGA[-A-Za-z0-9]+)")

participant_to_hist = {}
for rec in clinical:
    desc = rec.get('Patient_description', '') or ''
    hist = rec.get('histological_type')
    if not desc or not hist:
        continue
    # ensure record mentions Alive and Breast (query was filtered but double-check)
    if 'Alive' not in desc and 'Alive' not in desc.title():
        continue
    if 'Breast' not in desc and 'breast' not in desc:
        continue
    m = barcode_re.search(desc)
    if not m:
        continue
    barcode = m.group(1).strip().strip('.,;)')
    # normalize barcode (uppercase)
    barcode = barcode.upper()
    # keep first histological_type if multiple entries
    if barcode not in participant_to_hist:
        participant_to_hist[barcode] = hist

# Build set of participants with CDH1 mutation (unique)
mutated_participants = set()
for rec in mutations:
    pb = rec.get('ParticipantBarcode')
    if not pb:
        continue
    mutated_participants.add(pb.upper())

# Compute totals and mutated counts per histological_type
totals = defaultdict(int)
mut_counts = defaultdict(int)
for participant, hist in participant_to_hist.items():
    totals[hist] += 1
    if participant in mutated_participants:
        mut_counts[hist] += 1

# Compute percentages
results = []
for hist, total in totals.items():
    mutated = mut_counts.get(hist, 0)
    pct = (mutated / total * 100) if total > 0 else 0.0
    results.append({
        'histological_type': hist,
        'mutated_count': mutated,
        'total_count': total,
        'percentage': round(pct, 2)
    })

# Sort by percentage desc then by total_count desc
results_sorted = sorted(results, key=lambda x: (-x['percentage'], -x['total_count']))

# Take top 3
top3 = results_sorted[:3]

import json
print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_dJyZoS4JpTtjmnp7FftFEx5w': ['clinical_info'], 'var_call_9EWY5V3oh2lMhpsQxfPLEelA': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_d0U0tCwz0OaMoDgT4N86PqFD': 'file_storage/call_d0U0tCwz0OaMoDgT4N86PqFD.json', 'var_call_R0uADQYLWh98AlVBUtafB9i2': [], 'var_call_gTfbAaKkyQYKaUrejq2sPyBh': 'file_storage/call_gTfbAaKkyQYKaUrejq2sPyBh.json', 'var_call_iSLLMjcFhtpkVHC6hBVVuJCT': 'file_storage/call_iSLLMjcFhtpkVHC6hBVVuJCT.json'}

exec(code, env_args)
