code = """import json, re
from collections import defaultdict

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

clinical = load_var(var_call_OQ3HbKsJRnv31f0uwl66djac)
mutations = load_var(var_call_ZGG0MwDRFnXYXaitEFiSrmmP)
# var_call_qXH9... is small list
brca_mut_participants = var_call_qXH9l3Li7Cc3J8jATg6GtWEn

# build mutation set
mut_set = set()
for r in mutations:
    b = r.get('ParticipantBarcode') or r.get('participantbarcode')
    if b:
        mut_set.add(b)

# extract patient barcode and histological_type from clinical records
patients = {}
for rec in clinical:
    pd = rec.get('Patient_description','')
    hist = rec.get('histological_type')
    m = re.search(r'(TCGA-[A-Za-z0-9-]+)', pd)
    if m:
        barcode = m.group(1)
        # prefer existing hist if present, else set
        if barcode not in patients:
            patients[barcode] = hist if hist is not None else 'Unknown'

# aggregate counts per histological_type
hist_total = defaultdict(int)
hist_mut = defaultdict(int)
for barcode, hist in patients.items():
    hist_total[hist] += 1
    if barcode in mut_set:
        hist_mut[hist] += 1

rows = []
for h, total in hist_total.items():
    mutated = hist_mut.get(h, 0)
    pct = round((mutated * 100.0 / total), 2) if total > 0 else 0.0
    rows.append({
        'histological_type': h,
        'total_alive_patients': total,
        'mutated_patients': mutated,
        'percent_mutated': pct
    })

rows_sorted = sorted(rows, key=lambda x: x['percent_mutated'], reverse=True)
top3 = rows_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_vKO4Bztp8jHnPQviEZRrc9XR': ['clinical_info'], 'var_call_1FjVSkr2uFnNA0gU4KrNDdIj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_1gCSDpdQfHDvOefy90yowvNV': 'file_storage/call_1gCSDpdQfHDvOefy90yowvNV.json', 'var_call_p9SS3EE5zOXb0vgzAVsjt52m': 'file_storage/call_p9SS3EE5zOXb0vgzAVsjt52m.json', 'var_call_ZGG0MwDRFnXYXaitEFiSrmmP': 'file_storage/call_ZGG0MwDRFnXYXaitEFiSrmmP.json', 'var_call_Tqcqw8r3OLCcz7A5MVToASXx': [], 'var_call_qXH9l3Li7Cc3J8jATg6GtWEn': [{'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-BR-A44T'}, {'ParticipantBarcode': 'TCGA-BR-6803'}, {'ParticipantBarcode': 'TCGA-BR-4188'}, {'ParticipantBarcode': 'TCGA-BR-8370'}, {'ParticipantBarcode': 'TCGA-BR-8686'}, {'ParticipantBarcode': 'TCGA-BR-6452'}, {'ParticipantBarcode': 'TCGA-BR-8058'}, {'ParticipantBarcode': 'TCGA-BR-A4QM'}, {'ParticipantBarcode': 'TCGA-BR-8592'}, {'ParticipantBarcode': 'TCGA-BR-4187'}, {'ParticipantBarcode': 'TCGA-BR-6566'}, {'ParticipantBarcode': 'TCGA-BR-4279'}, {'ParticipantBarcode': 'TCGA-BR-8677'}, {'ParticipantBarcode': 'TCGA-BR-A4IV'}, {'ParticipantBarcode': 'TCGA-BR-4292'}], 'var_call_OQ3HbKsJRnv31f0uwl66djac': 'file_storage/call_OQ3HbKsJRnv31f0uwl66djac.json'}

exec(code, env_args)
