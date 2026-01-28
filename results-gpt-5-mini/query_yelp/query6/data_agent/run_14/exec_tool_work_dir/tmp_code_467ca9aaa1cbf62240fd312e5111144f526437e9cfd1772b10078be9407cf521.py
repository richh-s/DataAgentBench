code = """import json
import re
# Access previous query results from storage variables
res_reviews = var_call_KJnwAgvcGTICSq34nqQyCD7O
res_business = var_call_y7RfqwDx8oeD7P0M9jvmrbmw

if not res_reviews:
    result = {"error": "No review data found"}
else:
    r = res_reviews[0]
    b = res_business[0] if res_business else {}
    business_id = r.get('business_id')
    try:
        avg_rating = float(r.get('avg_rating'))
    except:
        avg_rating = None
    try:
        review_count = int(r.get('review_count'))
    except:
        review_count = None
    name = b.get('name')
    description = b.get('description','')

    # Extract categories from description using regex
    cats = []
    m = re.search(r'featuring\s+(.*?)(?:,?\s*(?:perfect|ideal)|\.)', description, re.IGNORECASE)
    if m:
        cats_str = m.group(1)
    else:
        idx = description.lower().find('featuring ')
        if idx != -1:
            cats_str = description[idx+len('featuring '):]
        else:
            cats_str = ''
    if cats_str:
        cats = [c.strip() for c in re.split(r',\s*', cats_str) if c.strip()]

    result = {
        "business_id": business_id,
        "name": name,
        "categories": cats,
        "avg_rating": avg_rating,
        "review_count": review_count,
        "rating_period_start": "2016-01-01",
        "rating_period_end": "2016-06-30"
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KJnwAgvcGTICSq34nqQyCD7O': [{'business_id': 'businessid_9', 'review_count': '5', 'avg_rating': '4.0'}], 'var_call_y7RfqwDx8oeD7P0M9jvmrbmw': [{'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
