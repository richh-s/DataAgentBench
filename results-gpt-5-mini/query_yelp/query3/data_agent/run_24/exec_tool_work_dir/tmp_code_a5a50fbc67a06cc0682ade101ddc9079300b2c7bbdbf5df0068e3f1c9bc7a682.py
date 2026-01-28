code = """import json, ast

reviews = var_call_Vyh5SnHllKqITLDJEsYeXCR6
businesses_json_path = var_call_1XdIjP84AZxlcTpAvx2UIIR6

# Build set of business IDs from reviews
review_business_ids = set()
for r in reviews:
    br = r.get('business_ref')
    if not br:
        continue
    if br.startswith('businessref_'):
        review_business_ids.add(br.replace('businessref_', 'businessid_'))
    else:
        review_business_ids.add(br)

# Load business records from file
with open(businesses_json_path, 'r') as f:
    businesses = json.load(f)

# helpers
def is_true_value(v):
    if v is True:
        return True
    if v is False or v is None:
        return False
    s = str(v).lower()
    return 'true' in s

def parse_possible_dict(val):
    if isinstance(val, dict):
        return val
    if val is None:
        return None
    s = str(val)
    # clean common unicode prefix patterns
    s = s.replace("u'", "'").replace('u"', '"')
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
    # if attributes is the string 'None'
    if isinstance(attributes, str):
        if attributes.strip().lower() == 'none':
            return False
        # try to parse string to dict
        try:
            parsed = ast.literal_eval(attributes)
            if isinstance(parsed, dict):
                attributes = parsed
        except Exception:
            # leave as string
            pass
    if isinstance(attributes, dict):
        # normalize keys
        norm = {k.lower(): v for k, v in attributes.items()}
        # bike parking key
        bike_val = norm.get('bikeparking')
        if bike_val is not None and is_true_value(bike_val):
            return True
        # business parking key
        bus_val = norm.get('businessparking')
        if bus_val is not None:
            parsed = parse_possible_dict(bus_val)
            if parsed:
                for pv in parsed.values():
                    if is_true_value(pv):
                        return True
            else:
                if is_true_value(bus_val):
                    return True
    return False

# Build map of businesses
biz_map = {b.get('business_id'): b for b in businesses if 'business_id' in b}
count = 0
matched_ids = []
for bid in sorted(review_business_ids):
    b = biz_map.get(bid)
    if not b:
        continue
    attrs = b.get('attributes')
    if offers_parking(attrs):
        count += 1
        matched_ids.append(bid)

result = {"count": count, "business_ids": matched_ids}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Vyh5SnHllKqITLDJEsYeXCR6': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}], 'var_call_Ll3cs9KVnKjmIg2chbQS7yiT': ['checkin', 'business'], 'var_call_1XdIjP84AZxlcTpAvx2UIIR6': 'file_storage/call_1XdIjP84AZxlcTpAvx2UIIR6.json'}

exec(code, env_args)
