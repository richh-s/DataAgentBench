code = """import json
import pandas as pd

# Load the clinical query result (stored as a JSON file path)
with open(var_call_GwO4VQomzNOIjtghenejj1Mv, 'r') as f:
    clinical = json.load(f)

# Load the mutation query result (stored as a JSON file path)
with open(var_call_sJJ2BFJHIZ0KK1NRcR3N4EX4, 'r') as f:
    mutations = json.load(f)

# Create DataFrames
clinical_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Ensure consistent column names
clinical_df.columns = [c.lower() for c in clinical_df.columns]
# clinical has 'participantbarcode' and 'histological_type'

# Get unique set of participant barcodes with CDH1 mutation
mut_participants = set(mut_df['ParticipantBarcode'].astype(str).str.strip().unique())

# For clinical, compute totals per histological_type and mutated counts
# Filter out rows missing histological_type or participantbarcode
clinical_df = clinical_df[clinical_df['participantbarcode'].notna()]
clinical_df['participantbarcode'] = clinical_df['participantbarcode'].astype(str).str.strip()
clinical_df = clinical_df[clinical_df['histological_type'].notna()]

# Group
grouped = clinical_df.groupby('histological_type').agg(total_patients=('participantbarcode', 'nunique'))

# Compute mutated counts per hist type
def count_mutated(part_bar_series):
    # count unique participants in this series that are in mut_participants
    unique = set(part_bar_series.astype(str).str.strip().unique())
    return len(unique & mut_participants)

mut_counts = clinical_df.groupby('histological_type')['participantbarcode'].apply(count_mutated).rename('mutated_patients')

result_df = grouped.join(mut_counts).fillna(0)
result_df['mutated_patients'] = result_df['mutated_patients'].astype(int)
result_df['percent_mutated'] = (result_df['mutated_patients'] / result_df['total_patients'] * 100).round(4)

# Filter to hist types with at least 1 patient
result_df = result_df[result_df['total_patients']>0]

# Sort and get top 3 by percent_mutated, tie-breaker by mutated_patients then total_patients
result_df = result_df.sort_values(['percent_mutated','mutated_patients','total_patients'], ascending=[False, False, False])

top3 = result_df.head(3).reset_index()

# Prepare output
output = []
for _, row in top3.iterrows():
    output.append({
        'histological_type': row['histological_type'],
        'total_patients': int(row['total_patients']),
        'mutated_patients': int(row['mutated_patients']),
        'percent_mutated': float(row['percent_mutated'])
    })

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_tjKLCzaf6xWMpAljuchbbfMJ': ['clinical_info'], 'var_call_IK0YViIDx1rdklE0m2mXsyPD': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_vC9b2PkpPDtWgcQ7cTChSOvc': 'file_storage/call_vC9b2PkpPDtWgcQ7cTChSOvc.json', 'var_call_Qvqmev67zbAG17yu86MXvqt1': [{'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Trunk|Extremities'}, {'tumor_tissue_site': 'Superficial Trunk - Flank'}, {'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Peritoneum ovary'}, {'tumor_tissue_site': 'Stomach'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_tissue_site': 'Prostate'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Adrenal gland'}, {'tumor_tissue_site': 'Bile duct'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Superficial Trunk - Buttock'}, {'tumor_tissue_site': 'Adrenal'}, {'tumor_tissue_site': 'Bladder'}, {'tumor_tissue_site': 'Thymus'}, {'tumor_tissue_site': '[Unknown]'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_tissue_site': 'Superficial Trunk - Abdominal wall'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal'}, {'tumor_tissue_site': 'Superficial Trunk - Back'}, {'tumor_tissue_site': 'Chest - Chest wall'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Rectum'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_tissue_site': 'Esophagus'}, {'tumor_tissue_site': 'Omentum'}, {'tumor_tissue_site': 'Chest - Other (please specify'}], 'var_call_5ao25kCjyBdC3YHj6mk1PBLH': 'file_storage/call_5ao25kCjyBdC3YHj6mk1PBLH.json', 'var_call_bMBpErLB3WntnrCTLh2xi3wd': 'file_storage/call_bMBpErLB3WntnrCTLh2xi3wd.json', 'var_call_sJJ2BFJHIZ0KK1NRcR3N4EX4': 'file_storage/call_sJJ2BFJHIZ0KK1NRcR3N4EX4.json', 'var_call_GwO4VQomzNOIjtghenejj1Mv': 'file_storage/call_GwO4VQomzNOIjtghenejj1Mv.json'}

exec(code, env_args)
