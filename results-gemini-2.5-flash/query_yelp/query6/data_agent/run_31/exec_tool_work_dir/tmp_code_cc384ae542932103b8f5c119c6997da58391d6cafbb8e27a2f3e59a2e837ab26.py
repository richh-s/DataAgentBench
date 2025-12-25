code = """import pandas as pd

df = pd.DataFrame(locals()['var_function-call-1804990784370553280'])
df['average_rating'] = df['average_rating'].astype(float)
highest_rated_business = df.loc[df['average_rating'].idxmax()]
business_ref = highest_rated_business['business_ref']
business_id = business_ref.replace('businessref_', 'businessid_')

print('__RESULT__:')
print(business_id)"""

env_args = {'var_function-call-1804990784370553280': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}]}

exec(code, env_args)
