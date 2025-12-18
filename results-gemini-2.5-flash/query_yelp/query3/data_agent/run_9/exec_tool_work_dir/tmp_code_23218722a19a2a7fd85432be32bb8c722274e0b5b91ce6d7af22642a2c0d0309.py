code = """import json

business_refs_2018 = locals()['var_function-call-9799307240642270063']
business_ids_2018 = [d['business_ref'].replace('businessref_', 'businessid_') for d in business_refs_2018]

# Constructing the MongoDB query for businesses with parking attributes
mongo_filter = {
    "business_id": {"$in": business_ids_2018},
    "$or": [
        {"attributes.BusinessParking": {"$ne": None}},
        {"attributes.BikeParking": {"$ne": None}}
    ]
}

mongo_query = {
    "collection": "business",
    "filter": mongo_filter,
    "projection": {"business_id": 1}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-9799307240642270063': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}]}

exec(code, env_args)
