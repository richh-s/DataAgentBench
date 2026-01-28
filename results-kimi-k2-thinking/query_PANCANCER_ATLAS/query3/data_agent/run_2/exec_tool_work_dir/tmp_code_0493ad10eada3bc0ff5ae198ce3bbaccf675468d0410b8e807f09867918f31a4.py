code = """import json

# Read the clinical data
with open("/tmp/var_functions.query_db:22.json", "r") as f:
    clinical_data = json.load(f)

# Let's analyze patient descriptions for cancer types and patient IDs
from collections import Counter
import re

cancer_type_counter = Counter()
patient_ids = []
barcode_to_info = {}

for record in clinical_data:
    desc = record.get("Patient_description", "")
    hist_type = record.get("histological_type", "")
    
    # Extract patient ID/barcodes from descriptions
    barcode_match = re.search(r'TCGA-[0-9A-Z]+-[0-9A-Z]+', desc)
    if barcode_match:
        barcode = barcode_match.group(0)
        patient_ids.append(barcode)
        barcode_to_info[barcode] = {
            "description": desc,
            "histological_type": hist_type
        }
    
    # Count histological types
    cancer_type_counter[hist_type] += 1

print("Top histological types found:")
for ctype, count in cancer_type_counter.most_common(20):
    print(f"  {ctype}: {count}")

print(f"\nTotal unique patient IDs found: {len(set(patient_ids))}")
print("\nSample patient IDs and their descriptions:")
for i, (barcode, info) in enumerate(list(barcode_to_info.items())[:10]):
    print(f"  {barcode}: {info['histological_type']}")

# Check if any of these are breast cancer
print("\nChecking for breast cancer patients...")
breast_patients = {barcode: info for barcode, info in barcode_to_info.items() 
                   if "breast" in info["description"].lower() or 
                      "BRCA" in info["description"] or
                      "Breast" in info["description"]}

print(f"Found {len(breast_patients)} potential breast cancer patients")
for barcode, info in list(breast_patients.items())[:10]:
    print(f"  {barcode}: {info['histological_type']}")
    print(f"    Desc: {info['description'][:100]}...")"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
