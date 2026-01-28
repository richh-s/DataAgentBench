code = """import json, ast

# data from previous tool calls
reviews = var_call_Vyh5SnHllKqITLDJEsYeXCR6
businesses_json_path = var_call_1XdIjP84AZxlcTpAvx2UIIR6

# Build set of business IDs from reviews (map businessref_X -> businessid_X)
review_business_ids = set()
for r in reviews:
    br = r.get('business_ref')
    if br is None:
        continue
    if br.startswith('businessref_'):
        review_business_ids.add(br.replace('businessref_', 'businessid_'))
    else:
        review_business_ids.add(br)

# Load full business records from JSON file
with open(businesses_json_path, 'r') as f:
    businesses = json.load(f)

# helper to determine if a value indicates True
def is_true_value(v):
    if v is True:
        return True
    if v is False or v is None:
        return False
    s = str(v).lower()
    if 'true' in s:
        return True
    return False

# helper to parse possible dict-string into dict
def parse_possible_dict(val):
    if isinstance(val, dict):
        return val
    if val is None:
        return None
    s = str(val)
    # clean unicode prefixes
    s = s.replace('u\'', "'").replace('u\"', '"')
    try:
        parsed = ast.literal_eval(s)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        pass
    return None


def offers_parking(attributes):
    if attributes is None:
        return False
    # attributes might be a string like "None" or a dict
    if isinstance(attributes, str):
        if attributes.lower() == 'none':
            return False
        # try to parse as JSON/dict
        try:
            # some strings are dict-like
            parsed = ast.literal_eval(attributes)
            if isinstance(parsed, dict):
                attributes = parsed
            else:
                return False
        except Exception:
            return False
    # normalize keys to lowercase for safe access
    if isinstance(attributes, dict):
        norm = {k.lower(): v for k, v in attributes.items()}
        # check bike parking
        bike_val = norm.get('bikeparking')
        if bike_val is not None and is_true_value(bike_val):
            return True
        # check business parking
        bus_val = norm.get('businessparking')
        if bus_val is not None:
            # bus_val might be a dict or string representation
            parsed = parse_possible_dict(bus_val)
            if parsed:
                # check any parking type True
                for pv in parsed.values():
                    if is_true_value(pv):
                        return True
            else:
                # if string contains 'true' or not 'none'
                if is_true_value(bus_val):
                    return True
        return False
    return False

# Iterate businesses and count those in review set that offer either parking
count = 0
matched_ids = []
# Create a map for quick lookup
biz_map = {b.get('business_id'): b for b in businesses if 'business_id' in b}
for bid in review_business_ids:
    b = biz_map.get(bid)
    if not b:
        continue
    attrs = b.get('attributes')
    if offers_parking(attrs):
        count += 1
        matched_ids.append(bid)

# Prepare result
result = {"count": count, "business_ids": sorted(matched_ids)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Vyh5SnHllKqITLDJEsYeXCR6': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}], 'var_call_Ll3cs9KVnKjmIg2chbQS7yiT': ['checkin', 'business'], 'var_call_1XdIjP84AZxlcTpAvx2UIIR6': 'file_storage/call_1XdIjP84AZxlcTpAvx2UIIR6.json'}

exec(code, env_args)
