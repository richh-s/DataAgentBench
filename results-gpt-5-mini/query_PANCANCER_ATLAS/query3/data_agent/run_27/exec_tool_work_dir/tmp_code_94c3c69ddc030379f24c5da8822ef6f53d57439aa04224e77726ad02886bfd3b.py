code = """import pandas as pd
import re
import json

# Load data from storage entries (paths or lists)
def load_var(v):
    if isinstance(v, str):
        # assume file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

clin_list = load_var(var_call_BQ43TojlQDRtdyB8K3m7aoaF)
mut_list = load_var(var_call_n8W82sGDbFVWNhl4od5wYZzY)

clin = pd.DataFrame(clin_list)
mut = pd.DataFrame(mut_list)

# Extract patient barcode from Patient_description
barcode_regex = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)')

def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = barcode_regex.search(text)
    return m.group(1) if m else None

clin['patient_barcode'] = clin['Patient_description'].apply(extract_barcode)

# Clean histological_type
clin['histological_type'] = clin['histological_type'].astype(str).str.strip()
invalid_hist = set(['None', '[Not Applicable]', 'NA', 'nan', ''])
clin = clin[clin['patient_barcode'].notnull()]
clin = clin[~clin['histological_type'].isin(invalid_hist)]

# Exclude generic 'Other' categories
clin = clin[~clin['histological_type'].str.contains('Other', case=False, na=False)]

# Build set of mutated patient barcodes from reliable mutation entries (FILTER == 'PASS')
if 'FILTER' in mut.columns and 'ParticipantBarcode' in mut.columns:
    mut_pass = mut[mut['FILTER'] == 'PASS']
    mutated_patients = set(mut_pass['ParticipantBarcode'].dropna().unique())
else:
    mutated_patients = set()

# Determine mutation presence per patient
clin['CDH1_mutated'] = clin['patient_barcode'].apply(lambda b: 'Yes' if b in mutated_patients else 'No')

# Count per histological type
hist_counts = clin.groupby('histological_type').size().to_dict()
# Exclude categories with marginal totals <= 10
included_hists = [h for h,c in hist_counts.items() if c > 10]

# Build contingency table for included histologies
contingency = {}
for h in included_hists:
    sub = clin[clin['histological_type'] == h]
    yes = int((sub['CDH1_mutated'] == 'Yes').sum())
    no = int((sub['CDH1_mutated'] == 'No').sum())
    contingency[h] = {'Yes': yes, 'No': no, 'Total': yes+no}

# If no histologies included, return a message
if len(included_hists) == 0:
    result = {'error': 'No histological categories with marginal totals > 10 were found.'}
else:
    # Compute chi-square statistic
    rows = included_hists
    cols = ['Yes', 'No']
    observed = [[contingency[r][c] for c in cols] for r in rows]
    grand_total = sum(sum(r) for r in observed)
    row_totals = [sum(r) for r in observed]
    col_totals = [sum(observed[i][j] for i in range(len(rows))) for j in range(len(cols))]
    chi2 = 0.0
    expected = [[(row_totals[i]*col_totals[j])/grand_total for j in range(len(cols))] for i in range(len(rows))]
    for i in range(len(rows)):
        for j in range(len(cols)):
            E = expected[i][j]
            O = observed[i][j]
            if E > 0:
                chi2 += (O - E)**2 / E
    result = {
        'chi2': chi2,
        'grand_total': int(grand_total),
        'rows': rows,
        'cols': cols,
        'observed': observed,
        'expected': [[round(x,4) for x in row] for row in expected],
        'contingency': contingency
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AWfLxzsRaU1ygdb6MjxVO4vv': 'file_storage/call_AWfLxzsRaU1ygdb6MjxVO4vv.json', 'var_call_V2tef5BcQWNGhbzssNRVkUSH': [], 'var_call_UGdCSff0Eys6488x63XH1hD9': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_n8W82sGDbFVWNhl4od5wYZzY': 'file_storage/call_n8W82sGDbFVWNhl4od5wYZzY.json', 'var_call_KAHmpkWspb6oLXY6xII6CltO': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_BQ43TojlQDRtdyB8K3m7aoaF': 'file_storage/call_BQ43TojlQDRtdyB8K3m7aoaF.json'}

exec(code, env_args)
