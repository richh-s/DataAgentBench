code = """import json
import collections

# Load metadata (File)
path_metadata = locals()['var_function-call-1035739676556382774']
with open(path_metadata, 'r') as f:
    metadata = json.load(f)

id_to_region = {item['article_id']: item['region'] for item in metadata}

# Load articles (Check type)
articles_data = locals()['var_function-call-3985334907629477990']
if isinstance(articles_data, str):
    # It's a file path
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    # It's the list
    articles = articles_data

# Classification Logic
keywords = {
    'World': ["iraq", "iran", "palestin", "israel", "afghanistan", "syria", "egypt", "ukraine", "russia", "china", "japan", "korea", "germany", "france", "britain", "uk", "united nations", "un", "nato", "eu", "european union", "president", "minister", "prime minister", "official", "government", "parliament", "election", "vote", "poll", "protest", "riot", "police", "kill", "dead", "bomb", "blast", "attack", "terror", "isis", "qaeda", "taliban", "rebel", "militia", "military", "army", "troop", "soldier", "war", "peace", "treaty", "summit", "talks", "nuclear", "weapon", "sanction", "crisis", "refugee", "migrant", "border", "global", "international", "world", "foreign"],
    'Sports': ["sport", "baseball", "basketball", "football", "soccer", "tennis", "golf", "hockey", "cricket", "rugby", "olympic", "game", "match", "tournament", "championship", "cup", "league", "team", "club", "player", "coach", "score", "win", "lose", "victory", "defeat", "medal", "stadium", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "race", "racing"],
    'Business': ["business", "company", "inc", "corp", "corporation", "market", "stock", "share", "wall street", "dow jones", "nasdaq", "invest", "investor", "profit", "loss", "earn", "revenue", "sale", "quarter", "bank", "finance", "economy", "economic", "recession", "inflation", "rate", "fed", "federal reserve", "dollar", "euro", "yen", "currency", "trade", "oil", "gold", "price", "cost", "merger", "acquisition", "ceo", "cfo", "manager", "executive", "job", "unemployment", "bid"],
    'Sci/Tech': ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "digital", "mobile", "phone", "smartphone", "app", "google", "microsoft", "apple", "ibm", "intel", "facebook", "twitter", "amazon", "yahoo", "nasa", "space", "astronomy", "biotech", "biology", "physics", "chemistry", "study", "research", "discover", "invent", "gadget", "device", "chip", "processor", "server", "network", "wireless", "broadband", "satellite", "robot", "ai", "linux", "browser"]
}

def classify(text):
    text = text.lower()
    scores = {k: 0 for k in keywords}
    for cat, kw_list in keywords.items():
        for kw in kw_list:
            if kw in text:
                scores[cat] += 1
    
    if "oil" in text and "price" in text: scores['Business'] += 2
    if "iraq" in text or "war" in text: scores['World'] += 2
    if "game" in text and "win" in text: scores['Sports'] += 2
    if "google" in text or "microsoft" in text: scores['Sci/Tech'] += 2
    
    m = max(scores.values())
    if m == 0:
        return "Unknown"
    
    candidates = [k for k, v in scores.items() if v == m]
    if 'World' in candidates: return 'World'
    return candidates[0]

world_counts = collections.Counter()
processed_count = 0
found_count = 0

# article_id in Mongo result is string (checked preview). In metadata it is string.
# We should ensure matching types.

for art in articles:
    aid = str(art['article_id'])
    if aid in id_to_region:
        processed_count += 1
        text = (art.get('title', '') + " " + art.get('description', ''))
        cat = classify(text)
        if cat == 'World':
            found_count += 1
            region = id_to_region[aid]
            world_counts[region] += 1

print(f"Processed: {processed_count}, Found World: {found_count}")
print("__RESULT__:")
print(json.dumps(world_counts))"""

