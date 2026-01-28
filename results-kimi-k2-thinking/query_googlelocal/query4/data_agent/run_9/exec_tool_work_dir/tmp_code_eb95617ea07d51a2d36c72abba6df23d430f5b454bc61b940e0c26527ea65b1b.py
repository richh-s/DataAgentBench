code = """# Load results from previous queries
import json

# Results from query_db calls (passed as variables from storage)
review_counts = [{"gmap_id": "gmap_20", "high_rating_count": "8"}, {"gmap_id": "gmap_53", "high_rating_count": "7"}, {"gmap_id": "gmap_40", "high_rating_count": "6"}]
business_names = [{"name": "Aurora Massage", "gmap_id": "gmap_20"}, {"name": "The Boochyard @ Local Roots", "gmap_id": "gmap_53"}, {"name": "Widows Peak Salon", "gmap_id": "gmap_40"}]

# Create dictionaries for easier lookup
review_dict = {item['gmap_id']: int(item['high_rating_count']) for item in review_counts}
name_dict = {item['gmap_id']: item['name'] for item in business_names}

# Create the final result list
result_list = []
for gmap_id in review_dict:
    result_list.append({
        'business_name': name_dict.get(gmap_id, 'Unknown'),
        'high_rating_reviews_count': review_dict[gmap_id]
    })

# Sort by count descending to maintain ranking
result_list = sorted(result_list, key=lambda x: x['high_rating_reviews_count'], reverse=True)

# Format output for final answer
output_lines = []
for i, item in enumerate(result_list, 1):
    output_lines.append(f"{i}. {item['business_name']}: {item['high_rating_reviews_count']} high-rating reviews")
    
final_output = "\\n".join(output_lines)

print('__RESULT__:')
print(final_output)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_functions.query_db:6': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
