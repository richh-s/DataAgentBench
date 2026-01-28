code = """import json
fp = var_call_KV6QvwPN7haclmsNoobLPPeq
with open(fp,'r') as f:
    data = json.load(f)

# Extract business_ref and categories from description
biz_to_cats = {}
for rec in data:
    bid = rec.get('business_id')
    bref = bid.replace('businessid_', 'businessref_')
    desc = rec.get('description') or ''
    # Find the part after "category of '...'", or look for 'in the category of'
    cats = []
    if "category of" in desc:
        # try to extract substring after "category of"
        try:
            part = desc.split("category of",1)[1]
            # strip punctuation
            part = part.strip().strip('.').strip()
            # remove surrounding quotes if present
            part = part.strip()
            # split by commas
            cats = [c.strip().strip("'") for c in part.split(',') if c.strip()]
        except Exception:
            cats = []
    else:
        # try to extract categories by splitting on 'offers a range of services in'
        if "offers a range of services in" in desc:
            part = desc.split("offers a range of services in",1)[1]
            part = part.strip().strip('.')
            cats = [c.strip().strip("'") for c in part.split(',') if c.strip()]
        elif "offers a diverse range of services" in desc:
            part = desc.split("offers a diverse range of services in the fields of",1)[1] if "offers a diverse range of services in the fields of" in desc else desc
            part = part.strip().strip('.')
            cats = [c.strip().strip("'") for c in part.split(',') if c.strip()]
        else:
            # fallback: try to get text between 'in the categories of' and '.'
            if 'in the categories of' in desc:
                part = desc.split('in the categories of',1)[1].split('.',1)[0]
                cats = [c.strip().strip("'") for c in part.split(',') if c.strip()]
    biz_to_cats[bref]=cats

print('__RESULT__:')
print(json.dumps(biz_to_cats))"""

env_args = {'var_call_LobF8jjX5IiHLMNao3tSLznC': ['business', 'checkin'], 'var_call_OrnNU9ZV8xUaiyij8J5RX1O1': ['review', 'tip', 'user'], 'var_call_8sPXPQmnDjxWuVFFLvf712sa': 'file_storage/call_8sPXPQmnDjxWuVFFLvf712sa.json', 'var_call_IgvP8VbGkFQXGvNQHbO8ipmQ': 'file_storage/call_IgvP8VbGkFQXGvNQHbO8ipmQ.json', 'var_call_fC40ymA3nKMGxxAB5LmNhIuh': {'business_refs': ['businessref_49', 'businessref_47', 'businessref_88', 'businessref_33', 'businessref_92', 'businessref_64', 'businessref_52', 'businessref_29', 'businessref_10', 'businessref_61', 'businessref_54', 'businessref_8', 'businessref_91', 'businessref_83', 'businessref_93', 'businessref_24', 'businessref_95', 'businessref_26', 'businessref_84', 'businessref_89', 'businessref_32', 'businessref_71', 'businessref_97', 'businessref_14', 'businessref_3', 'businessref_27', 'businessref_75', 'businessref_2', 'businessref_48', 'businessref_67', 'businessref_76', 'businessref_100', 'businessref_63', 'businessref_45', 'businessref_68', 'businessref_6', 'businessref_87', 'businessref_66', 'businessref_55', 'businessref_30', 'businessref_15', 'businessref_96', 'businessref_11', 'businessref_73', 'businessref_4', 'businessref_77', 'businessref_18', 'businessref_65', 'businessref_86', 'businessref_53', 'businessref_40', 'businessref_44', 'businessref_43', 'businessref_9', 'businessref_20', 'businessref_37', 'businessref_62', 'businessref_94', 'businessref_90', 'businessref_31', 'businessref_85', 'businessref_25', 'businessref_82', 'businessref_58', 'businessref_60', 'businessref_21', 'businessref_98', 'businessref_16', 'businessref_46', 'businessref_22', 'businessref_36', 'businessref_38', 'businessref_81', 'businessref_13', 'businessref_17'], 'biz_to_cats': {'businessref_49': [], 'businessref_47': [], 'businessref_88': [], 'businessref_33': [], 'businessref_92': [], 'businessref_64': [], 'businessref_52': [], 'businessref_29': [], 'businessref_10': [], 'businessref_61': [], 'businessref_54': [], 'businessref_8': [], 'businessref_91': [], 'businessref_83': [], 'businessref_93': [], 'businessref_24': [], 'businessref_95': [], 'businessref_26': [], 'businessref_84': [], 'businessref_89': [], 'businessref_32': [], 'businessref_71': [], 'businessref_97': [], 'businessref_14': [], 'businessref_3': [], 'businessref_27': [], 'businessref_75': [], 'businessref_2': [], 'businessref_48': [], 'businessref_67': [], 'businessref_76': [], 'businessref_100': [], 'businessref_63': [], 'businessref_45': [], 'businessref_68': [], 'businessref_6': [], 'businessref_87': [], 'businessref_66': [], 'businessref_55': [], 'businessref_30': [], 'businessref_15': [], 'businessref_96': [], 'businessref_11': [], 'businessref_73': [], 'businessref_4': [], 'businessref_77': [], 'businessref_18': [], 'businessref_65': [], 'businessref_86': [], 'businessref_53': [], 'businessref_40': [], 'businessref_44': [], 'businessref_43': [], 'businessref_9': [], 'businessref_20': [], 'businessref_37': [], 'businessref_62': [], 'businessref_94': [], 'businessref_90': [], 'businessref_31': [], 'businessref_85': [], 'businessref_25': [], 'businessref_82': [], 'businessref_58': [], 'businessref_60': [], 'businessref_21': [], 'businessref_98': [], 'businessref_16': [], 'businessref_46': [], 'businessref_22': [], 'businessref_36': [], 'businessref_38': [], 'businessref_81': [], 'businessref_13': [], 'businessref_17': []}}, 'var_call_a2OOwGbS9NVgCN6iyNgCe0qT': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_O4ZJOZXEZF7SlC5cMBzkFPbh': [], 'var_call_fMynhAEeOIvtBZe9zPgNjtJd': [{'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'review_count': '20', 'is_open': '1', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'hours': 'None', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_call_KV6QvwPN7haclmsNoobLPPeq': 'file_storage/call_KV6QvwPN7haclmsNoobLPPeq.json'}

exec(code, env_args)
