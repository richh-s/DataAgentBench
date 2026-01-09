code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

biz = load_records(var_call_NFEvdMmwAZrZR9o392X4YuFv)
dfb = pd.DataFrame(biz)

desc = dfb['description'].astype(str)
# try common pattern: ' in City, ST,'
pat1 = re.compile(r"\bin\s+[^,]+,\s*([A-Z]{2})\b")
ex1 = desc.str.extract(pat1, expand=False)
# try pattern: ' in City, ST.' or end
pat2 = re.compile(r"\bin\s+[^,]+,\s*([A-Z]{2})(?:\b|\.|\s)")
ex2 = desc.str.extract(pat2, expand=False)
# try address style: 'City, ST' anywhere
pat3 = re.compile(r"\b([A-Z]{2})\b")

sample = dfb.head(50).assign(ex1=ex1.head(50), ex2=ex2.head(50))[['description','ex1','ex2']].to_dict('records')

out={'non_null_ex1': int(ex1.notna().sum()), 'non_null_ex2': int(ex2.notna().sum()), 'sample': sample[:5]}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NFEvdMmwAZrZR9o392X4YuFv': 'file_storage/call_NFEvdMmwAZrZR9o392X4YuFv.json', 'var_call_S7DU8KadOMgbH0YSvnrEUPHf': 'file_storage/call_S7DU8KadOMgbH0YSvnrEUPHf.json', 'var_call_HTO75oPyIwPVZTi0znAPIaAS': {'state': None, 'total_review_count': None, 'average_rating': None}}

exec(code, env_args)
