code = """import json, re
from collections import defaultdict

clinical_path = var_call_HYBPOAdkq5h3WEGuLZfOFaA4
with open(clinical_path, 'r') as f:
    clinical = json.load(f)

mutated_records = var_call_eCvPahghJnp1ZYupyEquhrq9
mutated_set = set([r['ParticipantBarcode'].upper() for r in mutated_records if r.get('ParticipantBarcode')])

barcode_re = re.compile(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', re.IGNORECASE)

barcode_to_hist = {}
for rec in clinical:
    desc = rec.get('Patient_description','')
    hist = rec.get('histological_type') or 'None'
    m = barcode_re.search(desc)
    if m:
        bc = m.group(1).upper()
        barcode_to_hist[bc] = hist.strip() if isinstance(hist, str) else str(hist)

clinical_barcodes = set(barcode_to_hist.keys())
intersect = sorted(list(clinical_barcodes & mutated_set))

# Counts
totals = defaultdict(int)
mutated_counts = defaultdict(int)
for bc, hist in barcode_to_hist.items():
    totals[hist] += 1
    if bc in mutated_set:
        mutated_counts[hist] += 1

results = []
for hist, tot in totals.items():
    mut = mutated_counts.get(hist, 0)
    pct = (mut / tot * 100) if tot>0 else 0.0
    results.append({'histological_type': hist, 'total_alive_patients': tot, 'mutated_count': mut, 'percent_mutated': round(pct,2)})

results_sorted = sorted(results, key=lambda x: (-x['percent_mutated'], -x['mutated_count'], -x['total_alive_patients']))

output = {
    'clinical_alive_barcodes_count': len(clinical_barcodes),
    'mutated_participants_in_mutation_table_count': len(mutated_set),
    'intersection_count': len(intersect),
    'intersection_samples': intersect[:50],
    'top3_hist_types': results_sorted[:3]
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_6NZecJGlKfKNE0C2ZCTbMaxc': ['clinical_info'], 'var_call_WOGQHy3ZzgFlIJ2KhY8frO7X': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_0dhVjgqydL40Le3AyFjrYV79': 'file_storage/call_0dhVjgqydL40Le3AyFjrYV79.json', 'var_call_Hm8zygVPVDcMxUpWgBL1HpFb': 'file_storage/call_Hm8zygVPVDcMxUpWgBL1HpFb.json', 'var_call_eCvPahghJnp1ZYupyEquhrq9': [{'ParticipantBarcode': 'TCGA-BR-A44T'}, {'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}, {'ParticipantBarcode': 'TCGA-BR-4188'}, {'ParticipantBarcode': 'TCGA-BR-6452'}, {'ParticipantBarcode': 'TCGA-BR-8370'}, {'ParticipantBarcode': 'TCGA-BR-8686'}, {'ParticipantBarcode': 'TCGA-BR-8592'}, {'ParticipantBarcode': 'TCGA-BR-8058'}, {'ParticipantBarcode': 'TCGA-BR-A4QM'}, {'ParticipantBarcode': 'TCGA-BR-4187'}, {'ParticipantBarcode': 'TCGA-BR-6803'}, {'ParticipantBarcode': 'TCGA-BR-6566'}, {'ParticipantBarcode': 'TCGA-BR-4279'}, {'ParticipantBarcode': 'TCGA-BR-8677'}, {'ParticipantBarcode': 'TCGA-BR-A4IV'}, {'ParticipantBarcode': 'TCGA-BR-4292'}], 'var_call_ak0cTQQvVGYXmeRwaXXOozeT': 'file_storage/call_ak0cTQQvVGYXmeRwaXXOozeT.json', 'var_call_9NhF7KdwvHpQ8We4uCIwvjfi': [], 'var_call_o6ToHucNxWDKiC2LXtgmYpKf': [], 'var_call_HYBPOAdkq5h3WEGuLZfOFaA4': 'file_storage/call_HYBPOAdkq5h3WEGuLZfOFaA4.json', 'var_call_RebpnHaoH8dQ2Cv6A4SRfzfI': 'file_storage/call_RebpnHaoH8dQ2Cv6A4SRfzfI.json', 'var_call_1A37uLqOjHxnbK9PdG0OWdLl': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'total_alive_patients': 228, 'mutated_count': 0, 'percent_mutated': 0.0}, {'histological_type': 'None', 'total_alive_patients': 2, 'mutated_count': 0, 'percent_mutated': 0.0}], 'var_call_blR94OpkY2ct75u5p3vqlclJ': {'br_mutated_participants_count': 18, 'sample_barcodes': ['TCGA-BR-4187', 'TCGA-BR-4188', 'TCGA-BR-4279', 'TCGA-BR-4292', 'TCGA-BR-6452', 'TCGA-BR-6566', 'TCGA-BR-6803', 'TCGA-BR-8058', 'TCGA-BR-8364', 'TCGA-BR-8370', 'TCGA-BR-8592', 'TCGA-BR-8677', 'TCGA-BR-8686', 'TCGA-BR-A44T', 'TCGA-BR-A453', 'TCGA-BR-A4IV', 'TCGA-BR-A4J9', 'TCGA-BR-A4QM']}}

exec(code, env_args)
