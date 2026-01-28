code = """import json

result_file = locals()['var_functions.execute_python:30']

with open(result_file, 'r') as f:
    result = json.load(f)

output = []
for histology in ['Oligodendroglioma', 'Astrocytoma', 'Oligoastrocytoma']:
    if histology in result['averages_by_histology']:
        avg_log10 = result['averages_by_histology'][histology]['avg_log10_expression']
        output.append(histology + ': ' + str(round(avg_log10, 4)))

print('__RESULT__:')
print(json.dumps('\n'.join(output)))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ZNF770', 'Entrez': '54989', 'normalized_count': '1195.92'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'AMELY', 'Entrez': '266', 'normalized_count': '0.0'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'TPTE2P1', 'Entrez': '646405', 'normalized_count': '214.576'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ITGB3', 'Entrez': '3690', 'normalized_count': '13.6303'}], 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'total_lgg_patients': 513, 'patients_with_igf2': 23, 'histology_breakdown': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}, 'averages_by_histology': {'Oligodendroglioma': {'count': 8, 'avg_log10_expression': 2.6825}, 'Astrocytoma': {'count': 10, 'avg_log10_expression': 2.5713}, 'Oligoastrocytoma': {'count': 5, 'avg_log10_expression': 2.7136}}}}

exec(code, env_args)
