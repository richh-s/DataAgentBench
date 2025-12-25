code = """import json, re, math, pandas as pd

# Load full RNASeq IGF2 data
with open(var_call_UiLcwcUisOZ9sWIdDmElY7fe, 'r') as f:
    igf2_records = json.load(f)

# Convert to DataFrame
rna_df = pd.DataFrame(igf2_records)

# Extract patient barcode from Patient_description for LGG clinical entries
with open(var_call_jsVezBrewkdVlPdVZepz9vx7, 'r') as f:
    lgg_records = json.load(f)

clin_df = pd.DataFrame(lgg_records)

# Function to parse barcode and histology text from Patient_description
# Examples: "Case ..., linked to barcode TCGA-RY-A83X, corresponds ... Brain lower grade glioma"
#           "Patient TCGA-DB-A4XH (UUID ... ) is a ... diagnosed with Brain lower grade glioma."

def extract_barcode(desc: str):
    m = re.search(r"barcode (TCGA-[A-Z0-9-]+)", desc)
    if m:
        return m.group(1)
    m = re.search(r"Patient (TCGA-[A-Z0-9-]+) ", desc)
    if m:
        return m.group(1)
    m = re.search(r"patient (TCGA-[A-Z0-9-]+) ", desc)
    if m:
        return m.group(1)
    return None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Drop rows without a barcode
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])

# Histology type: we'll use the icd_o_3_histology code as histology type
clin_df['histology_type'] = clin_df['icd_o_3_histology']

# Filter RNA for those barcodes
merged = pd.merge(rna_df, clin_df[['ParticipantBarcode','histology_type']], on='ParticipantBarcode', how='inner')

# Remove invalid IGF2 expression: non-numeric or missing
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged.dropna(subset=['normalized_count','histology_type'])

# Exclude histology annotations enclosed in square brackets
# (none expected for icd_o_3_histology, but we apply the rule generically)
mask_sq = merged['histology_type'].astype(str).str.match(r"^\[.*\]$")
merged = merged[~mask_sq]

# Compute log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x + 1.0) if x >= 0 else None)
merged = merged.dropna(subset=['log10_expr'])

# Group by histology_type and compute mean
result_series = merged.groupby('histology_type')['log10_expr'].mean().sort_index()

# Format with at least four decimal places
result = {str(k): float(f"{v:.6f}") for k, v in result_series.items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UiLcwcUisOZ9sWIdDmElY7fe': 'file_storage/call_UiLcwcUisOZ9sWIdDmElY7fe.json', 'var_call_xcdPFb9s6QVkYPOfPXmHNsGB': ['clinical_info'], 'var_call_bdymrBBHMriETIvXndtKj9p2': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}], 'var_call_rABojyiiC0cwuljedayHebHr': 'file_storage/call_rABojyiiC0cwuljedayHebHr.json', 'var_call_jsVezBrewkdVlPdVZepz9vx7': 'file_storage/call_jsVezBrewkdVlPdVZepz9vx7.json'}

exec(code, env_args)
