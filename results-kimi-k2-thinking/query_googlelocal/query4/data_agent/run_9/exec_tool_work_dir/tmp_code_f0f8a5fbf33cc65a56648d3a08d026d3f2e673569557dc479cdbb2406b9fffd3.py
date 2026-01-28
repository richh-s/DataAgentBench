code = """# Load results from previous queries
import json

# Results from query_db calls
review_counts = [{"gmap_id": "gmap_20", "high_rating_count": "8"}, {"gmap_id": "gmap_53", "high_rating_count": "7"}, {"gmap_id": "gmap_40", "high_rating_count": "6"}]
business_names = [{"name": "Aurora Massage", "gmap_id": "gmap_20"}, {"name": "The Boochyard @ Local Roots", "gmap_id": "gmap_53"}, {"name": "Widows Peak Salon", "gmap_id": "gmap_40"}]

# Create dictionaries for easier lookup
review_dict = {}
for item in review_counts:
    review_dict[item["gmap_id"]] = int(item["high_rating_count"])

name_dict = {}
for item in business_names:
    name_dict[item["gmap_id"]] = item["name"]

# Create the final result list
result_list = []
for gmap_id in review_dict:
    business_name = name_dict.get(gmap_id, "Unknown")
    count = review_dict[gmap_id]
    result_list.append({"business_name": business_name, "high_rating_reviews_count": count})

# Sort by count descending
sorted_results = sorted(result_list, key=lambda x: x["high_rating_reviews_count"], reverse=True)

# Create a simple result string
result_parts = []
result_parts.append("Aurora Massage: 8 high-rating reviews")
result_parts.append("The Boochyard @ Local Roots: 7 high-rating reviews")  
result_parts.append("Widows Peak Salon: 6 high-rating reviews")

result_str = "\n".join(result_parts)

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_functions.query_db:6': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
