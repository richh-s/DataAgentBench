code = """import json
import pandas as pd
import re

# Load clinical data from the provided file path variable
clinical_path = var_call_VvVSCfuPge1pljJcFewIC9bu
with open(clinical_path, 'r') as f:
    clinical = json.load(f)

df = pd.DataFrame(clinical)

# Load mutation participant list
mut_list = var_call_PET98RzyfC128s3vtd4NNJXX
mut_set = set([r['ParticipantBarcode'] for r in mut_list if r.get('ParticipantBarcode')])

# Filter female BRCA (breast) patients
mask_female = df['Patient_description'].str.contains('FEMALE', case=False, na=False)
mask_breast = df['Patient_description'].str.contains('breast', case=False, na=False) | df['tumor_tissue_site'].str.contains('breast', case=False, na=False)
sub = df[mask_female & mask_breast].copy()

# Keep only known histological types
def hist_known(x):
    if pd.isna(x):
        return False
    s = str(x).strip()
    if s == '' or s.lower() in ('none','unknown'):
        return False
    if s.lower().startswith('other'):
        return False
    return True

sub = sub[sub['histological_type'].apply(hist_known)].copy()

# Extract TCGA participant barcode from Patient_description
pattern_specific = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', re.IGNORECASE)
pattern_broad = re.compile(r'(TCGA[-A-Za-z0-9]+)', re.IGNORECASE)

def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = pattern_specific.search(text)
    if m:
        return m.group(0).upper()
    m = pattern_broad.search(text)
    if m:
        # truncate at any non alnum or trailing punctuation
        token = m.group(1)
        # remove trailing punctuation
        token = re.sub(r"[^A-Z0-9-]$", "", token, flags=re.IGNORECASE)
        return token.upper()
    return None

sub['ParticipantBarcode'] = sub['Patient_description'].apply(extract_barcode)
# Drop rows without an extracted barcode
sub = sub[sub['ParticipantBarcode'].notna()].copy()

# Flag mutated if barcode in mut_set
sub['CDH1_mutated'] = sub['ParticipantBarcode'].isin(mut_set)

# Build contingency by histological_type
group = sub.groupby('histological_type').agg(total=('Patient_description','count'), mutated=('CDH1_mutated','sum'))
if 'mutated' in group.columns:
    group['not_mutated'] = group['total'] - group['mutated']
else:
    group['mutated'] = 0
    group['not_mutated'] = group['total']

# Exclude categories with marginal totals <= 10
included = group[group['total'] > 10].copy()
excluded = group[group['total'] <= 10].index.tolist()

# Prepare contingency table
contingency = []
for idx, row in included.iterrows():
    contingency.append({'histological_type': idx, 'mutated': int(row['mutated']), 'not_mutated': int(row['not_mutated']), 'total': int(row['total'])})

# Compute chi-square statistic
# Columns: Mutated (1), Not mutated (2)
rows = len(included)
cols = 2
observed = []
for _, row in included.iterrows():
    observed.append([int(row['mutated']), int(row['not_mutated'])])

grand_total = int(included['total'].sum()) if rows>0 else 0
col_totals = [int(included['mutated'].sum()) if rows>0 else 0, int(included['not_mutated'].sum()) if rows>0 else 0]
row_totals = [int(r['total']) for _, r in included.iterrows()]

chi2 = None
if rows > 0 and grand_total>0:
    chi2_val = 0.0
    for i in range(rows):
        for j in range(cols):
            O = observed[i][j]
            E = (row_totals[i] * col_totals[j]) / grand_total
            if E > 0:
                chi2_val += (O - E)**2 / E
    chi2 = chi2_val

result = {
    'chi2': chi2,
    'degrees_of_freedom': (rows-1)*(cols-1) if rows>0 else None,
    'grand_total_included': grand_total,
    'col_totals': {'mutated': col_totals[0], 'not_mutated': col_totals[1]},
    'row_totals': dict(zip(included.index.tolist(), row_totals)),
    'contingency': contingency,
    'excluded_categories': excluded,
    'total_clinical_female_breast_with_known_histology': int(sub.shape[0])
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ICbsE44gtMFc0POMTIb4qJW9': ['clinical_info'], 'var_call_cRmpPrAMWxarGT16KjhlheSd': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_SrXYfGaIEvVRfC4WUWlUeKte': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_qwjgqWGP0jbOxOjk7pdAhAtE': [], 'var_call_VvVSCfuPge1pljJcFewIC9bu': 'file_storage/call_VvVSCfuPge1pljJcFewIC9bu.json', 'var_call_PET98RzyfC128s3vtd4NNJXX': [{'ParticipantBarcode': 'TCGA-DU-6392', 'mut_count': '3'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'mut_count': '3'}, {'ParticipantBarcode': 'TCGA-AX-A2HD', 'mut_count': '3'}, {'ParticipantBarcode': 'TCGA-B5-A0JY', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-E2-A1IH', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-BR-4279', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-BR-A4IV', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-G2-A3IE', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-06-5416', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-KQ-A41S', 'mut_count': '2'}, {'ParticipantBarcode': 'TCGA-IN-7808', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AC-A6IV', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AR-A5QM', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AC-A4ZE', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-IR-A3LH', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-QF-A5YS', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-PE-A5DD', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-E9-A3X8', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AC-A2B8', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-42-2590', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-DD-A4NK', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-LD-A66U', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BH-A0E9', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-E9-A2JT', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-EE-A2A6', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-3M-AB47', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A1G0', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-CN-6024', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AR-A2LN', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BR-8686', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-4H-AAAK', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-PE-A5DE', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-LD-A7W6', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-05-5428', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AC-A2FG', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-B5-A11G', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-D8-A1Y1', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-D8-A1XO', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AO-A128', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-DF-A2KV', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-VQ-A8PO', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BR-8370', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-F4-6570', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-C8-A1HO', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-DK-A6AW', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-B6-A2IU', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A0CR', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-21-5787', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-B9-A8YI', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-GC-A3I6', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A0SY', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-LL-A9Q3', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A0CK', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A4S2', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A7-A425', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BS-A0UV', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-CD-A4MG', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-CA-6717', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AX-A0J0', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BH-A0HP', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-WT-AB44', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-E1-A7YJ', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A5-A0VO', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BR-8677', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-GM-A5PX', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-E2-A1L8', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A25A', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-OL-A66N', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-XF-AAN0', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BF-A3DL', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-63-A5MH', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-77-A5G1', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-OL-A66K', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-GM-A4E0', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-D7-8574', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-HT-A617', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-DD-AAE3', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BR-6803', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BR-A453', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-EE-A29E', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AC-A2FF', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-AP-A0LM', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-D7-6518', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A6-5661', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-F1-6874', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-E9-A5FK', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BR-8364', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-B0-5692', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-BR-A4J9', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-EW-A6SC', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-F5-6814', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-66-2759', 'mut_count': '1'}, {'ParticipantBarcode': 'TCGA-G9-6365', 'mut_count': '1'}]}

exec(code, env_args)
