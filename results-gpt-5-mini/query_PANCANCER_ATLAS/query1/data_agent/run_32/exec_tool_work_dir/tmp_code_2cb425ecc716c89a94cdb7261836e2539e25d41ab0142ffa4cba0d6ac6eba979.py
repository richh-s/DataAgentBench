code = """import pandas as pd
import json
import re
import math

# Load the previous tool results from storage variables
# var_call_ucDr0kzK4Vgxpd4TqhKHxYpg : clinical LGG query result (list of dicts) stored as file path or list
# var_call_eIsXo9y1td6Nfwh3UGqbp43M : RNASeq IGF2 query result

clinical_records = var_call_ucDr0kzK4Vgxpd4TqhKHxYpg
rna_records = var_call_eIsXo9y1td6Nfwh3UGqbp43M

# Ensure they are loaded as lists of dicts (if file paths, read them)
if isinstance(clinical_records, str):
    clinical_records = pd.read_json(clinical_records).to_dict(orient='records')
if isinstance(rna_records, str):
    rna_records = pd.read_json(rna_records).to_dict(orient='records')

clf = pd.DataFrame(clinical_records)
rna = pd.DataFrame(rna_records)

# Extract TCGA barcode from Patient_description using regex
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"TCGA-[A-Za-z0-9-]+", text)
    if m:
        return m.group(0)
    return None

clf['ParticipantBarcode'] = clf['Patient_description'].apply(extract_barcode)

# Filter out records without barcode or without histological_type or histological_type enclosed in square brackets
clf = clf[clf['ParticipantBarcode'].notna()]
clf = clf[clf['histological_type'].notna()]
# Exclude histologies that contain '[' or ']' (enclosed in square brackets)
clf = clf[~clf['histological_type'].str.contains(r"\[|\]", regex=True)]

# Prepare RNA data: ensure ParticipantBarcode present and normalized_count numeric
rna = rna[rna['ParticipantBarcode'].notna()]
# Convert normalized_count to numeric, coerce errors to NaN
rna['normalized_count'] = pd.to_numeric(rna['normalized_count'], errors='coerce')
# Keep only valid numeric normalized_count
rna = rna[rna['normalized_count'].notna()]

# Some participants may have multiple samples; average normalized_count per participant
rna_patient_avg = rna.groupby('ParticipantBarcode', dropna=False)['normalized_count'].mean().reset_index()

# Join clinical LGG patients to RNA
merged = pd.merge(clf[['ParticipantBarcode','histological_type']], rna_patient_avg, on='ParticipantBarcode', how='inner')

# Now compute log10(normalized_count + 1) per patient
merged['log10_igf2'] = merged['normalized_count'].apply(lambda x: math.log10(x + 1))

# Compute average log10 per histological_type
result = merged.groupby('histological_type', dropna=False)['log10_igf2'].mean().reset_index()

# Format results with at least four decimal places
output = {}
for _, row in result.iterrows():
    hist = row['histological_type']
    val = row['log10_igf2']
    # Format to 4 decimal places (but keep more if necessary) — use 4 decimal places exactly
    output[hist] = float(f"{val:.4f}")

# Print result in required format
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_RkeIi6upaYNv4fICv5Jd54UU': ['clinical_info'], 'var_call_K2TXHbsLXs4VylDejjJmBCIV': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_pa1ELmP4cW3gv0fN1pSTqKHK': 'file_storage/call_pa1ELmP4cW3gv0fN1pSTqKHK.json', 'var_call_oV7GkxO4F7Zu1KuYgwBuhBVQ': [{'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Trunk|Extremities'}, {'tumor_tissue_site': 'Superficial Trunk - Flank'}, {'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Peritoneum ovary'}, {'tumor_tissue_site': 'Stomach'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_tissue_site': 'Prostate'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Adrenal gland'}, {'tumor_tissue_site': 'Bile duct'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Superficial Trunk - Buttock'}, {'tumor_tissue_site': 'Adrenal'}, {'tumor_tissue_site': 'Bladder'}, {'tumor_tissue_site': 'Thymus'}, {'tumor_tissue_site': '[Unknown]'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_tissue_site': 'Superficial Trunk - Abdominal wall'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal'}, {'tumor_tissue_site': 'Superficial Trunk - Back'}, {'tumor_tissue_site': 'Chest - Chest wall'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Rectum'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_tissue_site': 'Esophagus'}, {'tumor_tissue_site': 'Omentum'}, {'tumor_tissue_site': 'Chest - Other (please specify'}], 'var_call_eIsXo9y1td6Nfwh3UGqbp43M': 'file_storage/call_eIsXo9y1td6Nfwh3UGqbp43M.json', 'var_call_ZjxnV2kXPzG0hMZZuuXloGuW': 'file_storage/call_ZjxnV2kXPzG0hMZZuuXloGuW.json', 'var_call_TeGkZa3RpS9FHooudI2XK1b8': [{'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Treated primary GBM'}, {'histological_type': 'Untreated primary (de novo) GBM'}], 'var_call_zTF4jVEVuSOtBnyqj7jI0ZyY': [], 'var_call_nTIiSkcXAkoJFBYjztGjIu7Q': [], 'var_call_ucDr0kzK4Vgxpd4TqhKHxYpg': 'file_storage/call_ucDr0kzK4Vgxpd4TqhKHxYpg.json'}

exec(code, env_args)
