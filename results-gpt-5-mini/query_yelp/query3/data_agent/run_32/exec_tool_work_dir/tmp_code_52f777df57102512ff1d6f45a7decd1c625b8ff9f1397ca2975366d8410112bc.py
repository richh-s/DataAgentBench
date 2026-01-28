code = """import json
# var_call_nJPVSDLBt2xmOBTHfBOQrpw9 contains the filepath to the full JSON result
with open(var_call_nJPVSDLBt2xmOBTHfBOQrpw9, 'r') as f:
    data = json.load(f)

# We'll map businessid_... to businessref_... for matching
business_ids = [d.get('business_id') for d in data]
# Extract attributes, normalize None to empty dict
results = []
for d in data:
    bid = d.get('business_id')
    attr = d.get('attributes') or {}
    # determine if bike parking exists
    bike = False
    if isinstance(attr, dict):
        bp = attr.get('BikeParking')
        if isinstance(bp, str):
            if bp.lower().strip().startswith("true"):
                bike = True
        elif isinstance(bp, bool):
            bike = bp
    # determine if any BusinessParking is present and indicates parking (lot/street/garage/valet/validated True)
    bizpark = False
    bpval = None
    if isinstance(attr, dict):
        bpval = attr.get('BusinessParking')
        if isinstance(bpval, str):
            s = bpval.lower()
            # simple checks for true keywords
            if "true" in s or "'lot': true" in s or "'street': true" in s or "'garage': true" in s or "lot': true" in s:
                bizpark = True
            # also if BusinessParking is 'None' explicitly then no
            if s.strip().startswith('none'):
                bizpark = False
        elif isinstance(bpval, dict):
            # if dict contains any True
            for v in bpval.values():
                if v is True:
                    bizpark = True
    results.append({'business_id': bid, 'bike_parking': bike, 'business_parking': bizpark, 'attributes': attr})

# Count businesses that have either bike_parking True or business_parking True
count = sum(1 for r in results if r['bike_parking'] or r['business_parking'])

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_R8Zq4nSI7alxOMhlzguYsi1z': ['checkin', 'business'], 'var_call_ikZyaopSDLNAJlhkhX8ZwtOs': ['review', 'tip', 'user'], 'var_call_1EQkFQTpvdrQceYTnzQ5CByu': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_nJPVSDLBt2xmOBTHfBOQrpw9': 'file_storage/call_nJPVSDLBt2xmOBTHfBOQrpw9.json'}

exec(code, env_args)
