code = """import json, re

# Load data
with open('/mnt/data/var_functions.query_db:52.json', 'r') as f:
    clinical_data = json.load(f)

with open('/mnt/data/var_functions.query_db:40.json', 'r') as f:
    cdh1_mutations = json.load(f)

print('Data loaded successfully')
print('Clinical records:', len(clinical_data))
print('CDH1 mutations:', len(cdh1_mutations))

# Extract female bladder cancer patients
patient_hist = {}
bladder_patients = []

for rec in clinical_data:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', '')
    
    if 'FEMALE' in desc:
        m = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
        if m:
            bc = m.group(0)
            patient_hist[bc] = hist
            if 'bladder' in desc.lower() or 'BRCA' in desc or 'urothelial' in desc.lower():
                bladder_patients.append(bc)

print('Female bladder patients:', len(bladder_patients))

# Get CDH1 mutated patients
cdh1_set = set(m['ParticipantBarcode'] for m in cdh1_mutations)
print('CDH1 mutated patients:', len(cdh1_set))

# Build contingency table
contingency = {}
for bc in bladder_patients:
    hist = patient_hist.get(bc, '')
    if not hist: continue
    
    has_mut = bc in cdh1_set
    if hist not in contingency:
        contingency[hist] = [0, 0]  # [CDH1_mutation, CDH1_wildtype]
    
    if has_mut:
        contingency[hist][0] += 1
    else:
        contingency[hist][1] += 1

print('Histological types:', len(contingency))

# Filter by marginal totals > 10
filtered = {}
for h, counts in contingency.items():
    total = counts[0] + counts[1]
    if total > 10:
        filtered[h] = {'CDH1_mutated': counts[0], 'CDH1_wildtype': counts[1]}
        print(h, 'total:', total, 'mut:', counts[0], 'wt:', counts[1])

print('Filtered types:', len(filtered))
result = {'bladder_patients': len(bladder_patients), 'contingency': filtered}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
