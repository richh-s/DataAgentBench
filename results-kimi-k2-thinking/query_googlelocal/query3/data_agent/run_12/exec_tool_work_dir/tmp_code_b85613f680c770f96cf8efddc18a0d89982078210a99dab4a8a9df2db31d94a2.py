code = """import json
import ast
from collections import defaultdict

businesses_file = locals()['var_functions.query_db:20']
reviews_file = locals()['var_functions.query_db:10']

with open(businesses_file, 'r') as f:
    businesses = json.load(f)

with open(reviews_file, 'r') as f:
    reviews = json.load(f)

def is_open_after_6pm(time_range):
    """Check if business is open after 6 PM based on time range string"""
    if time_range == "Open 24 hours":
        return True
    if time_range == "Closed":
        return False
    
    try:
        # Split on the actual dash character used in data
        if '\u2013' in time_range:
            parts = time_range.split('\u2013')
        elif '-' in time_range:
            parts = time_range.split('-')
        else:
            return False
        
        if len(parts) != 2:
            return False
        
        closing = parts[1].strip()
        
        # Handle various formats
        if 'PM' in closing.upper():
            closing_upper = closing.upper()
            
            # Extract hour
            hour_str = ''
            for char in closing_upper:
                if char.isdigit():
                    hour_str += char
                elif char == ':':
                    break
            
            if not hour_str:
                return False
                
            hour = int(hour_str)
            
            # Check for times after 6 PM
            if hour > 6 and hour < 12:
                return True
            elif hour == 12 and '12:' in closing_upper and '12:00' not in closing_upper:
                # Could be 12:xx PM which is noon
                return False
            elif hour == 6:
                # Check if it's after 6:00 (e.g., 6:30PM)
                if ':' in closing:
                    minute_part = closing.split(':')[1]
                    minute_digits = ''
                    for char in minute_part:
                        if char.isdigit():
                            minute_digits += char
                        else:
                            break
                    if minute_digits and int(minute_digits) > 0:
                        return True
                return False
        
        return False
    except:
        return False

# Calculate average ratings
business_ratings = defaultdict(list)
for r in reviews:
    gid = r['gmap_id']
    rating = int(r['rating'])
    business_ratings[gid].append(rating)

avg_ratings = {}
for gid, ratings in business_ratings.items():
    avg_ratings[gid] = {
        'avg': sum(ratings) / len(ratings),
        'count': len(ratings)
    }

# Check businesses with valid hours
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
valid = []

for b in businesses:
    gid = b['gmap_id']
    name = b['name']
    hours_str = b.get('hours', '')
    
    if not hours_str or hours_str == 'None':
        continue
    
    try:
        hours_list = ast.literal_eval(hours_str)
        
        for day_entry in hours_list:
            if len(day_entry) != 2:
                continue
            
            day_name, time_range = day_entry
            if day_name in weekdays and is_open_after_6pm(time_range):
                if gid in avg_ratings:
                    valid.append({
                        'gmap_id': gid,
                        'name': name,
                        'hours': hours_str,
                        'avg_rating': avg_ratings[gid]['avg'],
                        'review_count': avg_ratings[gid]['count']
                    })
                break
    except:
        continue

# Sort by rating and get top 5
valid.sort(key=lambda x: x['avg_rating'], reverse=True)
top5 = valid[:5]

results = []
for b in top5:
    results.append({
        'name': b['name'],
        'operating_hours': b['hours'],
        'average_rating': round(b['avg_rating'], 2),
        'review_count': b['review_count']
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'hours': 'None', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'gmap_id': 'gmap_44'}, {'gmap_id': 'gmap_41'}, {'gmap_id': 'gmap_43'}, {'gmap_id': 'gmap_38'}, {'gmap_id': 'gmap_45'}, {'gmap_id': 'gmap_74'}, {'gmap_id': 'gmap_17'}, {'gmap_id': 'gmap_22'}, {'gmap_id': 'gmap_29'}, {'gmap_id': 'gmap_25'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'businesses_count': 66, 'reviews_count': 2000}, 'var_functions.execute_python:18': [{'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'avg_rating': 5.0, 'review_count': 18}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'avg_rating': 5.0, 'review_count': 8}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'avg_rating': 5.0, 'review_count': 2}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'avg_rating': 5.0, 'review_count': 2}, {'gmap_id': 'gmap_9', 'name': 'Mariscos el poblano', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]', 'avg_rating': 5.0, 'review_count': 3}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': [{'name': 'Mariscos el poblano', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]', 'avg_rating': 5.0, 'review_count': 3}, {'name': 'Regus - California, Irvine - Oracle Tower', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]', 'avg_rating': 4.44, 'review_count': 16}, {'name': 'Mobile Moreno Valley Dispensary', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]', 'avg_rating': 1.0, 'review_count': 3}]}

exec(code, env_args)
