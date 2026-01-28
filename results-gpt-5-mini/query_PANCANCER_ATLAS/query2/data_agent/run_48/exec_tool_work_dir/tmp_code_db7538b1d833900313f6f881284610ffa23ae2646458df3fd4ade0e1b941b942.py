code = """import json
# Load mutation records for CDH1 (large file path)
mut_path = var_call_Hm8zygVPVDcMxUpWgBL1HpFb
with open(mut_path, 'r') as f:
    mut_records = json.load(f)

# Filter BRCA participant barcodes from mutation records
br_mut = [r for r in mut_records if r.get('ParticipantBarcode','').upper().startswith('TCGA-BR-')]
# Unique participants
br_participants = sorted(list({r['ParticipantBarcode'].upper() for r in br_mut}))

print('__RESULT__:')
print(json.dumps({'br_mutated_participants_count': len(br_participants), 'sample_barcodes': br_participants[:50]}))"""

env_args = {'var_call_6NZecJGlKfKNE0C2ZCTbMaxc': ['clinical_info'], 'var_call_WOGQHy3ZzgFlIJ2KhY8frO7X': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_0dhVjgqydL40Le3AyFjrYV79': 'file_storage/call_0dhVjgqydL40Le3AyFjrYV79.json', 'var_call_Hm8zygVPVDcMxUpWgBL1HpFb': 'file_storage/call_Hm8zygVPVDcMxUpWgBL1HpFb.json', 'var_call_eCvPahghJnp1ZYupyEquhrq9': [{'ParticipantBarcode': 'TCGA-BR-A44T'}, {'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}, {'ParticipantBarcode': 'TCGA-BR-4188'}, {'ParticipantBarcode': 'TCGA-BR-6452'}, {'ParticipantBarcode': 'TCGA-BR-8370'}, {'ParticipantBarcode': 'TCGA-BR-8686'}, {'ParticipantBarcode': 'TCGA-BR-8592'}, {'ParticipantBarcode': 'TCGA-BR-8058'}, {'ParticipantBarcode': 'TCGA-BR-A4QM'}, {'ParticipantBarcode': 'TCGA-BR-4187'}, {'ParticipantBarcode': 'TCGA-BR-6803'}, {'ParticipantBarcode': 'TCGA-BR-6566'}, {'ParticipantBarcode': 'TCGA-BR-4279'}, {'ParticipantBarcode': 'TCGA-BR-8677'}, {'ParticipantBarcode': 'TCGA-BR-A4IV'}, {'ParticipantBarcode': 'TCGA-BR-4292'}], 'var_call_ak0cTQQvVGYXmeRwaXXOozeT': 'file_storage/call_ak0cTQQvVGYXmeRwaXXOozeT.json', 'var_call_9NhF7KdwvHpQ8We4uCIwvjfi': [], 'var_call_o6ToHucNxWDKiC2LXtgmYpKf': [], 'var_call_HYBPOAdkq5h3WEGuLZfOFaA4': 'file_storage/call_HYBPOAdkq5h3WEGuLZfOFaA4.json', 'var_call_RebpnHaoH8dQ2Cv6A4SRfzfI': 'file_storage/call_RebpnHaoH8dQ2Cv6A4SRfzfI.json', 'var_call_1A37uLqOjHxnbK9PdG0OWdLl': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'total_alive_patients': 228, 'mutated_count': 0, 'percent_mutated': 0.0}, {'histological_type': 'None', 'total_alive_patients': 2, 'mutated_count': 0, 'percent_mutated': 0.0}]}

exec(code, env_args)
