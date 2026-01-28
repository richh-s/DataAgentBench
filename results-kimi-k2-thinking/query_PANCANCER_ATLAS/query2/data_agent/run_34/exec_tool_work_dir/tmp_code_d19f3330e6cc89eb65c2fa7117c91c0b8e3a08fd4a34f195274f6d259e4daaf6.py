code = """import json, re, os

# Load BRCA clinical data
brca_path = str(var_functions.query_db:54).strip("'")
brca_data = json.load(open(brca_path, 'r'))

# Load CDH1 mutation data  
cdh1_path = str(var_functions.query_db:76).strip("'")
cdh1_data = json.load(open(cdh1_path, 'r'))

print('BRCA records:', len(brca_data))
print('CDH1 records:', len(cdh1_data))

# Identify alive BRCA patients and their histological types
alive_brca = {}
for rec in brca_data:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type', 'Unknown')
    if 'Alive' in desc:
        m = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', desc)
        if m:
            alive_brca[m.group(1)] = hist

# Get CDH1 mutated patients
cdh1_patients = set([x['ParticipantBarcode'] for x in cdh1_data])

# Calculate mutation rates by histology
from collections import defaultdict
stats = defaultdict(lambda: [0, 0])
for code, hist in alive_brca.items():
    stats[hist][0] += 1
    if code in cdh1_patients:
        stats[hist][1] += 1

# Determine top 3 by percentage
results = []
for hist, (total, mutated) in stats.items():
    if total >= 3:
        pct = round((mutated / total) * 100, 1)
        results.append((hist, pct, mutated, total))

top3 = sorted(results, key=lambda x: x[1], reverse=True)[:3]

# Format output for final answer
output_lines = []
output_lines.append('Top 3 histological types with highest CDH1 mutation percentage among alive BRCA patients:')
output_lines.append('')
for i, (hist, pct, mut, total) in enumerate(top3, 1):
    output_lines.append('{}. {}: {}% ({}/{} patients)'.format(i, hist, pct, mut, total))

final_answer = '\n'.join(output_lines)
print('__RESULT__:')
print(final_answer)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:18': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Tumor_SampleBarcode': 'TCGA-A8-A091-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A091-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A091-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A091-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.727G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Tumor_SampleBarcode': 'TCGA-A8-A0A1-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A1-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A1-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A1-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q307Hfs*2', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.921_955delAGATCCTGAGCTCCCTGACAAAAATATGTTCACCA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Tumor_SampleBarcode': 'TCGA-A8-A0A9-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A9-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A9-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A9-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q503*', 'Variant_Classification': 'Nonsense_Mutation', 'HGVSc': 'c.1507C>T', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Tumor_SampleBarcode': 'TCGA-AA-3821-01A', 'Tumor_AliquotBarcode': 'TCGA-AA-3821-01A-01W-0995-10', 'Normal_SampleBarcode': 'TCGA-AA-3821-10A', 'Normal_AliquotBarcode': 'TCGA-AA-3821-10A-01W-0995-10', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V365I', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1093G>A', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Tumor_AliquotBarcode': 'TCGA-A2-A0YL-01A-21D-A10G-09', 'Normal_SampleBarcode': 'TCGA-A2-A0YL-10A', 'Normal_AliquotBarcode': 'TCGA-A2-A0YL-10A-01D-A10G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.1090_1100delACAGTCACTGA', 'CENTERS': 'INDELOCATOR*|PINDEL', 'FILTER': 'PASS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.query_db:94': [], 'var_functions.query_db:98': []}

exec(code, env_args)
