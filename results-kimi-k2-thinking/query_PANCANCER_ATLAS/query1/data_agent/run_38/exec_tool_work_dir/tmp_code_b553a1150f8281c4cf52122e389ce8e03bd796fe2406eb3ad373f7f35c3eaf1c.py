code = """import json
import math
import re
from collections import defaultdict, Counter

# Get file paths
lgg_file = locals()['var_functions.query_db:22']
igf2_file = locals()['var_functions.query_db:26']

# Load data
with open(lgg_file, 'r') as f:
    lgg_patients = json.load(f)

with open(igf2_file, 'r') as f:
    igf2_expressions = json.load(f)

# Process LGG patients - extract barcodes and histological types
lgg_participants = []
for patient in lgg_patients:
    patient_desc = patient.get('Patient_description', '')
    hist_type = patient.get('histological_type', '')
    
    # Extract TCGA barcode
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4,5})', patient_desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        # Only include if histological_type is not enclosed in square brackets
        if hist_type and not (hist_type.startswith('[') and hist_type.endswith(']')):
            lgg_participants.append({
                'ParticipantBarcode': barcode,
                'histological_type': hist_type
            })

# Create IGF2 expression map (ParticipantBarcode -> normalized_count)
igf2_map = {}
for expr in igf2_expressions:
    barcode = expr['ParticipantBarcode']
    # Only keep valid expression values (non-empty and non-zero)
    norm_count = expr['normalized_count']
    if norm_count and float(norm_count) > 0:
        igf2_map[barcode] = float(norm_count)

# Merge LGG patients with IGF2 expression
merged_data = []
for lgg in lgg_participants:
    barcode = lgg['ParticipantBarcode']
    if barcode in igf2_map:
        merged_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': lgg['histological_type'],
            'normalized_count': igf2_map[barcode]
        })

# Calculate histology counts and log10-transformed averages
histology_groups = defaultdict(list)
for data in merged_data:
    histology_groups[data['histological_type']].append(data['normalized_count'])

results = {}
for hist_type, counts in histology_groups.items():
    log10_counts = [math.log10(c + 1) for c in counts]  # Add 1 to avoid log10(0)
    avg_log10 = sum(log10_counts) / len(log10_counts) if log10_counts else 0
    results[hist_type] = {
        'count': len(counts),
        'avg_log10_expression': round(avg_log10, 4)
    }

# Prepare output
output = {
    'total_lgg_patients': len(lgg_participants),
    'patients_with_igf2': len(merged_data),
    'histology_breakdown': dict(Counter([p['histological_type'] for p in lgg_participants])),
    'averages_by_histology': results
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ZNF770', 'Entrez': '54989', 'normalized_count': '1195.92'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'AMELY', 'Entrez': '266', 'normalized_count': '0.0'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'TPTE2P1', 'Entrez': '646405', 'normalized_count': '214.576'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ITGB3', 'Entrez': '3690', 'normalized_count': '13.6303'}], 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
