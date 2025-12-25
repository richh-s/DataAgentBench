code = """import pandas as pd

business_with_parking = locals()['var_function-call-10646893983038338241']
df_business_with_parking = pd.DataFrame(business_with_parking)

# Some 'attributes.BusinessParking' can be 'None' string, we need to treat them as null
# Also check if the actual parking value indicates parking available, since some parking attribute fields may be present but contain only False values or None.
df_business_with_parking_filtered = df_business_with_parking[
    (
        df_business_with_parking['attributes'].apply(lambda x: x.get('BusinessParking') is not None and x.get('BusinessParking') != 'None' and (
            'True' in x.get('BusinessParking') if isinstance(x.get('BusinessParking'), str) else True
        ))
    ) | (
        df_business_with_parking['attributes'].apply(lambda x: x.get('BikeParking') == 'True')
    )
]

count = len(df_business_with_parking_filtered['business_id'].unique())

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-10541306311981934869': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_function-call-9158911077237227672': ['businessid_13', 'businessid_79', 'businessid_91', 'businessid_46', 'businessid_47', 'businessid_73', 'businessid_66', 'businessid_25', 'businessid_59', 'businessid_67', 'businessid_15', 'businessid_24', 'businessid_36', 'businessid_17', 'businessid_43', 'businessid_99', 'businessid_80', 'businessid_40', 'businessid_83', 'businessid_86', 'businessid_62', 'businessid_8', 'businessid_57', 'businessid_37', 'businessid_26', 'businessid_4', 'businessid_68', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_77', 'businessid_27', 'businessid_20', 'businessid_22', 'businessid_14', 'businessid_28'], 'var_function-call-10646893983038338241': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'attributes': {'BusinessParking': 'None'}}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'attributes': {'BikeParking': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}"}}]}

exec(code, env_args)
