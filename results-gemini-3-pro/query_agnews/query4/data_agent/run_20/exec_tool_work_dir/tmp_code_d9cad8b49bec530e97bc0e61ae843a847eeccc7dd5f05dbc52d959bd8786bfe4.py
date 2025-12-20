code = """import json
import collections
import re
import os

# Load counts
if os.path.exists('counts.json'):
    with open('counts.json', 'r') as f:
        counts = json.load(f)
else:
    counts = {}

# Load 2015 metadata (ids map)
with open(locals()['var_function-call-121859605526448438'], 'r') as f:
    meta_list = json.load(f)
meta_map = {str(item['article_id']): item['region'] for item in meta_list}
ids_2015 = set(meta_map.keys())

# Load Batch 2 articles
batch_file = locals()['var_function-call-3337357360678412435']
with open(batch_file, 'r') as f:
    articles_list = json.load(f)

# Keywords
categories = {
    "Business": ["market", "stock", "dow", "nasdaq", "nyse", "wall street", "share", "profit", "earning", "revenue", "dividend", "quarter", "analyst", "economy", "economic", "bank", "fed", "rate", "dollar", "euro", "yen", "currency", "trade", "deal", "merger", "acquisition", "company", "corp", "inc", "ltd", "ceo", "cfo", "business", "industry", "sector", "oil", "gas", "price", "crude", "barrel", "investor", "sales", "hedge", "fund"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "net", "google", "apple", "microsoft", "ibm", "intel", "linux", "windows", "server", "mobile", "phone", "cell", "wireless", "network", "satellite", "space", "nasa", "astronomer", "galaxy", "planet", "mars", "biology", "physics", "chemistry", "study", "research", "cancer", "disease", "virus", "flu", "health", "medical", "drug", "gene", "genome", "gadget", "device", "browser", "spam", "hacker", "robot"],
    "Sports": ["sport", "game", "match", "team", "player", "coach", "manager", "win", "won", "lose", "lost", "draw", "score", "goal", "point", "cup", "trophy", "medal", "olympic", "champion", "league", "tournament", "season", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby", "racing", "f1", "nascar", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "stadium"],
    "World": ["world", "international", "nation", "country", "state", "government", "parliament", "congress", "senate", "election", "vote", "poll", "candidate", "president", "prime minister", "minister", "official", "leader", "dictator", "king", "queen", "prince", "pope", "vatican", "police", "military", "army", "navy", "air force", "soldier", "troop", "rebel", "guerrilla", "terrorist", "terrorism", "attack", "bomb", "blast", "explosion", "kill", "dead", "injure", "casualty", "victim", "war", "peace", "conflict", "fight", "battle", "truce", "treaty", "accord", "agreement", "summit", "talk", "negotiation", "diplomacy", "foreign", "ambassador", "un", "united nations", "security council", "nato", "eu", "european union", "commission", "court", "trial", "judge", "prison", "jail", "hostage", "kidnap", "protest", "strike", "riot", "demonstrate", "disaster", "quake", "flood", "storm", "hurricane", "typhoon", "crash", "accident", "iraq", "iran", "syria", "israel", "palestin", "gaza", "lebanon", "egypt", "libya", "sudan", "darfur", "africa", "asia", "europe", "russia", "china", "japan", "korea", "afghanistan", "pakistan", "india", "baghdad", "tehran", "kabul", "moscow", "beijing", "ukraine", "putin", "obama", "bush", "clinton", "yasser", "arafat", "sharon", "premier", "chancellor"]
}

count_processed = 0
count_world = 0

for article in articles_list:
    aid = str(article.get('article_id', ''))
    if aid in ids_2015:
        count_processed += 1
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        scores = {cat: 0 for cat in categories}
        words = re.findall(r'\w+', text)
        
        for word in words:
            for cat, kws in categories.items():
                if word in kws:
                    scores[cat] += 1
        
        for cat, kws in categories.items():
            for kw in kws:
                if " " in kw and kw in text:
                     scores[cat] += 1
        
        best_cat = max(scores, key=scores.get)
        if scores[best_cat] > 0:
            assigned_cat = best_cat
        else:
            assigned_cat = "Unknown"
        
        if assigned_cat == "World":
            reg = meta_map[aid]
            counts[reg] = counts.get(reg, 0) + 1
            count_world += 1

with open('counts.json', 'w') as f:
    json.dump(counts, f)

print("__RESULT__:")
print(json.dumps({"processed_in_batch": count_processed, "world_found": count_world, "total_counts": counts}))"""

