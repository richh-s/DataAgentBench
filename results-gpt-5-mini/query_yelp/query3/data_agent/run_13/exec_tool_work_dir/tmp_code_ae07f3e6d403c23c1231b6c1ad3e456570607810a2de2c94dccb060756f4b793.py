code = """import json, ast
# Load variables from storage
review_refs = var_call_K31Y6FG1NJftQ9th7rMBPLKQ
business_file = var_call_uFlbUTVvnlK88fQUhm5fESf6

# Read full business data from file
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Build set of business_ids corresponding to review business_ref values
ids = set()
for r in review_refs:
    br = r.get('business_ref')
    if br is None:
        continue
    if br.startswith('businessref_'):
        suffix = br.split('_', 1)[1]
        ids.add('businessid_' + suffix)
    else:
        # fallback
        ids.add(br)

# Map business_id to attributes
biz_map = {b.get('business_id'): b.get('attributes') for b in businesses}

matching = []
for bid in ids:
    attrs = biz_map.get(bid)
    has = False
    # Normalize attrs
    if attrs is None or attrs == 'None':
        attrs_dict = None
    else:
        if isinstance(attrs, str):
            # try to parse string that represents a dict
            s = attrs
            if s.strip() == 'None':
                attrs_dict = None
            else:
                try:
                    # replace leading u' occurrences to be safe
                    s2 = s.replace("u'", "'").replace('u"', '"')
                    attrs_dict = ast.literal_eval(s2)
                    # If result is not a dict, set None
                    if not isinstance(attrs_dict, dict):
                        attrs_dict = None
                except Exception:
                    # fallback: try eval in restricted env
                    try:
                        attrs_dict = eval(s, {'__builtins__': None}, {})
                        if not isinstance(attrs_dict, dict):
                            attrs_dict = None
                    except Exception:
                        attrs_dict = None
        elif isinstance(attrs, dict):
            attrs_dict = attrs
        else:
            attrs_dict = None

    if attrs_dict:
        # Check BikeParking
        bike = attrs_dict.get('BikeParking') if isinstance(attrs_dict, dict) else None
        if bike is not None:
            if isinstance(bike, bool):
                if bike:
                    has = True
            elif isinstance(bike, str):
                if 'true' in bike.lower():
                    has = True
        # Check BusinessParking
        if not has:
            bp = attrs_dict.get('BusinessParking')
            if bp is not None:
                # bp may be dict or string
                bp_dict = None
                if isinstance(bp, dict):
                    bp_dict = bp
                elif isinstance(bp, str):
                    s = bp
                    if s.strip() != 'None':
                        try:
                            s2 = s.replace("u'", "'").replace('u"', '"')
                            bp_dict = ast.literal_eval(s2)
                        except Exception:
                            try:
                                bp_dict = eval(s, {'__builtins__': None}, {})
                            except Exception:
                                bp_dict = None
                if isinstance(bp_dict, dict):
                    for v in bp_dict.values():
                        if isinstance(v, bool) and v:
                            has = True
                            break
                        if isinstance(v, str) and 'true' in v.lower():
                            has = True
                            break
                        if isinstance(v, (int, float)) and v != 0:
                            has = True
                            break
    # If attributes dict was None, still could have 'BikeParking' or 'BusinessParking' as top-level? handled above
    if has:
        matching.append(bid)

count = len(matching)

# Prepare result as simple int JSON
import json
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_K31Y6FG1NJftQ9th7rMBPLKQ': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_uFlbUTVvnlK88fQUhm5fESf6': 'file_storage/call_uFlbUTVvnlK88fQUhm5fESf6.json'}

exec(code, env_args)
