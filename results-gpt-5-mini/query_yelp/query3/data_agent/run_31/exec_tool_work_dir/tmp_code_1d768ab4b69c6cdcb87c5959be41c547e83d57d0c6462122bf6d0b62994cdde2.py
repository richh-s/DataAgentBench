code = """import json
import pandas as pd
# var_call_juYz7LZKfFvjMkQdiw3aGiFF contains the file path to the JSON results from the previous Mongo query
fp = var_call_juYz7LZKfFvjMkQdiw3aGiFF
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Normalize attributes: some are None, some are strings representing dicts
# We'll define functions to detect BikeParking and BusinessParking presence

def has_bike_parking(attr):
    if not isinstance(attr, dict):
        return False
    bp = attr.get('BikeParking')
    if bp is None:
        return False
    # Some values are strings 'True'/'False' or boolean
    if isinstance(bp, bool):
        return bp
    s = str(bp).lower()
    return 'true' in s

import ast

def has_business_parking(attr):
    if not isinstance(attr, dict):
        return False
    bp = attr.get('BusinessParking')
    if bp is None:
        return False
    # bp may be a string like "{'garage': False, 'street': True, ...}" or 'None'
    if isinstance(bp, dict):
        # check if any value True
        return any([v is True or (isinstance(v, str) and 'true' in v.lower()) for v in bp.values()])
    if isinstance(bp, str):
        s = bp.strip()
        if s.lower() == 'none' or s.lower()=='null':
            return False
        try:
            parsed = ast.literal_eval(s)
            if isinstance(parsed, dict):
                return any([v is True or (isinstance(v, str) and 'true' in v.lower()) for v in parsed.values()])
            else:
                return False
        except Exception:
            # fallback: look for 'true' in string
            return 'true' in s.lower()
    return False

# Apply checks

# Ensure attributes are actual dicts or None
# Some entries have attributes as the string "None"
def fix_attr(x):
    if x is None:
        return None
    if isinstance(x, dict):
        return x
    if isinstance(x, str):
        s = x.strip()
        if s.lower()=='none':
            return None
        # sometimes it's a repr of a dict? but for attributes it's usually a dict already
        try:
            parsed = ast.literal_eval(s)
            if isinstance(parsed, dict):
                return parsed
            else:
                # could be a string like "u'free'" etc; we will leave as-is
                return x
        except Exception:
            return x
    return x

# Apply fix

df['attributes_fixed'] = df['attributes'].apply(fix_attr)

df['has_bike'] = df['attributes_fixed'].apply(has_bike_parking)

df['has_business_parking'] = df['attributes_fixed'].apply(has_business_parking)

df['either_parking'] = df['has_bike'] | df['has_business_parking']

# Count how many businesses have either parking
count = int(df['either_parking'].sum())

# For debugging create list of business_ids with either
businesses_list = df[df['either_parking']]['business_id'].tolist()

result = {'count': count, 'business_ids': businesses_list}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MHtmxgvLpqA5KoxSqjS4wVL6': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}], 'var_call_juYz7LZKfFvjMkQdiw3aGiFF': 'file_storage/call_juYz7LZKfFvjMkQdiw3aGiFF.json'}

exec(code, env_args)
