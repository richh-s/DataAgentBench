code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

biz = pd.DataFrame(load_records(var_call_IXRsmvUPODRIJr7mp4l2uQsP))

pat = re.compile(r'\b([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Prefer pattern "in City, ST" or "in ... , ST," or ending with ST
    m = re.findall(r'\bin\s+[^,]+,\s*([A-Z]{2})\b', desc)
    if m:
        return m[-1]
    m2 = re.findall(r',\s*([A-Z]{2})\b', desc)
    if m2:
        return m2[-1]
    # fallback: any standalone 2-letter token from known states list
    states = set('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC'.split())
    tokens = pat.findall(desc)
    tokens = [t for t in tokens if t in states]
    return tokens[-1] if tokens else None

biz['state'] = biz['description'].map(extract_state)
res = biz['state'].value_counts(dropna=False).head(20)
print('__RESULT__:')
print(json.dumps(res.to_dict()))"""

env_args = {'var_call_IXRsmvUPODRIJr7mp4l2uQsP': 'file_storage/call_IXRsmvUPODRIJr7mp4l2uQsP.json', 'var_call_K6dAAbajJ8oQTnQ4Clt9GAZ7': 'file_storage/call_K6dAAbajJ8oQTnQ4Clt9GAZ7.json', 'var_call_x36hhPHfOF41me0lzcFupgCQ': {'state': None, 'total_reviews': 0, 'avg_rating': None}}

exec(code, env_args)
