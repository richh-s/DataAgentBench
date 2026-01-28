code = """import json, ast

# Load the large query result from the businessinfo_database call
path = var_call_fE2WDEr6bjisfaE5TzqbmaPl
with open(path, 'r') as f:
    data = json.load(f)

count = 0
satisfying = []

def str_to_bool(s):
    if isinstance(s, bool):
        return s
    if s is None:
        return False
    if isinstance(s, (int, float)):
        return bool(s)
    if isinstance(s, str):
        s2 = s.strip().lower()
        if s2 in ("true", "'true'", 'yes', 'y', '1'):
            return True
        return False
    return False

for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes')
    has_bike = False
    has_business_parking = False
    if attrs is None or (isinstance(attrs, str) and attrs.strip().lower() == 'none'):
        pass
    else:
        # attrs may be a dict or a string representation of a dict
        if isinstance(attrs, str):
            # try parse
            try:
                parsed = ast.literal_eval(attrs)
                if isinstance(parsed, dict):
                    attrs = parsed
            except Exception:
                # can't parse, leave as string
                attrs = {'_raw': attrs}
        if isinstance(attrs, dict):
            # BikeParking
            if 'BikeParking' in attrs:
                if str_to_bool(attrs.get('BikeParking')):
                    has_bike = True
            # BusinessParking
            if 'BusinessParking' in attrs:
                bp = attrs.get('BusinessParking')
                if bp is None:
                    has_business_parking = False
                else:
                    # bp could be dict or string
                    if isinstance(bp, str):
                        if bp.strip().lower() == 'none':
                            has_business_parking = False
                        else:
                            try:
                                bp_parsed = ast.literal_eval(bp)
                                if isinstance(bp_parsed, dict):
                                    # check any inner value truthy
                                    any_true = False
                                    for v in bp_parsed.values():
                                        if str_to_bool(v):
                                            any_true = True
                                            break
                                    has_business_parking = any_true
                                else:
                                    # non-dict string -> consider as offering if not 'none'
                                    has_business_parking = True
                            except Exception:
                                # can't parse, but not 'None' => assume offers parking
                                has_business_parking = True
                    elif isinstance(bp, dict):
                        any_true = False
                        for v in bp.values():
                            if str_to_bool(v):
                                any_true = True
                                break
                        has_business_parking = any_true
                    else:
                        # other types, treat truthy
                        has_business_parking = bool(bp)
    if has_bike or has_business_parking:
        satisfying.append(bid)

# Unique count
unique_bids = sorted(set(satisfying))
result_count = len(unique_bids)

import json
print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_suja6VR75Ae07VadWan7OfdR': ['business', 'checkin'], 'var_call_QT3If8Mha9j0LRBPgMjfd3uD': ['review', 'tip', 'user'], 'var_call_XyxsiHTWR4MkmGcKprwr2Ojm': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_fE2WDEr6bjisfaE5TzqbmaPl': 'file_storage/call_fE2WDEr6bjisfaE5TzqbmaPl.json'}

exec(code, env_args)
