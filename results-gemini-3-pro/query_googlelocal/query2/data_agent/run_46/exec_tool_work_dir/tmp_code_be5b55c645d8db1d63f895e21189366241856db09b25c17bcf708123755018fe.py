code = """import json
import pandas as pd

businesses = locals()['var_function-call-11719054033594276390']
ratings = locals()['var_function-call-12138529831137689475']

df_bus = pd.DataFrame(businesses)
df_rate = pd.DataFrame(ratings)

# Ensure types match for merge
df_bus['gmap_id'] = df_bus['gmap_id'].astype(str)
df_rate['gmap_id'] = df_rate['gmap_id'].astype(str)

merged = pd.merge(df_bus, df_rate, on='gmap_id')
# Sort by rating desc
merged = merged.sort_values(by='avg_rating', ascending=False)

result = merged[['name', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4436743891636796731': [{'description': ' Located in Bakersfield, CA 93308, this service connects job seekers with local employers to facilitate meaningful career opportunities.', 'count': '1'}, {'description': ' This professional headquarters in McClellan Park, CA 95652, serves as a central hub for strategic operations and management activities.', 'count': '1'}, {'description': ' Offering a variety of dynamic workouts and wellness classes, this center in San Juan Capistrano, CA 92675, helps individuals achieve their health and fitness goals in a supportive community environment.', 'count': '1'}, {'description': ' Located in San Diego, CA 92108, this firm specializes in providing expert technical guidance and innovative solutions for complex engineering challenges.', 'count': '1'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'count': '1'}, {'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.', 'count': '1'}, {'description': ' This nurturing educational institution in Colfax, CA 95713, provides a strong foundation for early learners through engaging curriculum and supportive teachers.', 'count': '1'}, {'description': ' Providing expert HVAC services and solutions for optimal indoor climate control in Bakersfield, CA 93309.', 'count': '1'}, {'description': ' Located in Roseville, CA 95678, this upscale establishment offers a range of hair and skincare services to enhance your natural beauty and rejuvenate your look.', 'count': '1'}, {'description': ' Serving Riverside, CA 92503, this skilled provider specializes in comprehensive plumbing solutions, ensuring efficient repairs and installations for residential and commercial needs.', 'count': '1'}], 'var_function-call-11437792447531317383': [], 'var_function-call-2036910321229291493': [], 'var_function-call-3628240184388376667': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-11719054033594276390': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28'}], 'var_function-call-12138529831137689475': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
