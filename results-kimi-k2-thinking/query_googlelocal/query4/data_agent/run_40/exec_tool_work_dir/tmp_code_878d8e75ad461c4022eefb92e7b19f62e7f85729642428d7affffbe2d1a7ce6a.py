code = """import json
import re
from datetime import datetime
from collections import defaultdict

# Load review data - access using locals() due to special character in variable name
review_var = 'var_functions.query_db:8'
review_file_path = locals()[review_var]

with open(review_file_path, 'r') as f:
    reviews = json.load(f)

# Load business data
businesses = locals()['var_functions.query_db:10']

# Create a dictionary for business names
business_dict = {b['gmap_id']: b['name'] for b in businesses}

# Function to extract year from time string
def extract_year(time_str):
    if not time_str:
        return None
    
    # Try different patterns
    patterns = [
        r'(\d{4})-\d{2}-\d{2}',  # YYYY-MM-DD
        r'(\d{4})',  # Any 4-digit year
    ]
    
    for pattern in patterns:
        match = re.search(pattern, time_str)
        if match:
            try:
                return int(match.group(1))
            except:
                continue
    
    return None

# Filter reviews from 2019 with rating >= 4.5
high_rating_2019 = []
for review in reviews:
    year = extract_year(review.get('time', ''))
    rating = float(review.get('rating', 0))
    
    if year == 2019 and rating >= 4.5:
        high_rating_2019.append({
            'gmap_id': review['gmap_id'],
            'rating': rating,
            'time': review['time']
        })

# Group by business and count
business_counts = defaultdict(int)
for review in high_rating_2019:
    business_counts[review['gmap_id']] += 1

# Get top 3 businesses
top_3 = sorted(business_counts.items(), key=lambda x: x[1], reverse=True)[:3]

# Format result
result = []
for gmap_id, count in top_3:
    business_name = business_dict.get(gmap_id, 'Unknown')
    result.append({
        'business_name': business_name,
        'high_rating_review_count': count,
        'gmap_id': gmap_id
    })

# Print result
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'rating': '5', 'time': 'September 03, 2020 at 04:15 PM', 'gmap_id': 'gmap_44'}, {'rating': '5', 'time': '2021-04-12 17:07:52', 'gmap_id': 'gmap_44'}, {'rating': '5', 'time': '2018-04-23 16:24:26', 'gmap_id': 'gmap_44'}, {'rating': '5', 'time': '2017-07-10 22:12:19', 'gmap_id': 'gmap_44'}, {'rating': '3', 'time': 'May 19, 2021 at 03:55 AM', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:7': [{'name': 'City Textile', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'name': 'City Textile', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25'}, {'name': 'PODS Sacramento Hub', 'gmap_id': 'gmap_19'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'J B Oriental Inc', 'gmap_id': 'gmap_32'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21'}, {'name': 'State Street/7th Street', 'gmap_id': 'gmap_48'}, {'name': 'HDR', 'gmap_id': 'gmap_50'}, {'name': 'Porvene Doors', 'gmap_id': 'gmap_18'}, {'name': 'Hanford Auto Supply', 'gmap_id': 'gmap_16'}, {'name': "Jeff's Auto Repair", 'gmap_id': 'gmap_26'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28'}, {'name': 'Tax Deferred Solutions (TDS Group, INC)', 'gmap_id': 'gmap_23'}, {'name': 'Origin Church', 'gmap_id': 'gmap_31'}, {'name': 'Colfax Elementary School', 'gmap_id': 'gmap_27'}, {'name': 'Life Pointe Church', 'gmap_id': 'gmap_2'}, {'name': 'The Beauty Bar', 'gmap_id': 'gmap_30'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': "Zuby's Brake Tires & Wheels", 'gmap_id': 'gmap_72'}, {'name': 'Regus - California, Irvine - Oracle Tower', 'gmap_id': 'gmap_63'}, {'name': 'Fitness Machine Technicians', 'gmap_id': 'gmap_52'}, {'name': 'J & T Plumbing Pros', 'gmap_id': 'gmap_56'}, {'name': 'Excel Hair & Nails', 'gmap_id': 'gmap_65'}, {'name': 'Birdi Systems, Inc.', 'gmap_id': 'gmap_37'}, {'name': 'Taba Rug Gallery', 'gmap_id': 'gmap_51'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39'}, {'name': 'Beauty Divine Artistry', 'gmap_id': 'gmap_36'}, {'name': 'IBEW 441', 'gmap_id': 'gmap_59'}, {'name': "Ely's Beauty Salon", 'gmap_id': 'gmap_57'}, {'name': 'United Methodist Church', 'gmap_id': 'gmap_13'}, {'name': 'Dirk Vermeulen - State Farm Insurance Agent', 'gmap_id': 'gmap_15'}, {'name': 'White Barn Candle Co', 'gmap_id': 'gmap_12'}, {'name': "Teter's Oakdale Jewelry", 'gmap_id': 'gmap_14'}, {'name': 'Timmons Auto & Truck Repair', 'gmap_id': 'gmap_3'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'gmap_id': 'gmap_35'}, {'name': 'Lafayette Entrance 1', 'gmap_id': 'gmap_4'}, {'name': 'ATSI', 'gmap_id': 'gmap_6'}, {'name': "Rossy's Beauty Salon", 'gmap_id': 'gmap_7'}, {'name': 'TACOS LA CABANA', 'gmap_id': 'gmap_8'}, {'name': 'Jjironwork', 'gmap_id': 'gmap_10'}, {'name': 'Mariscos el poblano', 'gmap_id': 'gmap_9'}, {'name': 'Climate Control', 'gmap_id': 'gmap_77'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42'}, {'name': 'Avani Staffing Solutions', 'gmap_id': 'gmap_78'}, {'name': 'CrossFit to the Core', 'gmap_id': 'gmap_70'}, {'name': 'Dr. Syverain Skincare Clinic', 'gmap_id': 'gmap_5'}, {'name': "Ruby's Boutique", 'gmap_id': 'gmap_34'}, {'name': 'Paradise tattoo', 'gmap_id': 'gmap_11'}, {'name': 'Full Circle Trading Post', 'gmap_id': 'gmap_0'}, {'name': 'Northern Builders Supply', 'gmap_id': 'gmap_1'}, {'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin', 'gmap_id': 'gmap_62'}, {'name': 'Off The Hoof', 'gmap_id': 'gmap_61'}, {'name': 'Weatherline Reroofing & Repairs', 'gmap_id': 'gmap_58'}, {'name': 'HIGHPOINTE', 'gmap_id': 'gmap_66'}, {'name': 'B2Sign, Inc.', 'gmap_id': 'gmap_46'}, {'name': 'Laptop Masters', 'gmap_id': 'gmap_47'}, {'name': 'HAVEN™ Dispensary', 'gmap_id': 'gmap_75'}, {'name': 'IronStep', 'gmap_id': 'gmap_76'}, {'name': 'CYD Works Electric', 'gmap_id': 'gmap_73'}, {'name': 'Mobile Moreno Valley Dispensary', 'gmap_id': 'gmap_55'}, {'name': 'Wildomar Campground', 'gmap_id': 'gmap_54'}, {'name': 'Advanced Auto Upholstery', 'gmap_id': 'gmap_68'}, {'name': 'AMMCOR Management Company, Inc.', 'gmap_id': 'gmap_71'}, {'name': 'LuXe Organic Nails Boutique', 'gmap_id': 'gmap_67'}, {'name': 'Taitz Orly DDS', 'gmap_id': 'gmap_69'}, {'name': 'St John Knits International Inc', 'gmap_id': 'gmap_64'}, {'name': 'NEX Barbershop', 'gmap_id': 'gmap_49'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}, {'name': 'The Dream Junction', 'gmap_id': 'gmap_60'}]}

exec(code, env_args)