env_args = {'var_function-call-121859605526448438': 'file_storage/function-call-121859605526448438.json', 'var_function-call-951208037007644572': 'file_storage/function-call-951208037007644572.json', 'var_function-call-8352185799025476041': [{'count(*)': '127600'}], 'var_function-call-6206586464072558012': 47788, 'var_function-call-12195274356503434995': {'min': 13, 'max': 127570}, 'var_function-call-16754112173434574181': 'file_storage/function-call-16754112173434574181.json', 'var_function-call-9929434618377718204': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7583640517852942502': {'max_region': 'None', 'count': 0, 'all_counts': {}}, 'var_function-call-2917885648773578921': 5, 'var_function-call-11927292896935640679': {'collection': 'articles', 'filter': {'article_id': {'$in': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271, 309, 314, 364, 365, 369, 379, 408, 429, 488, 498, 501, 509, 519, 534, 606, 652, 698, 743, 745, 879, 885, 902, 907, 924, 932, 935, 941, 970, 987, 993, 1001, 1045, 1053, 1061, 1065, 1077, 1084, 1108, 1137, 1171, 1190, 1242, 1244, 1277, 1332, 1363, 1366, 1386, 1435, 1470, 1477, 1494, 1531, 1548, 1570, 1589, 1611, 1631, 1662, 1678, 1689, 1720, 1727, 1736, 1769, 1791, 1792, 1848, 1853, 1866, 1880, 1905, 1910, 1969, 1978, 1996, 2009, 2010, 2017, 2023, 2041, 2168, 2180, 2214, 2218, 2270, 2285, 2302, 2322, 2351, 2358, 2368, 2389, 2395, 2414, 2430, 2457, 2470, 2491, 2501, 2505, 2512, 2514, 2517, 2519, 2602, 2613, 2616, 2617, 2668, 2675, 2676, 2693, 2707, 2725, 2740, 2741, 2762, 2767, 2783, 2798, 2859, 2887, 2901, 2903, 3006, 3016, 3019, 3028, 3059, 3061, 3079, 3096, 3127, 3137, 3139, 3153, 3215, 3222, 3231, 3232, 3234, 3239, 3244, 3257, 3265, 3289, 3305, 3368, 3389, 3417, 3445, 3457, 3482, 3492, 3510, 3523, 3545, 3559, 3564, 3570, 3574, 3601, 3631, 3643, 3665, 3678, 3688, 3733, 3750, 3755, 3789, 3846, 3852, 3861, 3909, 3914, 3917, 3945, 4016, 4041, 4050, 4056, 4089, 4090, 4129, 4144, 4181, 4224, 4270, 4272, 4327, 4339, 4369, 4370, 4411, 4437, 4438, 4440, 4568, 4575, 4583, 4600, 4623, 4665, 4679, 4719, 4731, 4763, 4801, 4890, 4906, 4909, 4922, 4953, 4959, 4996, 5003, 5009, 5023, 5031, 5037, 5041, 5062, 5078, 5100, 5102, 5109, 5111, 5143, 5149, 5151, 5158, 5171, 5172, 5176, 5293, 5300, 5303, 5313, 5351, 5357, 5365, 5370, 5393, 5395, 5396, 5410, 5430, 5471, 5532, 5581, 5584, 5600, 5605, 5614, 5655, 5671, 5683, 5687, 5694, 5713, 5722, 5723, 5768, 5784, 5831, 5834, 5841, 5870, 5904, 5915, 5935, 5945, 5951, 5959, 5983, 6009, 6030, 6034, 6054, 6111, 6115, 6140, 6166, 6183, 6231, 6249, 6295, 6301, 6306, 6346, 6400, 6411, 6417, 6435, 6436, 6486, 6507, 6527, 6528, 6538, 6557, 6569, 6584, 6615, 6654, 6691, 6692, 6742, 6745, 6756, 6761, 6768, 6814, 6830, 6834, 6838, 6840, 6870, 6881, 6893, 6905, 6913, 6918, 6949, 6997, 7068, 7114, 7122, 7140, 7218, 7243, 7257, 7275, 7289, 7301, 7336, 7338, 7356, 7371, 7376, 7388, 7393, 7415, 7418, 7426, 7458, 7488, 7499, 7500, 7516, 7567, 7600, 7610, 7629, 7630, 7643, 7656, 7665, 7685, 7700, 7714, 7731, 7737, 7783, 7790, 7875, 7876, 7887, 7896, 7897, 7901, 7906, 7923, 7946, 7949, 7952, 7957, 8023, 8027, 8042, 8079, 8142, 8154, 8185, 8217, 8218, 8248, 8260, 8302, 8304, 8309, 8327, 8348, 8360, 8373, 8416, 8443, 8473, 8475, 8486, 8495, 8516, 8521, 8522, 8546, 8572, 8576, 8607, 8616, 8631, 8632, 8645, 8681, 8692, 8695, 8739, 8762, 8778, 8803, 8831, 8849, 8853, 8899, 9000, 9055, 9083, 9101, 9120, 9127, 9163, 9164, 9165, 9216, 9220, 9249, 9261, 9268, 9292, 9295, 9348, 9409, 9429, 9439, 9466, 9490, 9506, 9521, 9530, 9534, 9576, 9590, 9650, 9657, 9660, 9681, 9684, 9693, 9705, 9751, 9764, 9772, 9793, 9801, 9848, 9860, 9898, 9913, 9933, 9937, 9948, 9975, 9978, 10045, 10050, 10051, 10062, 10079, 10084, 10095, 10113, 10170, 10173, 10187, 10200, 10223, 10242, 10292, 10329, 10344, 10380, 10383, 10388, 10418, 10419, 10475, 10509, 10525, 10537, 10539, 10573, 10589, 10595, 10596, 10611, 10631, 10661, 10671, 10676, 10682, 10769, 10808, 10832, 10858, 10864, 10893, 10921, 10944, 10947, 10967, 11025, 11033, 11048, 11062, 11094, 11127, 11142, 11206, 11222, 11265, 11285, 11343, 11357, 11401, 11416, 11431, 11465, 11472, 11489, 11491, 11509, 11539, 11558, 11560, 11584, 11585, 11589, 11591, 11595, 11598, 11602, 11632, 11645, 11664, 11671, 11717, 11732, 11744, 11750, 11753, 11768, 11814, 11855, 11856, 11877, 11880, 11882, 11883, 11893, 11936, 11940, 11946, 11977, 12000, 12010, 12022, 12032, 12076, 12126, 12139, 12156, 12179, 12204, 12207, 12211, 12215, 12257, 12272, 12282, 12287, 12355, 12381, 12409, 12410, 12419, 12457, 12493, 12516, 12556, 12560, 12561, 12572, 12589, 12596, 12598, 12601, 12604, 12607, 12608, 12614, 12615, 12629, 12632, 12636, 12637, 12650, 12658, 12662, 12671, 12774, 12800, 12805, 12873, 12910, 12926, 12931, 12934, 13005, 13013, 13030, 13037, 13055, 13060, 13066, 13075, 13091, 13098, 13127, 13146, 13206, 13231, 13264, 13296, 13297, 13316, 13341, 13343, 13352, 13368, 13377, 13381, 13418, 13456, 13459, 13465, 13467, 13534, 13541, 13542, 13556, 13564, 13583, 13632, 13685, 13691, 13709, 13714, 13725, 13741, 13749, 13819, 13823, 13881, 13944, 13947, 13950, 13957, 13964, 13966, 14049, 14086, 14100, 14106, 14108, 14114, 14136, 14154, 14200, 14254, 14273, 14305, 14310, 14320, 14329, 14342, 14374, 14399, 14423, 14443, 14451, 14456, 14510, 14529, 14533, 14573, 14585, 14609, 14631, 14663, 14664, 14678, 14694, 14696, 14745, 14763, 14775, 14780, 14782, 14787, 14797, 14800, 14834, 14893, 14919, 14951, 14981, 15006, 15009, 15059, 15118, 15123, 15131, 15164, 15174, 15190, 15202, 15203, 15216, 15249, 15253, 15257, 15282, 15298, 15303, 15315, 15318, 15319, 15331, 15365, 15421, 15422, 15430, 15496, 15500, 15519, 15527, 15571, 15575, 15590, 15592, 15608, 15610, 15675, 15758, 15761, 15788, 15821, 15835, 15871, 15875, 15876, 15878, 15888, 15908, 15957, 15972, 16031, 16061, 16080, 16112, 16132, 16143, 16179, 16200, 16212, 16213, 16233, 16301, 16339, 16355, 16361, 16385, 16390, 16395, 16435, 16489, 16490, 16560, 16564, 16570, 16585, 16604, 16620, 16674, 16750, 16763, 16808, 16813, 16838, 16883, 16908, 16915, 16929, 16962, 16980, 17023, 17030, 17089, 17097, 17136, 17144, 17157, 17168, 17202, 17246, 17255, 17262, 17317, 17348, 17368, 17371, 17376, 17420, 17422, 17425, 17436, 17443, 17471, 17519, 17550, 17563, 17571, 17601, 17621, 17636, 17643, 17675, 17707, 17753, 17758, 17771, 17800, 17803, 17826, 17840, 17875, 17885, 17889, 17909, 17915, 17925, 17942, 17955, 17963, 17966, 17967, 17976, 17987, 18012, 18059, 18068, 18078, 18084, 18091, 18101, 18126, 18128, 18137, 18163, 18183, 18195, 18230, 18239, 18285, 18292, 18312, 18321, 18332, 18344, 18423, 18442, 18454, 18459, 18486, 18506, 18515, 18548, 18567, 18578, 18597, 18614, 18619, 18629, 18654, 18690, 18724, 18729, 18730, 18741, 18752, 18770, 18775, 18776, 18798, 18806, 18833, 18838, 18841, 18842, 18889, 18914, 18916, 18940, 18944, 18965, 18970, 18992, 19010, 19015, 19034, 19042, 19098, 19104, 19111, 19130, 19143, 19144, 19170, 19172, 19174, 19187, 19201, 19213, 19216, 19227, 19252, 19257, 19301, 19314, 19326, 19339, 19343, 19371, 19411, 19449, 19502, 19541, 19580, 19585, 19630, 19643, 19712, 19744, 19752, 19769, 19777, 19788, 19798, 19800, 19817, 19831, 19904, 19906, 19918, 19930, 19956, 19968, 20014, 20029]}}, 'limit': 1000}, 'var_function-call-16426148715308528007': 'file_storage/function-call-16426148715308528007.json', 'var_function-call-74620427741394151': {'processed_in_batch': 998, 'world_found': 308, 'total_counts': {'Africa': 70, 'Asia': 60, 'South America': 69, 'North America': 62, 'Europe': 47}}, 'var_function-call-3337357360678412435': 'file_storage/function-call-3337357360678412435.json'}

exec(code, env_args)
