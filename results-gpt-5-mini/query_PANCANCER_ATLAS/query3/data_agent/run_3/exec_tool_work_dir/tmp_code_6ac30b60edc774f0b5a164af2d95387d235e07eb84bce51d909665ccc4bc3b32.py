code = """import json
import re
import pandas as pd

# Load clinical BRCA female records from storage file
clinical_path = var_call_POXIeDzAe66pn6Eqzva8pqaZ
with open(clinical_path, 'r') as f:
    clinical_data = json.load(f)

# Load CDH1 mutation records (already in storage variable)
mutation_data = var_call_ZsTwTvn3HMvE6steM5WMj773

# Convert to DataFrame
clin_df = pd.DataFrame(clinical_data)
mut_df = pd.DataFrame(mutation_data)

# Extract TCGA participant barcodes from Patient_description
barcode_re = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{3,6})', re.IGNORECASE)

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = barcode_re.search(desc)
    return m.group(1).upper() if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Keep only FEMALE patients and known histological_type
clin_df = clin_df[clin_df['Patient_description'].str.contains('FEMALE', case=False, na=False)]
clin_df = clin_df[clin_df['ParticipantBarcode'].notnull()]
clin_df = clin_df[clin_df['histological_type'].notnull()]

# Clean histological_type strings
clin_df['histological_type'] = clin_df['histological_type'].astype(str).str.strip()
clin_df = clin_df[~clin_df['histological_type'].str.lower().isin(['none', 'unknown', '', 'other  specify', 'other specify'])]

# Keep one entry per participant (if duplicates, keep first)
clin_df = clin_df.drop_duplicates(subset=['ParticipantBarcode'], keep='first')

# Prepare mutation set: participants with PASS-filtered CDH1 mutations
mut_df = mut_df[mut_df['Hugo_Symbol'] == 'CDH1']
# Consider only reliable mutation entries (FILTER == 'PASS')
pass_mut = mut_df[mut_df['FILTER'].str.upper() == 'PASS']
pass_participants = set(pass_mut['ParticipantBarcode'].str.upper())

# Build presence flag for clinical participants
clin_df['CDH1_mutated'] = clin_df['ParticipantBarcode'].apply(lambda x: x.upper() in pass_participants)

# Build contingency table
contingency = clin_df.groupby(['histological_type', 'CDH1_mutated']).size().unstack(fill_value=0)

# Ensure both columns present
for col in [False, True]:
    if col not in contingency.columns:
        contingency[col] = 0
contingency = contingency[[True, False]]
contingency.columns = ['mutated', 'not_mutated']

# Exclude histological types with marginal totals <= 10
contingency['row_total'] = contingency['mutated'] + contingency['not_mutated']
filtered = contingency[contingency['row_total'] > 10].copy()

# If no categories remain, return a message
if filtered.empty:
    result = {
        'error': 'No histological categories with marginal totals > 10 after filtering.'
    }
else:
    # Compute chi-square statistic
    grand_total = filtered['row_total'].sum()
    col_totals = filtered[['mutated', 'not_mutated']].sum()

    chi2 = 0.0
    expected = {}
    for idx, row in filtered.iterrows():
        rtot = row['row_total']
        expected_mut = (rtot * col_totals['mutated']) / grand_total
        expected_not = (rtot * col_totals['not_mutated']) / grand_total
        expected[idx] = {'mutated': expected_mut, 'not_mutated': expected_not}
        # add contributions
        if expected_mut > 0:
            chi2 += (row['mutated'] - expected_mut) ** 2 / expected_mut
        if expected_not > 0:
            chi2 += (row['not_mutated'] - expected_not) ** 2 / expected_not

    # Prepare output
    result = {
        'chi2': chi2,
        'grand_total': int(grand_total),
        'column_totals': {'mutated': int(col_totals['mutated']), 'not_mutated': int(col_totals['not_mutated'])},
        'included_histological_types': list(filtered.index.astype(str)),
        'contingency_table': {idx: {'mutated': int(row['mutated']), 'not_mutated': int(row['not_mutated'])} for idx, row in filtered[['mutated','not_mutated']].iterrows()},
        'expected_counts': {idx: {'mutated': expected[idx]['mutated'], 'not_mutated': expected[idx]['not_mutated']} for idx in expected}
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_n2S2zfj8mkJMF680ydOZ5aMP': ['clinical_info'], 'var_call_WrsOtRBTAFd779sbmoyWs7AV': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_hssVOe76hYStmHJdCXAoUb8A': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_7WUnrJphSkGKJxkxOyS5IGGm': [{'diagnosis': 'None'}, {'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_EKhW2LY7CNjKWvlBI0qebyy9': 'file_storage/call_EKhW2LY7CNjKWvlBI0qebyy9.json', 'var_call_ZsTwTvn3HMvE6steM5WMj773': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q307Hfs*2', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q503*', 'Variant_Classification': 'Nonsense_Mutation', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V365I', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N315Ifs*41', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A824V', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.G169Rfs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R598Q', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L249V', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N785S', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V425I', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.W409L', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L776M', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-X6-A8C2', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q449K', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EE-A2GO', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.X441_splice', 'Variant_Classification': 'Splice_Site', 'FILTER': 'oxog'}, {'ParticipantBarcode': 'TCGA-13-0889', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V493Gfs*44', 'Variant_Classification': 'Frame_Shift_Ins', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A6', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.X522_splice', 'Variant_Classification': 'Splice_Site', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-A02K', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R224C', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AG-3892', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E648*', 'Variant_Classification': 'Nonsense_Mutation', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-63-A5MM', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A719V', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-A2-A0YK', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R63*', 'Variant_Classification': 'Nonsense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-A7-A4SC', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.D288Gfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AC-A3QQ', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q23*', 'Variant_Classification': 'Nonsense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AL', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.I505Sfs*17', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BR-8370', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.D257N', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-CV-6937', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.D569E', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-DD-A4NK', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.K187R', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EW-A1IZ', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.X522_splice', 'Variant_Classification': 'Splice_Site', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-FP-A8CX', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Y190C', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-G4-6586', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.P126Rfs*89', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-GC-A3I6', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L798V', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-OD-A75X', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R74Pfs*20', 'Variant_Classification': 'Frame_Shift_Ins', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-A8-A09Z', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.P127Afs*41', 'Variant_Classification': 'Frame_Shift_Ins', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A2', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E165_P170del', 'Variant_Classification': 'In_Frame_Del', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-55-A4DF', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A408P', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-5L-AAT0', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q23*', 'Variant_Classification': 'Nonsense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-77-A5G1', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V425I', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-A2-A0T4', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E757*', 'Variant_Classification': 'Frame_Shift_Ins', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-A5-A1OF', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.G49C', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AX-A06L', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R732Q', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q23*', 'Variant_Classification': 'Nonsense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BH-A18F', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.L583Pfs*6', 'Variant_Classification': 'Frame_Shift_Ins', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BH-A209', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R63*', 'Variant_Classification': 'Nonsense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BR-4188', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.G212E', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BR-4279', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R222G', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BR-A44T', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.I248F', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0TE', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q95L', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-C8-A274', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T627Hfs*36', 'Variant_Classification': 'Frame_Shift_Ins', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D1-A103', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.R124H', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}], 'var_call_POXIeDzAe66pn6Eqzva8pqaZ': 'file_storage/call_POXIeDzAe66pn6Eqzva8pqaZ.json', 'var_call_NIzM3rePIIELOc8E55aWfbGg': {'clinical_type': 'list', 'clinical_len': 200, 'clinical_first_keys': ['patient_id', 'Patient_description', 'histological_type'], 'mutation_type': 'list', 'mutation_len': 50, 'mutation_first_keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER']}}

exec(code, env_args)
