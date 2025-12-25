code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_wOKoM4R79ZT6Fu5v3TRM3bqH)
records = json.loads(path.read_text())

df = pd.DataFrame(records)

def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    if attrs.get('BikeParking') in ['True', True]:
        return True
    bp = attrs.get('BusinessParking')
    if isinstance(bp, str):
        s = bp.lower()
        if 'true' in s and "none" not in s:
            return True
    return False

eligible = df[df['attributes'].apply(has_parking)][['business_id']].drop_duplicates()
result = eligible.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_wOKoM4R79ZT6Fu5v3TRM3bqH': 'file_storage/call_wOKoM4R79ZT6Fu5v3TRM3bqH.json'}

exec(code, env_args)