env_args = {'var_function-call-1035739676556382774': 'file_storage/function-call-1035739676556382774.json', 'var_function-call-3913174241045787597': 'file_storage/function-call-3913174241045787597.json', 'var_function-call-4226666748069906040': 6696, 'var_function-call-8137097747050366523': [{'_id': '694517b9aca359b335e4a6f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694517b9aca359b335e4a6f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694517b9aca359b335e4a6f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694517b9aca359b335e4a6fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694517b9aca359b335e4a6fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14483490166809063929': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-8016527500700536991': {'max_gap': 181, 'gaps_gt_100': 30}, 'var_function-call-9539619455840806462': 'file_storage/function-call-9539619455840806462.json', 'var_function-call-8627244258780105005': {'collection': 'articles', 'filter': {'article_id': {'$in': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271, 309, 314, 364, 365, 369, 379, 408, 429, 488, 498, 501, 509, 519, 534, 606, 652, 698, 743, 745, 879, 885, 902, 907, 924, 932, 935, 941, 970, 987, 993, 1001, 1045, 1053, 1061, 1065, 1077, 1084, 1108, 1137, 1171, 1190, 1242, 1244, 1277, 1332, 1363, 1366, 1386, 1435, 1470, 1477, 1494, 1531, 1548, 1570, 1589, 1611, 1631, 1662, 1678, 1689, 1720, 1727, 1736, 1769, 1791, 1792, 1848, 1853, 1866, 1880, 1905, 1910, 1969, 1978, 1996, 2009, 2010, 2017, 2023, 2041, 2168, 2180, 2214, 2218, 2270, 2285, 2302, 2322, 2351, 2358, 2368, 2389, 2395, 2414, 2430, 2457, 2470, 2491, 2501, 2505, 2512, 2514, 2517, 2519, 2602, 2613, 2616, 2617, 2668, 2675, 2676, 2693, 2707, 2725, 2740, 2741, 2762, 2767, 2783, 2798, 2859, 2887, 2901, 2903, 3006, 3016, 3019, 3028, 3059, 3061, 3079, 3096, 3127, 3137, 3139, 3153, 3215, 3222, 3231, 3232, 3234, 3239, 3244, 3257, 3265, 3289, 3305, 3368, 3389, 3417, 3445, 3457, 3482, 3492, 3510, 3523, 3545, 3559, 3564, 3570, 3574, 3601, 3631, 3643, 3665, 3678, 3688, 3733, 3750, 3755, 3789, 3846, 3852, 3861, 3909, 3914, 3917, 3945, 4016, 4041, 4050, 4056, 4089, 4090, 4129, 4144, 4181, 4224, 4270, 4272, 4327, 4339, 4369, 4370, 4411, 4437, 4438, 4440, 4568, 4575, 4583, 4600, 4623, 4665, 4679, 4719, 4731, 4763, 4801, 4890, 4906, 4909, 4922, 4953, 4959, 4996, 5003, 5009, 5023, 5031, 5037, 5041, 5062, 5078, 5100, 5102, 5109, 5111, 5143, 5149, 5151, 5158, 5171, 5172, 5176, 5293, 5300, 5303, 5313, 5351, 5357, 5365, 5370, 5393, 5395, 5396, 5410, 5430, 5471, 5532, 5581, 5584, 5600, 5605, 5614, 5655, 5671, 5683, 5687, 5694, 5713, 5722, 5723, 5768, 5784, 5831, 5834, 5841, 5870, 5904, 5915, 5935, 5945, 5951, 5959, 5983, 6009, 6030, 6034, 6054, 6111, 6115, 6140, 6166, 6183, 6231, 6249, 6295, 6301, 6306, 6346, 6400, 6411, 6417, 6435, 6436, 6486, 6507, 6527, 6528, 6538, 6557, 6569, 6584, 6615, 6654, 6691, 6692, 6742, 6745, 6756, 6761, 6768, 6814, 6830, 6834, 6838, 6840, 6870, 6881, 6893, 6905, 6913, 6918, 6949, 6997, 7068, 7114, 7122, 7140, 7218, 7243, 7257, 7275, 7289, 7301, 7336, 7338, 7356, 7371, 7376, 7388, 7393, 7415, 7418, 7426, 7458, 7488, 7499, 7500, 7516, 7567, 7600, 7610, 7629, 7630, 7643, 7656, 7665, 7685, 7700, 7714, 7731, 7737, 7783, 7790, 7875, 7876, 7887, 7896, 7897, 7901, 7906, 7923, 7946, 7949, 7952, 7957, 8023, 8027, 8042, 8079, 8142, 8154, 8185, 8217, 8218, 8248, 8260, 8302, 8304, 8309, 8327, 8348, 8360, 8373, 8416, 8443, 8473, 8475, 8486, 8495, 8516, 8521, 8522, 8546, 8572, 8576, 8607, 8616, 8631, 8632, 8645, 8681, 8692, 8695, 8739, 8762, 8778, 8803, 8831, 8849, 8853, 8899, 9000, 9055, 9083, 9101, 9120, 9127, 9163, 9164, 9165, 9216, 9220, 9249, 9261, 9268, 9292, 9295, 9348, 9409, 9429, 9439, 9466, 9490, 9506, 9521, 9530, 9534, 9576, 9590, 9650, 9657, 9660, 9681, 9684, 9693, 9705, 9751, 9764, 9772, 9793, 9801, 9848, 9860, 9898, 9913, 9933, 9937, 9948, 9975, 9978, 10045, 10050, 10051, 10062, 10079, 10084, 10095, 10113, 10170, 10173, 10187, 10200, 10223, 10242, 10292, 10329, 10344, 10380, 10383, 10388, 10418, 10419, 10475, 10509, 10525, 10537, 10539, 10573, 10589, 10595, 10596, 10611, 10631, 10661, 10671, 10676, 10682, 10769, 10808, 10832, 10858, 10864, 10893, 10921, 10944, 10947, 10967, 11025, 11033, 11048, 11062, 11094, 11127, 11142, 11206, 11222, 11265, 11285, 11343, 11357, 11401, 11416, 11431, 11465, 11472, 11489, 11491, 11509, 11539, 11558, 11560, 11584, 11585, 11589, 11591, 11595, 11598, 11602, 11632, 11645, 11664, 11671, 11717, 11732, 11744, 11750, 11753, 11768, 11814, 11855, 11856, 11877, 11880, 11882, 11883, 11893, 11936, 11940, 11946, 11977, 12000, 12010, 12022, 12032, 12076, 12126, 12139, 12156, 12179, 12204, 12207, 12211, 12215, 12257, 12272, 12282, 12287, 12355, 12381, 12409, 12410, 12419, 12457, 12493, 12516, 12556, 12560, 12561, 12572, 12589, 12596, 12598, 12601, 12604, 12607, 12608, 12614, 12615, 12629, 12632, 12636, 12637, 12650, 12658, 12662, 12671, 12774, 12800, 12805, 12873, 12910, 12926, 12931, 12934, 13005, 13013, 13030, 13037, 13055, 13060, 13066, 13075, 13091, 13098, 13127, 13146, 13206, 13231, 13264, 13296, 13297, 13316, 13341, 13343, 13352, 13368, 13377, 13381, 13418, 13456, 13459, 13465, 13467, 13534, 13541, 13542, 13556, 13564, 13583, 13632, 13685, 13691, 13709, 13714, 13725, 13741, 13749, 13819, 13823, 13881, 13944, 13947, 13950, 13957, 13964, 13966, 14049, 14086, 14100, 14106, 14108, 14114, 14136, 14154, 14200, 14254, 14273, 14305, 14310, 14320, 14329, 14342, 14374, 14399, 14423, 14443, 14451, 14456, 14510, 14529, 14533, 14573, 14585, 14609, 14631, 14663, 14664, 14678, 14694, 14696, 14745, 14763, 14775, 14780, 14782, 14787, 14797, 14800, 14834, 14893, 14919, 14951, 14981, 15006, 15009, 15059, 15118, 15123, 15131, 15164, 15174, 15190, 15202, 15203, 15216, 15249, 15253, 15257, 15282, 15298, 15303, 15315, 15318, 15319, 15331, 15365, 15421, 15422, 15430, 15496, 15500, 15519, 15527, 15571, 15575, 15590, 15592, 15608, 15610, 15675, 15758, 15761, 15788, 15821, 15835, 15871, 15875, 15876, 15878, 15888, 15908, 15957, 15972, 16031, 16061, 16080]}}}, 'var_function-call-3985334907629477990': [{'_id': '694517b9aca359b335e4a704', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '694517b9aca359b335e4a705', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '694517b9aca359b335e4a706', 'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'_id': '694517b9aca359b335e4a707', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '694517b9aca359b335e4a708', 'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}]}

exec(code, env_args)
