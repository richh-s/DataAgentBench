code = """import json
import re

# Load both datasets
clinical_path = locals()['var_functions.query_db:22']
mutation_path = locals()['var_functions.query_db:30']

if isinstance(clinical_path, str) and '.json' in clinical_path:
    with open(clinical_path, 'r') as f:
        brca_clinical = json.load(f)
else:
    brca_clinical = clinical_path

if isinstance(mutation_path, str) and '.json' in mutation_path:
    with open(mutation_path, 'r') as f:
        cdh1_mutations = json.load(f)
else:
    cdh1_mutations = mutation_path

print('Loaded', len(brca_clinical), 'BRCA clinical records')
print('Loaded', len(cdh1_mutations), 'CDH1 mutations')

# Extract participant barcodes from all alive BRCA patients
participant_barcode_to_histology = {}
for rec in brca_clinical:
    if 'Alive' in rec.get('Patient_description', ''):
        desc = rec['Patient_description']
        hist_type = rec.get('histological_type')
        
        # Extract participant barcode
        match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', desc)
        if match:
            barcode = match.group()
            participant_barcode_to_histology[barcode] = hist_type

print('Alive BRCA participants with histology:', len(participant_barcode_to_histology))

# Count total alive patients per histological type
total_per_histology = {}
for hist_type in participant_barcode_to_histology.values():
    total_per_histology[hist_type] = total_per_histology.get(hist_type, 0) + 1

print('Total alive patients per histology:')
sorted_total = sorted(total_per_histology.items(), key=lambda x: x[1], reverse=True)
for hist_type, count in sorted_total:
    print('  ', hist_type + ':', count)

# Identify which participants have CDH1 mutations
mutated_participants = set()
for mut in cdh1_mutations:
    mutated_participants.add(mut['ParticipantBarcode'])

print('Total mutated participants:', len(mutated_participants))

# Count CDH1 mutated patients per histological type
mutated_per_histology = {}
for barcode in mutated_participants:
    hist_type = participant_barcode_to_histology.get(barcode)
    if hist_type:
        mutated_per_histology[hist_type] = mutated_per_histology.get(hist_type, 0) + 1

print('CDH1 mutated patients per histology:')
for hist_type, count in sorted(mutated_per_histology.items(), key=lambda x: x[1], reverse=True):
    print('  ', hist_type + ':', count)

# Calculate percentages
histology_percentages = {}
for hist_type in total_per_histology:
    total = total_per_histology[hist_type]
    mutated = mutated_per_histology.get(hist_type, 0)
    percentage = (mutated / total) * 100 if total > 0 else 0
    histology_percentages[hist_type] = {
        'total': total,
        'mutated': mutated,
        'percentage': round(percentage, 2)
    }

print('\\nMutation percentages by histology:')
sorted_by_percentage = sorted(histology_percentages.items(), key=lambda x: x[1]['percentage'], reverse=True)
for hist_type, data in sorted_by_percentage:
    print(f'  {hist_type}: {data["percentage"]}% ({data["mutated"]}/{data["total"]} patients)')

# Get top 3
top_3 = sorted_by_percentage[:3]
print('\\nTop 3 histological types:')
for i, (hist_type, data) in enumerate(top_3, 1):
    print(f'  {i}. {hist_type}: {data["percentage"]}% ({data["mutated"]}/{data["total"]} patients)')

result = {
    'total_alive': len(participant_barcode_to_histology),
    'histology_analysis': histology_percentages,
    'top_3': top_3
}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'status': 'checked', 'records': 5}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'total_clinical': 50, 'brca_patients': 0, 'alive_brca': 0, 'histology_types': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'total_brca': 116, 'alive_brca': 100, 'histology_distribution': {'Infiltrating Ductal Carcinoma': 72, 'Other  specify': 4, 'Mixed Histology (please specify)': 1, 'Infiltrating Lobular Carcinoma': 19, 'Metaplastic Carcinoma': 2, 'Mucinous Carcinoma': 2}, 'participant_barcodes': ['TCGA-A1-A0SH', 'TCGA-A1-A0SB', 'TCGA-A1-A0SM', 'TCGA-A1-A0SN', 'TCGA-A1-A0SP', 'TCGA-A1-A0SO', 'TCGA-A1-A0SG', 'TCGA-A1-A0SD', 'TCGA-A1-A0SJ', 'TCGA-A1-A0SF', 'TCGA-A1-A0SQ', 'TCGA-A1-A0SE', 'TCGA-A1-A0SI', 'TCGA-A2-A1FZ', 'TCGA-A2-A3XZ', 'TCGA-A2-A04T', 'TCGA-A2-A0CV', 'TCGA-A2-A1FV', 'TCGA-A2-A1G0', 'TCGA-A2-A0YF', 'TCGA-A2-A3XV', 'TCGA-A2-A3XW', 'TCGA-A2-A0T3', 'TCGA-A2-A0YD', 'TCGA-A2-A04U', 'TCGA-A2-A0CX', 'TCGA-A2-A0T4', 'TCGA-A2-A0EN', 'TCGA-A2-A04Q', 'TCGA-A2-A0D4', 'TCGA-A2-A0CZ', 'TCGA-A2-A0EP', 'TCGA-A2-A04R', 'TCGA-A2-A0EV', 'TCGA-A2-A0ES', 'TCGA-A2-A04Y', 'TCGA-A2-A0EQ', 'TCGA-A2-A1FW', 'TCGA-A2-A259', 'TCGA-A2-A0CL', 'TCGA-A2-A25A', 'TCGA-A2-A0ET', 'TCGA-A2-A0T1', 'TCGA-A2-A0CT', 'TCGA-A2-A4RW', 'TCGA-A2-A0YG', 'TCGA-A2-A0YH', 'TCGA-A2-A0EM', 'TCGA-A2-A25B', 'TCGA-A2-A0SU', 'TCGA-A2-A0CY', 'TCGA-A2-A0YI', 'TCGA-A2-A4S1', 'TCGA-A2-A0YE', 'TCGA-A2-A0EX', 'TCGA-A2-A0EU', 'TCGA-A2-A0YJ', 'TCGA-A2-A0ER', 'TCGA-A2-A0T7', 'TCGA-A2-A0T5', 'TCGA-A2-A25D', 'TCGA-A2-A0YM', 'TCGA-A2-A04X', 'TCGA-A2-A4S2', 'TCGA-A2-A0YC', 'TCGA-A2-A0D3', 'TCGA-A2-A0EO', 'TCGA-A2-A4S3', 'TCGA-A2-A0EY', 'TCGA-A2-A0CQ', 'TCGA-A2-A0D1', 'TCGA-A2-A3Y0', 'TCGA-A2-A0CP', 'TCGA-A2-A25F', 'TCGA-A2-A3XT', 'TCGA-A2-A0CR', 'TCGA-A2-A3KD', 'TCGA-A2-A25C', 'TCGA-A2-A0YL', 'TCGA-A2-A0ST', 'TCGA-A2-A3KC', 'TCGA-A2-A25E', 'TCGA-A2-A0T0', 'TCGA-A2-A1G1', 'TCGA-A2-A4S0', 'TCGA-A2-A4RX', 'TCGA-A2-A0SY', 'TCGA-A2-A0CK', 'TCGA-A2-A0YK', 'TCGA-A2-A1G4', 'TCGA-A2-A0D0', 'TCGA-A2-A1FX', 'TCGA-A2-A04W', 'TCGA-A2-A0SX', 'TCGA-A2-A0D2', 'TCGA-A2-A1G6', 'TCGA-A2-A0CW', 'TCGA-A2-A04N', 'TCGA-A2-A4RY', 'TCGA-A2-A0T6']}, 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-A2-A0CR', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0SY', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-A2-A0EX', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A4S2', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0T4', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0CK', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A1FV', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-A2-A1G0', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A1-A0SE', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0T6', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-A2-A25A', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0YD', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}]}

exec(code, env_args)
