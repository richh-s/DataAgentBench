code = """import json
import pandas as pd

# Load BRCA patients from clinical data
file_path = var_functions.query_db:14
with open(file_path, 'r') as f:
    brca_patients = json.load(f)

# Filter for alive BRCA patients
alive_brca_patients = []
for patient in brca_patients:
    if 'Alive' in patient['Patient_description']:
        alive_brca_patients.append(patient)

# Extract patient information
patient_data = []
for patient in alive_brca_patients:
    patient_data.append({
        'ParticipantBarcode': patient['Patient_description'].split('TCGA-')[1].split()[0] if 'TCGA-' in patient['Patient_description'] else '',
        'histological_type': patient.get('histological_type', 'Unknown'),
        'vital_status': 'Alive'
    })

print('__RESULT__:')
print(json.dumps(f'Total BRCA patients: {len(brca_patients)}, Alive BRCA patients: {len(alive_brca_patients)}'))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'OBSCN', 'HGVSp_Short': 'p.V2237A', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.6710T>C', 'CENTERS': 'RADIA|MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'RIMS2', 'HGVSp_Short': 'p.S511L', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1532C>T', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'TMEM53', 'HGVSp_Short': 'p.R87H', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.260G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Tumor_SampleBarcode': 'TCGA-04-1331-01A', 'Tumor_AliquotBarcode': 'TCGA-04-1331-01A-01W-0486-08', 'Normal_SampleBarcode': 'TCGA-04-1331-10A', 'Normal_AliquotBarcode': 'TCGA-04-1331-10A-01W-0486-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CCDC102A', 'HGVSp_Short': 'p.T245K', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.734C>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-04-1331', 'Tumor_SampleBarcode': 'TCGA-04-1331-01A', 'Tumor_AliquotBarcode': 'TCGA-04-1331-01A-01W-0486-08', 'Normal_SampleBarcode': 'TCGA-04-1331-10A', 'Normal_AliquotBarcode': 'TCGA-04-1331-10A-01W-0486-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'WNT7A', 'HGVSp_Short': 'p.E171D', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.513G>T', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
