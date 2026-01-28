code = """import json
import re
from collections import defaultdict

# Load the large query results from file paths provided in storage
with open(var_call_NUMdkW3Vwbd69CqLMhVWRsYj, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_5yc2JcsnPAq7OS0rdmLmh0xr, 'r') as f:
    mutation_records = json.load(f)

# Extract female BRCA patients with known histological_type
female_brca = []
pattern = re.compile(r'(TCGA-[A-Z0-9-]+)', re.IGNORECASE)
for rec in clinical_records:
    pd = rec.get('Patient_description') or ''
    hist = rec.get('histological_type')
    if not hist:
        continue
    if 'female' in pd.lower() and 'breast' in pd.lower():
        m = pattern.search(pd)
        if m:
            barcode = m.group(1).upper()
            female_brca.append({'barcode': barcode, 'histological_type': hist})

# Unique by barcode: prefer first occurrence
unique = {}
for rec in female_brca:
    if rec['barcode'] not in unique:
        unique[rec['barcode']] = rec['histological_type']

# Build mutated barcode set (CDH1 PASS)
mutated = set()
for rec in mutation_records:
    pb = rec.get('ParticipantBarcode')
    if pb:
        mutated.add(pb.upper())

# Build contingency counts per histological_type
counts = defaultdict(lambda: {'mutated': 0, 'wildtype': 0})
for barcode, hist in unique.items():
    if barcode in mutated:
        counts[hist]['mutated'] += 1
    else:
        counts[hist]['wildtype'] += 1

# Exclude categories with marginal totals <= 10
included = {}
excluded = []
for hist, vals in counts.items():
    total = vals['mutated'] + vals['wildtype']
    if total > 10:
        included[hist] = vals
    else:
        excluded.append({'histological_type': hist, 'total': total})

# If less than 2 categories included, cannot compute chi-square
result = {}
if len(included) < 2:
    result = {
        'error': 'Not enough histological categories with total > 10 to compute chi-square.',
        'num_included_categories': len(included),
        'excluded_categories': excluded
    }
else:
    # Build contingency matrix for included rows
    rows = list(included.keys())
    # columns mutated (yes) and wildtype (no)
    grand_total = 0
    row_totals = {}
    col_totals = {'mutated': 0, 'wildtype': 0}
    for r in rows:
        m = included[r]['mutated']
        w = included[r]['wildtype']
        row_totals[r] = m + w
        col_totals['mutated'] += m
        col_totals['wildtype'] += w
        grand_total += (m + w)

    # Compute chi-square
    chi2 = 0.0
    expected = {}
    for r in rows:
        expected[r] = {}
        for c in ['mutated', 'wildtype']:
            E = (row_totals[r] * col_totals[c]) / grand_total if grand_total>0 else 0
            expected[r][c] = E
            O = included[r][c]
            if E > 0:
                chi2 += (O - E)**2 / E
    
    result = {
        'chi2': round(chi2, 6),
        'grand_total': grand_total,
        'row_totals': row_totals,
        'col_totals': col_totals,
        'included_histological_types': rows,
        'contingency_table': included,
        'expected_counts': expected,
        'excluded_categories': excluded
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Tp2aA7D0J7jYlQhhXhY2VQim': ['clinical_info'], 'var_call_cdTvpOrYGzdFXsfdpJ1ux1K7': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Vy0gsTfK1zLbTquQR4j3TFwL': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_ZVSjelHnxLqERt22yn5Y7aGy': [], 'var_call_n35LWzEYTcQ3ittUaXGyros7': 'file_storage/call_n35LWzEYTcQ3ittUaXGyros7.json', 'var_call_NUMdkW3Vwbd69CqLMhVWRsYj': 'file_storage/call_NUMdkW3Vwbd69CqLMhVWRsYj.json', 'var_call_5yc2JcsnPAq7OS0rdmLmh0xr': 'file_storage/call_5yc2JcsnPAq7OS0rdmLmh0xr.json'}

exec(code, env_args)
