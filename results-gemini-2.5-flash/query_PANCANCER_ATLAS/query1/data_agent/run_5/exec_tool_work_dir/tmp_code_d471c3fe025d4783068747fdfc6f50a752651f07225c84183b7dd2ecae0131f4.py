code = """import json
import pandas as pd

clinical_info_lgg = pd.read_json(locals()['var_function-call-12761025957224578765'])

def extract_participant_barcode(description):
    try:
        return description.split('TCGA-')[1].split(' ')[0][:12]
    except IndexError:
        return None

clinical_info_lgg['ParticipantBarcode'] = clinical_info_lgg['Patient_description'].apply(extract_participant_barcode)
lgg_patients = clinical_info_lgg[['ParticipantBarcode', 'histological_type']].dropna().drop_duplicates()

print('__RESULT__:')
print(lgg_patients.to_json(orient='records'))"""

env_args = {'var_function-call-4957086281897016977': ['clinical_info'], 'var_function-call-416097526651329997': 'file_storage/function-call-416097526651329997.json', 'var_function-call-3730502989688273455': [], 'var_function-call-15383304184964350761': 'file_storage/function-call-15383304184964350761.json', 'var_function-call-12761025957224578765': 'file_storage/function-call-12761025957224578765.json'}

exec(code, env_args)
