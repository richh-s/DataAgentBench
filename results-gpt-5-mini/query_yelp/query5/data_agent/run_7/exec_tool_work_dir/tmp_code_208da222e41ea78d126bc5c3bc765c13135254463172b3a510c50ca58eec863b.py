code = """import json

# Load previous results
res = var_call_cMTaokgnWHpRsRUA1eBOFr1B
ratings = var_call_4tK8IjHFYbbLgRU80IBT8BtF

# Convert avg_rating and counts to numeric and compute weighted/unweighted averages
total_reviews = 0
weighted_sum = 0.0
sum_avgs = 0.0
n_businesses = 0
per_business = {}
for r in ratings:
    br = r['business_ref']
    avg = float(r['avg_rating'])
    count = int(r['review_count'])
    per_business[br] = {'avg': avg, 'count': count}
    total_reviews += count
    weighted_sum += avg * count
    sum_avgs += avg
    n_businesses += 1

if n_businesses>0:
    overall_avg_weighted = weighted_sum/total_reviews
    overall_avg_unweighted = sum_avgs/n_businesses
else:
    overall_avg_weighted = None
    overall_avg_unweighted = None

out = {
    'state': res['top_state'],
    'business_count': res['count'],
    'business_refs': res['business_refs'],
    'per_business': per_business,
    'average_rating_weighted_by_reviews': overall_avg_weighted,
    'average_rating_unweighted': overall_avg_unweighted
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1o2zFCOf1hHTSbMhk4XAjGii': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'name': '7-Eleven', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_call_3n7CuaG7JdRRHiQckUQOKYDh': 'file_storage/call_3n7CuaG7JdRRHiQckUQOKYDh.json', 'var_call_cMTaokgnWHpRsRUA1eBOFr1B': {'top_state': 'PA', 'count': 8, 'business_ids': ['businessid_89', 'businessid_97', 'businessid_67', 'businessid_77', 'businessid_86', 'businessid_40', 'businessid_44', 'businessid_82'], 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82']}, 'var_call_4tK8IjHFYbbLgRU80IBT8BtF': [{'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'review_count': '42'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'review_count': '46'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'review_count': '25'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'review_count': '46'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'review_count': '17'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'review_count': '42'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'review_count': '42'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'review_count': '21'}]}

exec(code, env_args)
