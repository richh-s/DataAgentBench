code = """import json
from collections import defaultdict

# Load metadata and articles from storage paths or variables
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

metadata = load_var(var_call_FptZsboUs5IwWU1JjmsLWqRS)
articles = load_var(var_call_cM4oOZaZME2cOvhSbQpurik5)

# Build articles map by article_id (int)
art_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except Exception:
        continue
    art_map[aid] = a

# Prepare keyword list for Business category
keywords = [
    'economy','economic','economics','eurozone','market','markets','stock','stocks','share','shares',
    'bank','banks','company','companies','firm','firms','business','invest','investment','ipo',
    'merger','acquisition','profit','loss','finance','financial','trade','inflation','interest rate','interest rates',
    'oil prices','oil price','oil','revenue','earnings','unemployment','gdp'
]

# Function to classify as business if any keyword in title or description
def is_business(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    for kw in keywords:
        if kw in text:
            return True
    return False

# Count business articles per year from 2010 to 2020
counts = {str(y): 0 for y in range(2010, 2021)}
missing_articles = 0
for rec in metadata:
    try:
        aid = int(rec.get('article_id'))
        pub = rec.get('publication_date')
        year = None
        if pub and len(pub) >= 4:
            year = pub[:4]
    except Exception:
        continue
    if year is None or year not in counts:
        continue
    art = art_map.get(aid)
    if not art:
        missing_articles += 1
        continue
    title = art.get('title','')
    desc = art.get('description','')
    if is_business(title, desc):
        counts[year] += 1

total = sum(counts.values())
average = total / len(counts) if counts else 0

result = {
    'counts_by_year': counts,
    'total_business_articles_2010_2020': total,
    'average_business_articles_per_year_2010_2020': average,
    'notes': {
        'classification_method': 'keyword-based on title and description',
        'num_metadata_records': len(metadata),
        'num_articles_in_articles_collection': len(articles),
        'num_missing_article_documents': missing_articles
    }
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FptZsboUs5IwWU1JjmsLWqRS': 'file_storage/call_FptZsboUs5IwWU1JjmsLWqRS.json', 'var_call_HBBdA6FPdUWa5BCoHOOdtJQd': 'file_storage/call_HBBdA6FPdUWa5BCoHOOdtJQd.json', 'var_call_bV13hOg4wYXHErfZMCC2zTQT': 'file_storage/call_bV13hOg4wYXHErfZMCC2zTQT.json', 'var_call_hKfnU591hnamZsiGUwzUNZm8': {'num_queries': 15, 'first_query_prefix': '{"collection": "articles", "filter": {"article_id": {"$in": [3, 9, 13, 14, 21, 27, 43, 60, 62, 63, 64, 66, 78, 128, 140, 142, 143, 144, 151, 154, 164, 179, 181, 190, 201, 202, 203, 210, 214, 216, 223, 243, 257, 265, 268, 270, 271, 279, 298, 300, 309, 328, 336, 338, 339, 348, 371, 379, 383, 394, 398, 400, 429, 439, 446, 452, 456, 457, 460, 474, 482, 484, 485, 502, 509, 510, 514, 532, 534, 536, 539, 554, 557, 564, 567, 569, 572, 576, 584, 597, 624, 642, 647, 661, 663, 669, 678, 682, 697, 712, 717, 756, 763, 768, 774, 782, 793, 805, 810, 846, 865, 879, 919, 935, 940, 974, 982, 984, 987, 990, 993, 999, 1001, 1003, 1014, 1030, 1045, 1054, 1061, 1101, 1103, 1108, 1129, 1135, 1140, 1144, 1148, 1168, 1182, 1190, 1193, 1208, 1229, 1244, 1265, 1284, 1289, 1310, 1323, 1327, 1333, 1334, 1337, 1343, 1362, 1377, 1378, 1380, 1386, 1391, 1406, 1412, 1416, 1422, 1439, 1441, 1450, 1462, 1495, 1510, 1529, 1536, 1541, 1549, 1551, 1565, 1567, 1570, 1572, 1581, 1594, 1600, 1609, 1611, 1627, 1635, 1642, 1646', 'second_query_prefix': '{"collection": "articles", "filter": {"article_id": {"$in": [9063, 9072, 9074, 9084, 9095, 9098, 9100, 9107, 9115, 9118, 9130, 9138, 9161, 9163, 9164, 9165, 9185, 9197, 9198, 9206, 9207, 9210, 9211, 9213, 9222, 9233, 9236, 9238, 9251, 9255, 9261, 9268, 9281, 9298, 9317, 9325, 9330, 9331, 9333, 9360, 9372, 9402, 9409, 9415, 9418, 9420, 9423, 9427, 9436, 9457, 9482, 9483, 9485, 9507, 9509, 9513, 9515, 9531, 9540, 9542, 9551, 9554, 9563, 9570, 9576, 9584, 9587, 9593, 9594, 9596, 9600, 9603, 9619, 9630, 9639, 9644, 9653, 9658, 9673, 9685, 9689, 9690, 9695, 9699, 9727, 9731, 9745, 9746, 9751, 9786, 9795, 9817, 9828, 9838, 9845, 9848, 9853, 9855, 9872, 9898, 9925, 9928, 9933, 9952, 9953, 9971, 9972, 9981, 9983, 10009, 10026, 10037, 10042, 10055, 10065, 10066, 10072, 10083, 10092, 10093, 10106, 10124, 10127, 10139, 10156, 10159, 10178, 10186, 10187, 10210, 10214, 10227, 10231, 10238, 10250, 10252, 10257, 10261, 10274, 10282, 10299, 10306, 10310, 10312, 10321, 10322, 10324, 10331, 10347, 10348'}, 'var_call_cM4oOZaZME2cOvhSbQpurik5': 'file_storage/call_cM4oOZaZME2cOvhSbQpurik5.json'}

exec(code, env_args)
