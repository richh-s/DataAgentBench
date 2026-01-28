code = """import json, re

# Load BRCA alive clinical records from large JSON file path provided by query
clinical_path = var_call_HYBPOAdkq5h3WEGuLZfOFaA4
with open(clinical_path, 'r') as f:
    clinical = json.load(f)

# Load mutated participant barcodes (CDH1 in BR participants)
mutated_records = var_call_eCvPahghJnp1ZYupyEquhrq9
mutated_set = set([r['ParticipantBarcode'].upper() for r in mutated_records if r.get('ParticipantBarcode')])

# Regex to extract TCGA barcode
barcode_re = re.compile(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', re.IGNORECASE)

# Build mapping barcode -> histological_type for BRCA (Bladder) alive patients
barcode_to_hist = {}
for rec in clinical:
    desc = rec.get('Patient_description','')
    hist = rec.get('histological_type') or 'None'
    # Ensure these clinical records are Bladder urothelial carcinoma cohort
    # The original query filtered by Patient_description ILIKE '%Bladder%' so assume all are Bladder
    m = barcode_re.search(desc)
    if m:
        bc = m.group(1).upper()
        # Normalize histological type string
        hist_norm = hist.strip() if isinstance(hist, str) else str(hist)
        barcode_to_hist[bc] = hist_norm

# Aggregate totals and mutated counts by histological_type
from collections import defaultdict

totals = defaultdict(int)
mutated_counts = defaultdict(int)

for bc, hist in barcode_to_hist.items():
    totals[hist] += 1
    if bc in mutated_set:
        mutated_counts[hist] += 1

# Build list of hist types with percentages
results = []
for hist, tot in totals.items():
    mut = mutated_counts.get(hist, 0)
    pct = (mut / tot * 100) if tot>0 else 0.0
    results.append({'histological_type': hist, 'total_alive_patients': tot, 'mutated_count': mut, 'percent_mutated': round(pct,2)})

# Sort by percent_mutated desc, then mutated_count desc, then total_alive_patients desc
results_sorted = sorted(results, key=lambda x: (-x['percent_mutated'], -x['mutated_count'], -x['total_alive_patients']))

top3 = results_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_6NZecJGlKfKNE0C2ZCTbMaxc': ['clinical_info'], 'var_call_WOGQHy3ZzgFlIJ2KhY8frO7X': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_0dhVjgqydL40Le3AyFjrYV79': 'file_storage/call_0dhVjgqydL40Le3AyFjrYV79.json', 'var_call_Hm8zygVPVDcMxUpWgBL1HpFb': 'file_storage/call_Hm8zygVPVDcMxUpWgBL1HpFb.json', 'var_call_eCvPahghJnp1ZYupyEquhrq9': [{'ParticipantBarcode': 'TCGA-BR-A44T'}, {'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}, {'ParticipantBarcode': 'TCGA-BR-4188'}, {'ParticipantBarcode': 'TCGA-BR-6452'}, {'ParticipantBarcode': 'TCGA-BR-8370'}, {'ParticipantBarcode': 'TCGA-BR-8686'}, {'ParticipantBarcode': 'TCGA-BR-8592'}, {'ParticipantBarcode': 'TCGA-BR-8058'}, {'ParticipantBarcode': 'TCGA-BR-A4QM'}, {'ParticipantBarcode': 'TCGA-BR-4187'}, {'ParticipantBarcode': 'TCGA-BR-6803'}, {'ParticipantBarcode': 'TCGA-BR-6566'}, {'ParticipantBarcode': 'TCGA-BR-4279'}, {'ParticipantBarcode': 'TCGA-BR-8677'}, {'ParticipantBarcode': 'TCGA-BR-A4IV'}, {'ParticipantBarcode': 'TCGA-BR-4292'}], 'var_call_ak0cTQQvVGYXmeRwaXXOozeT': 'file_storage/call_ak0cTQQvVGYXmeRwaXXOozeT.json', 'var_call_9NhF7KdwvHpQ8We4uCIwvjfi': [], 'var_call_o6ToHucNxWDKiC2LXtgmYpKf': [], 'var_call_HYBPOAdkq5h3WEGuLZfOFaA4': 'file_storage/call_HYBPOAdkq5h3WEGuLZfOFaA4.json', 'var_call_RebpnHaoH8dQ2Cv6A4SRfzfI': 'file_storage/call_RebpnHaoH8dQ2Cv6A4SRfzfI.json'}

exec(code, env_args)
