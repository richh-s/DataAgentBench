code = """import pandas as pd, json
import re
# load 5-row preview file
path = var_call_s9J8KbRCbUNgfEXAjSvxe2hJ
import pathlib
text = pathlib.Path(path).read_text()
rows = json.loads(text)
cols = list(rows[0].keys())
# find likely acronym/cancer type column names
cands = [c for c in cols if re.search(r'acron|cancer|project|study|cohort|disease|type', c, re.I)]
# also show gender-related columns
gender_cands = [c for c in cols if re.search(r'gender|sex', c, re.I)]
# histology columns
hist_cands = [c for c in cols if re.search(r'histo', c, re.I)]
res = {"candidate_cancer_columns": cands, "candidate_gender_columns": gender_cands, "candidate_histology_columns": hist_cands, "all_columns_count": len(cols)}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_OdZYUDxvtvwydIUCVd5Y91ET': 'file_storage/call_OdZYUDxvtvwydIUCVd5Y91ET.json', 'var_call_iDs8l5svOQckP7ca5YFdAvFj': 'file_storage/call_iDs8l5svOQckP7ca5YFdAvFj.json', 'var_call_y4fgr56kJluIzXuDf9aHdkA1': ['clinical_info'], 'var_call_s9J8KbRCbUNgfEXAjSvxe2hJ': 'file_storage/call_s9J8KbRCbUNgfEXAjSvxe2hJ.json'}

exec(code, env_args)
