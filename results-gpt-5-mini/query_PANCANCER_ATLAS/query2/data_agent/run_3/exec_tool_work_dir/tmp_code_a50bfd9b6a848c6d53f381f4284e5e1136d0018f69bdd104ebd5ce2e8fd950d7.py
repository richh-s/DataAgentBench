code = """import json
import re

# Load the clinical and mutation data from storage file paths
clin_path = var_call_dF39qIlf7E6AVA41sOJEVZyt
mut_path = var_call_yqBx57oZQ7XLPtZLNeehmKsa

with open(clin_path, 'r') as f:
    clin = json.load(f)
with open(mut_path, 'r') as f:
    mut = json.load(f)

# Extract barcode from Patient_description using regex
barcode_re = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)')

barcode_to_hist = {}
for rec in clin:
    desc = rec.get('Patient_description', '') or ''
    hist = rec.get('histological_type') or 'Unknown'
    m = barcode_re.search(desc)
    if not m:
        # try to construct from patient_id if present (some patient_id values are short like A5EH)
        pid = rec.get('patient_id')
        if pid:
            # no reliable way to reconstruct full TCGA barcode, skip
            continue
        else:
            continue
    barcode = m.group(1).upper()
    # map first occurrence
    if barcode not in barcode_to_hist:
        barcode_to_hist[barcode] = hist

# Build histological_type -> set of barcodes (alive BRCA patients)
hist_to_barcodes = {}
for bc, hist in barcode_to_hist.items():
    hist_to_barcodes.setdefault(hist, set()).add(bc)

# Build set of barcodes with CDH1 mutation from mutation data
mut_bcs = set()
for rec in mut:
    if (rec.get('Hugo_Symbol') or '').upper() == 'CDH1':
        pb = (rec.get('ParticipantBarcode') or '').upper()
        if pb:
            mut_bcs.add(pb)

# For each histological type compute totals and mutated counts
results = []
for hist, bcs in hist_to_barcodes.items():
    total = len(bcs)
    if total == 0:
        continue
    mutated = len(sorted(bcs.intersection(mut_bcs)))
    pct = (mutated / total) * 100 if total>0 else 0.0
    results.append({'histological_type': hist, 'total_alive': total, 'mutated_count': mutated, 'mutation_percent': round(pct, 2)})

# Sort by mutation_percent desc, then mutated_count desc, then histological_type
results_sorted = sorted(results, key=lambda x: (-x['mutation_percent'], -x['mutated_count'], x['histological_type']))

top3 = results_sorted[:3]

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_LujSgaQaYg915CRKPu466R02': ['clinical_info'], 'var_call_9V6owfIKCnMI8J36nO9XlVW5': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_KMb5PB6FvHhTmtpTEA85KNFd': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_sP7XLHQvNg041LwqqAX71iup': [{'diagnosis': 'None', 'cnt': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'cnt': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'cnt': '490'}], 'var_call_WoRKraDfyKqxjawr1RWXi3WK': [], 'var_call_0ovWFtX5MY2ctyT2bxAfSC9b': [], 'var_call_B5TdMAzIKX8ARZsGpiF8Nv3V': 'file_storage/call_B5TdMAzIKX8ARZsGpiF8Nv3V.json', 'var_call_0kAvLaDH5m8rT0WXc70mgByh': 'file_storage/call_0kAvLaDH5m8rT0WXc70mgByh.json', 'var_call_dF39qIlf7E6AVA41sOJEVZyt': 'file_storage/call_dF39qIlf7E6AVA41sOJEVZyt.json', 'var_call_9iKjfxHqTgNqpNDCb7QujYTB': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Tumor_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Tumor_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Normal_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'Normal_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Normal_SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Hugo_Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'HGVSp_Short', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '8', 'name': 'Variant_Classification', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '9', 'name': 'HGVSc', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '10', 'name': 'CENTERS', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '11', 'name': 'FILTER', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_yqBx57oZQ7XLPtZLNeehmKsa': 'file_storage/call_yqBx57oZQ7XLPtZLNeehmKsa.json'}

exec(code, env_args)
