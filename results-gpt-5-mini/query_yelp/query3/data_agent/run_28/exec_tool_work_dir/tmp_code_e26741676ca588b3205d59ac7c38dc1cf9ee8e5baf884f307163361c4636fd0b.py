code = """import json
import ast

# Load the full business collection result from the provided file path
businesses = json.load(open(var_call_wFNTlM4QAV9TUcC6xkswH3Wg, 'r'))

# Extract target business_ids from review results
review_refs = var_call_5PF0SDjuAlSgAHKzbH0odTuj
target_ids = set()
for r in review_refs:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        target_ids.add('businessid_' + br.split('_', 1)[1])

# Build a dict for quick lookup
biz_map = {b.get('business_id'): b.get('attributes') for b in businesses}

count = 0
matched = 0
for bid in target_ids:
    attrs = biz_map.get(bid, None)
    if attrs is None:
        # missing or null attributes -> treat as no parking
        continue
    matched += 1
    has_parking = False
    # attributes may be a dict or a string
    if isinstance(attrs, dict):
        bike = attrs.get('BikeParking')
        bp = attrs.get('BusinessParking') or attrs.get('Businessparking') or attrs.get('businessparking')
    elif isinstance(attrs, str):
        # string could be "None" or a repr of a dict or JSON-like
        if attrs == 'None':
            bike = None
            bp = None
        else:
            # try to parse as dict-like string
            try:
                parsed = ast.literal_eval(attrs)
                if isinstance(parsed, dict):
                    bike = parsed.get('BikeParking') or parsed.get('bikeparking')
                    bp = parsed.get('BusinessParking') or parsed.get('businessparking')
                else:
                    bike = None
                    bp = None
            except Exception:
                bike = None
                bp = None
    else:
        bike = None
        bp = None

    # Normalize bike
    if isinstance(bike, str):
        if bike.lower().strip(" \"'") == 'true':
            has_parking = True
    elif isinstance(bike, bool):
        if bike:
            has_parking = True

    # Normalize business parking
    if not has_parking and bp is not None:
        # bp could be a dict or a string representation
        if isinstance(bp, dict):
            # If any value True -> has parking
            for v in bp.values():
                if isinstance(v, bool) and v:
                    has_parking = True
                    break
                if isinstance(v, str) and v.lower().strip(" \"'") == 'true':
                    has_parking = True
                    break
        elif isinstance(bp, str):
            if bp == 'None':
                pass
            else:
                try:
                    parsed_bp = ast.literal_eval(bp)
                    if isinstance(parsed_bp, dict):
                        for v in parsed_bp.values():
                            if isinstance(v, bool) and v:
                                has_parking = True
                                break
                            if isinstance(v, str) and v.lower().strip(" \"'") == 'true':
                                has_parking = True
                                break
                except Exception:
                    # fallback: if string contains "True" then assume parking
                    if 'True' in bp or 'true' in bp:
                        has_parking = True

    if has_parking:
        count += 1

# Prepare result as JSON-serializable string
import json
result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ahykiNY0zABwSHlCxeCTCLuE': ['checkin', 'business'], 'var_call_YaeHjrzfmwQaqjHlu4h3b9gG': ['review', 'tip', 'user'], 'var_call_5PF0SDjuAlSgAHKzbH0odTuj': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}], 'var_call_wFNTlM4QAV9TUcC6xkswH3Wg': 'file_storage/call_wFNTlM4QAV9TUcC6xkswH3Wg.json'}

exec(code, env_args)
