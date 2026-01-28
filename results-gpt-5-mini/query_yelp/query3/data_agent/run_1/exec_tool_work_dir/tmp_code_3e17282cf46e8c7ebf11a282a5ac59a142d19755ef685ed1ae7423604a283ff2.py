code = """import json, ast
# var_call_Vg3lSQFuaNC1NOzz4HShfoAs and var_call_JWziLTIBqPtgz9IE50AqMUpx are available from storage
refs = [d['business_ref'] for d in var_call_Vg3lSQFuaNC1NOzz4HShfoAs]
business_ids = set(['businessid_' + ref.split('_', 1)[1] for ref in refs])

with open(var_call_JWziLTIBqPtgz9IE50AqMUpx, 'r') as f:
    docs = json.load(f)

count = 0
matched_ids = []
for doc in docs:
    bid = doc.get('business_id')
    if bid in business_ids:
        attrs = doc.get('attributes')
        has = False
        if attrs and attrs != 'None':
            # attrs may be dict or string
            if isinstance(attrs, dict):
                bp = attrs.get('BikeParking')
                if bp is True or (isinstance(bp, str) and bp.lower() == 'true'):
                    has = True
                bpar = attrs.get('BusinessParking')
                if not has and bpar:
                    if isinstance(bpar, dict):
                        if any((v is True) or (isinstance(v, str) and v.lower() == 'true') for v in bpar.values()):
                            has = True
                    elif isinstance(bpar, str):
                        try:
                            parsed = ast.literal_eval(bpar)
                            if isinstance(parsed, dict) and any((v is True) or (isinstance(v, str) and v.lower() == 'true') for v in parsed.values()):
                                has = True
                        except Exception:
                            if 'True' in bpar:
                                has = True
            elif isinstance(attrs, str):
                # try to literal_eval the whole attributes string
                try:
                    parsed_attrs = ast.literal_eval(attrs)
                    if isinstance(parsed_attrs, dict):
                        bp = parsed_attrs.get('BikeParking')
                        if bp is True or (isinstance(bp, str) and bp.lower() == 'true'):
                            has = True
                        bpar = parsed_attrs.get('BusinessParking')
                        if not has and bpar:
                            if isinstance(bpar, dict):
                                if any((v is True) or (isinstance(v, str) and v.lower() == 'true') for v in bpar.values()):
                                    has = True
                            elif isinstance(bpar, str):
                                try:
                                    parsed = ast.literal_eval(bpar)
                                    if isinstance(parsed, dict) and any((v is True) or (isinstance(v, str) and v.lower() == 'true') for v in parsed.values()):
                                        has = True
                                except Exception:
                                    if 'True' in bpar:
                                        has = True
                except Exception:
                    # fallback simple checks
                    if "BikeParking" in attrs and "True" in attrs:
                        has = True
                    if "BusinessParking" in attrs and "True" in attrs:
                        has = True
        if has:
            count += 1
            matched_ids.append(bid)

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_Vg3lSQFuaNC1NOzz4HShfoAs': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}], 'var_call_PqktJiuSxDUouNwkg1GdclVn': ['checkin', 'business'], 'var_call_JWziLTIBqPtgz9IE50AqMUpx': 'file_storage/call_JWziLTIBqPtgz9IE50AqMUpx.json'}

exec(code, env_args)
