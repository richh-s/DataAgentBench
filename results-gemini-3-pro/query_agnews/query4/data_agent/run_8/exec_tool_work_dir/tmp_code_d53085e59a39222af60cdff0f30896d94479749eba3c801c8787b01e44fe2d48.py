code = """import json
import collections
import re

# Load metadata
path_meta = locals()['var_function-call-750385390280883322']
with open(path_meta, 'r') as f:
    metadata = json.load(f)

# Load previous counts
prev_result_var = locals()['var_function-call-13688558663543767915']
if isinstance(prev_result_var, str):
    # Try to clean it if needed or just load
    try:
        region_counts = json.loads(prev_result_var)
    except:
        region_counts = {}
elif isinstance(prev_result_var, dict):
    region_counts = prev_result_var
else:
    region_counts = {}

# Load new articles
path_articles = locals()['var_function-call-1071897199243019569']
if isinstance(path_articles, str):
    with open(path_articles, 'r') as f:
        articles_list = json.load(f)
else:
    articles_list = path_articles

# Create lookup for NEW articles
articles_dict = {}
for a in articles_list:
    try:
        aid = int(a['article_id'])
        articles_dict[aid] = a
    except:
        pass

# Keywords
keywords = {
    'World': set([
        'world', 'international', 'president', 'minister', 'parliament', 'senate', 'congress', 'war', 'peace', 
        'treaty', 'united nations', 'un', 'nato', 'eu', 'european union', 'syria', 'iraq', 'iran', 'afghanistan', 
        'israel', 'palestine', 'gaza', 'ukraine', 'russia', 'putin', 'obama', 'white house', 'pentagon', 'military', 
        'army', 'navy', 'air force', 'bomb', 'attack', 'terror', 'isis', 'al qaeda', 'protest', 'election', 'vote', 
        'poll', 'government', 'policy', 'diplomacy', 'ambassador', 'official', 'leader', 'prime minister', 'chancellor', 
        'premier', 'security', 'nuclear', 'weapon', 'sanction', 'crisis', 'refugee', 'migrant', 'border', 'police', 
        'court', 'law', 'judge', 'trial', 'prison', 'kill', 'dead', 'death', 'blast', 'explosion', 'suicide', 'crash',
        'storm', 'hurricane', 'quake', 'earthquake', 'flood', 'disaster', 'rescue', 'egypt', 'libya', 'korea', 'china',
        'germany', 'france', 'britain', 'uk', 'spain', 'italy', 'greece', 'turkey', 'pakistan', 'india', 'africa'
    ]),
    'Sports': set([
        'sport', 'game', 'match', 'team', 'club', 'player', 'coach', 'manager', 'league', 'tournament', 'cup', 
        'championship', 'olympic', 'medal', 'score', 'win', 'lose', 'draw', 'victory', 'defeat', 'football', 'soccer', 
        'basketball', 'nba', 'baseball', 'mlb', 'hockey', 'nhl', 'tennis', 'golf', 'racing', 'driver', 'athlete', 
        'stadium', 'fan', 'season', 'playoff', 'final', 'world cup', 'super bowl', 'cricket', 'rugby'
    ]),
    'Business': set([
        'business', 'company', 'corporation', 'inc', 'ltd', 'stock', 'share', 'market', 'exchange', 'wall street', 
        'dow jones', 'nasdaq', 's&p', 'price', 'cost', 'profit', 'loss', 'earning', 'revenue', 'sales', 'quarter', 
        'deal', 'merger', 'acquisition', 'buyout', 'invest', 'bank', 'finance', 'economy', 'economic', 'trade', 
        'dollar', 'euro', 'yen', 'currency', 'inflation', 'rate', 'fed', 'federal reserve', 'oil', 'gas', 'energy', 
        'gold', 'ceo', 'cfo', 'executive', 'job', 'unemployment', 'hiring', 'retail', 'industry'
    ]),
    'Sci_Tech': set([
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'app', 
        'mobile', 'phone', 'smartphone', 'tablet', 'apple', 'google', 'microsoft', 'facebook', 'amazon', 'twitter', 
        'intel', 'ibm', 'nasa', 'space', 'mars', 'moon', 'rocket', 'launch', 'satellite', 'orbit', 'astronomy', 
        'physics', 'chemistry', 'biology', 'medical', 'health', 'disease', 'virus', 'cancer', 'study', 'research', 
        'scientist', 'engineer', 'robot', 'ai', 'artificial intelligence', 'browser', 'server', 'data', 'cyber'
    ])
}

# Process metadata
for meta in metadata:
    aid = int(meta['article_id'])
    region = meta['region']
    
    if aid in articles_dict:
        art = articles_dict[aid]
        title = art.get('title', '').lower()
        desc = art.get('description', '').lower()
        text = title + ' ' + desc
        
        tokens = re.findall(r'\w+', text)
        token_set = set(tokens)
        
        scores = {}
        for cat, kws in keywords.items():
            scores[cat] = len(token_set.intersection(kws))
            
        if sum(scores.values()) == 0:
            continue
            
        best_cat = max(scores, key=scores.get)
        
        max_val = scores[best_cat]
        tied = [k for k, v in scores.items() if v == max_val]
        if 'World' in tied:
            best_cat = 'World'

        if best_cat == 'World':
            region_counts[region] = region_counts.get(region, 0) + 1

print('__RESULT__:')
print(json.dumps(region_counts))"""

env_args = {'var_function-call-750385390280883322': 'file_storage/function-call-750385390280883322.json', 'var_function-call-6083932913443130219': 6696, 'var_function-call-14170722069696433452': 'file_storage/function-call-14170722069696433452.json', 'var_function-call-14254421073685728294': [{'_id': '6944f121311e1de8e6047551', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f121311e1de8e6047552', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f121311e1de8e6047553', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f121311e1de8e6047554', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f121311e1de8e6047555', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6366566729007167229': [{'region': 'Africa', 'count': '1345'}, {'region': 'Asia', 'count': '1333'}, {'region': 'Europe', 'count': '1357'}, {'region': 'North America', 'count': '1329'}, {'region': 'South America', 'count': '1332'}], 'var_function-call-17726170228108370257': [26, 52, 117, 519, 652, 745, 907, 924, 970, 1077, 1277, 1494, 1689, 1866, 2041, 2218, 2270, 2395, 2491, 2514, 2519, 2602, 2617, 2725, 2762, 2859, 3139, 3153, 3232, 3234, 3244, 3257, 3265, 3389, 3564, 3909, 3917, 3945, 4056, 4272, 4440, 4575, 4679, 4801, 4909, 5031, 5109, 5158, 5171, 5176, 5351, 5365, 5370, 5430, 5532, 5584, 5600, 5671, 5784, 5904, 5959, 6030, 6054, 6306, 6435, 6528, 6692, 6881, 6949, 7218, 7243, 7388, 7393, 7415, 7458, 7500, 7685, 7737, 7887, 7949, 8079, 8154, 8260, 8360, 8473, 8475, 8632, 8681, 8692, 8762, 9083, 9429, 9490, 9521, 9530, 9590, 9681, 9801, 9913, 9937, 9978, 10095, 10170, 10223, 10242, 10329, 10383, 10419, 10475, 10539, 10893, 11127, 11206, 11265, 11357, 11539, 11589, 11632, 11732, 11814, 11882, 11883, 11977, 12139, 12215, 12287, 12556, 12572, 12608, 12650, 12662, 12931, 13005, 13013, 13037, 13060, 13075, 13146, 13206, 13231, 13316, 13352, 13542, 13583, 13685, 14305, 14399, 14423, 14533, 14663, 14696, 14763, 14780, 14787, 14834, 15118, 15123, 15131, 15174, 15203, 15253, 15315, 15318, 15788, 15821, 15871, 15878, 15908, 16061, 16112, 16132, 16212, 16213, 16233, 16301, 16585, 16813, 16980, 17097, 17368, 17422, 17425, 17443, 17563, 17601, 17675, 17800, 17840, 17885, 17915, 17925, 17942, 17966, 18078, 18091, 18101, 18137, 18454, 18506, 18729, 18730, 18752, 18889, 19015, 19104, 19144, 19170, 19314, 19371, 19502, 19580, 19585, 19712, 19744, 19798, 19817, 20077, 20136, 20168, 20229, 20265, 20298, 20416, 20545, 20618, 20883, 21009, 21054, 21104, 21205, 21209, 21282, 21478, 21508, 21551, 21591, 21718, 22015, 22051, 22308, 22611, 22638, 22655, 22759, 22794, 22890, 22971, 23084, 23604, 23723, 23807, 23941, 23963, 24058, 24230, 24273, 24382, 24385, 24393, 24485, 24500, 24647, 24727, 24770, 24773, 24822, 24874, 24918, 25199, 25334, 25448, 25537, 25663, 25670, 25706, 25854, 25856, 25876, 26134, 26159, 26338, 26516, 26761, 26876, 27013, 27029, 27050, 27324, 27411, 27465, 27558, 27578, 27600, 27750, 27870, 27948, 28053, 28142, 28193, 28308, 28419, 28501, 28721, 28735, 28897, 28930, 29201, 29224, 29257, 29319, 29452, 29604, 29726, 29809, 30111, 30312, 30541, 30602, 30613, 30822, 31105, 31137, 31138, 31375, 31530, 31647, 31761, 31810, 32008, 32164, 32187, 32349, 32545, 32585, 32617, 32690, 32787, 32808, 33124, 33209, 33230, 33303, 33351, 33635, 33652, 33715, 33733, 33750, 33809, 33815, 34020, 34053, 34056, 34086, 34238, 34266, 34554, 34775, 34820, 34869, 35022, 35190, 35267, 35422, 35478, 35498, 35581, 35655, 35658, 35733, 35779, 35825, 35926, 35983, 36005, 36120, 36182, 36255, 36396, 36473, 36496, 36510, 36564, 36603, 36678, 36732, 36776, 36833, 37018, 37317, 37486, 37573, 37610, 37617, 37769, 37903, 37915, 37926, 37965, 38047, 38378, 38611, 38695, 38843, 38882, 38892, 38984, 39230, 39261, 39314, 39387, 39539, 39591, 39739, 39765, 39837, 40048, 40109, 40138, 40266, 40298, 40309, 40509, 40515, 40565, 40652, 40712, 40726, 40734, 40737, 40857, 40890, 40923, 40939, 40948, 40984, 41110, 41261, 41286, 41328, 41341, 41537, 41619, 41657, 41708, 41923, 41948, 42052, 42142, 42191, 42442, 42487, 42498, 42521, 42546, 42972, 43005, 43193, 43428, 43609, 43736, 43757, 43796, 43813, 43947, 44105, 44131, 44268, 44459, 44553, 44626, 44658, 44701, 44727, 44782, 44797, 44974, 45042, 45163, 45222, 45323, 45458, 45599, 45619, 45791, 45816, 45912, 46000, 46089, 46103, 46131, 46184, 46187, 46269, 46430, 46602, 46694, 46731, 46738, 46902, 46946, 47101, 47168, 47210, 47290, 47299, 47606, 47644, 47670, 47762, 47785, 47805, 47953, 48010, 48078, 48104, 48165, 48287, 48355, 48421, 48428, 48523, 48705, 49022, 49030, 49050, 49058, 49071, 49186, 49196, 49322, 49378, 49420, 49677, 49730, 49879, 50057, 50130, 50263, 50284, 50385, 50667, 50673, 50774, 50832, 50845, 50907, 50934, 50957, 51037, 51135, 51313, 51437, 51567, 51737, 51861, 51886, 52113, 52128, 52177, 52200, 52346, 52396, 52650, 52686, 52894, 52991, 53007, 53067, 53194, 53275, 53352, 53466, 53592, 53627, 53781, 53866, 54118, 54156, 54190, 54291, 54428, 54488, 54522, 54533, 54604, 54668, 54704, 54749, 54753, 54796, 55248, 55326, 55468, 55950, 55986, 55998, 56273, 56303, 56427, 56465, 56629, 56993, 57058, 57059, 57076, 57430, 57557, 57568, 57631, 57688, 57814, 57884, 57893, 57989, 58037, 58055, 58251, 58279, 58309, 58397, 58402, 58453, 58459, 58577, 58650, 58685, 58811, 58849, 58957, 58975, 59077, 59364, 59381, 59435, 59457, 59486, 59558, 59610, 59685, 59849, 59878, 59929, 59944, 60056, 60088, 60095, 60224, 60256, 60426, 60582, 60650, 60700, 60789, 60891, 61061, 61125, 61155, 61176, 61264, 61273, 61288, 61343, 61353, 61552, 61589, 61604, 61620, 61660, 61665, 61922, 61963, 62033, 62057, 62083, 62221, 62252, 62364, 62434, 62541, 62562, 62621, 63112, 63153, 63263, 63415, 63480, 63503, 63570, 63791, 63991, 64021, 64046, 64301, 64477, 64492, 64495, 64519, 64668, 64673, 64748, 64759, 64781, 64845, 65055, 65205, 65299, 65366, 65382, 65706, 65893, 65983, 66090, 66096, 66184, 66217, 66272, 66371, 66434, 66655, 66681, 66688, 66815, 66896, 66942, 67089, 67144, 67254, 67301, 67309, 67356, 67485, 67511, 67780, 67839, 67939, 68043, 68214, 68429, 68476, 68606, 68849, 68962, 69056, 69203, 69224, 69261, 69263, 69508, 69590, 69761, 69895, 69923, 69977, 70033, 70041, 70056, 70157, 70486, 70574, 70600, 70631, 70686, 70867, 70870, 70915, 71029, 71849, 72149, 72164, 72196, 72302, 72307, 72351, 72372, 72393, 72705, 72907, 73121, 73183, 73227, 73245, 73366, 73388, 73435, 73561, 73586, 73767, 73891, 73950, 73957, 74034, 74059, 74064, 74154, 74243, 74264, 74335, 74644, 74705, 74797, 74933, 74971, 75037, 75076, 75235, 75363, 75374, 75427, 75448, 75496, 75521, 75530, 75554, 75626, 75811, 75826, 75830, 75901, 75957, 76002, 76107, 76145, 76265, 76357, 76389, 76467, 76472, 76521, 76542, 77099, 77137, 77165, 77276, 77305, 77402, 77442, 77575, 77726, 77785, 77803, 77948, 77984, 78207, 78296, 78336, 78497, 78698, 78746, 78750, 78775, 78807, 78911, 79011, 79110, 79138, 79329, 79398, 79565, 79861, 79867, 79962, 80009, 80028, 80085, 80243, 80256, 80293, 80431, 80501, 80633, 80702, 80816, 80894, 81029, 81107, 81212, 81508, 81613, 81620, 81844, 82019, 82077, 82235, 82247, 82341, 82351, 82401, 82500, 82550, 82559, 82902, 83021, 83110, 83281, 83393, 83418, 83450, 83623, 83845, 83892, 83893, 83968, 84050, 84051, 84143, 84244, 84273, 84426, 84457, 84539, 84661, 84799, 84897, 84900, 84944, 85008, 85089, 85114, 85377, 85477, 85553, 85587, 85620, 85644, 85870, 85874, 86025, 86279, 86372, 86522, 86573, 86632, 86634, 86710, 86925, 86932, 86956, 87009, 87080, 87154, 87267, 87352, 87473, 87560, 87638, 87740, 87822, 87829, 87905, 87987, 88187, 88210, 88246, 88321, 88331, 88476, 88639, 88837, 88909, 89189, 89398, 89615, 89634, 89738, 89957, 90034, 90135, 90377, 90691, 91027, 91130, 91157, 91194, 91266, 91446, 91505, 91564, 91784, 92200, 92284, 92468, 92636, 92670, 93104, 93151, 93314, 93325, 93399, 93454, 93505, 93531, 93700, 93850, 94139, 94288, 94319, 94512, 94518, 94599, 94862, 94955, 95022, 95044, 95196, 95288, 95485, 95593, 95677, 95712, 95743, 95923, 96109, 96534, 96636, 96684, 97018, 97109, 97263, 97332, 97361, 97377, 97428, 97453, 97549, 97643, 98051, 98094, 98134, 98168, 98188, 98258, 98273, 98472, 98508, 98599, 98606, 98730, 98804, 98840, 98889, 98994, 99147, 99196, 99509, 99579, 99956, 100219, 100387, 100706, 100783, 100868, 100993, 101111, 101125, 101133, 101134, 101140, 101218, 101347, 101427, 101466, 101485, 101492, 101771, 101790, 101928, 102018, 102090, 102442, 102598, 102856, 102942, 102989, 103391, 103416, 103440, 103457, 103465, 103505, 103527, 103537, 103542, 103676, 103734, 103763, 103855, 103921, 103956, 104061, 104485, 104489, 104533, 104568, 104634, 104636, 104644, 104752, 104862, 104924, 104991, 105079, 105095, 105128, 105307, 105322, 105389, 105457, 105517, 105664, 105697, 105735, 105746, 105760, 105905, 106104, 106123, 106130, 106399, 106526, 106612, 106744, 106776, 107280, 107334, 107338, 107348, 107461, 107474, 107483, 107709, 107976, 108535, 109036, 109052, 109185, 109244, 109320, 109396, 109601, 109642, 109714, 109786, 109898, 109902, 109915, 109930, 109996, 110221, 110342, 110420, 110536, 110682, 110732, 111016, 111088, 111092, 111210, 111292, 111407, 111478, 111578, 111657, 111690, 111707, 111739, 111893, 111971, 112081, 112112, 112283, 112441, 112493, 112554, 112596, 112767, 113066, 113233, 113291, 113313, 113450, 113478, 113488, 113554, 113568, 113797, 113940, 114070, 114089, 114133, 114169, 114247, 114275, 114355, 114568, 114631, 114834, 114865, 114999, 115002, 115070, 115170, 115285, 115316, 115325, 115398, 115574, 115610, 116299, 116370, 116425, 116491, 116630, 116675, 116824, 116943, 116961, 117123, 117231, 117418, 117482, 117535, 117555, 117581, 117598, 117650, 117673, 117759, 117788, 117793, 117828, 117978, 117990, 118145, 118314, 118321, 118339, 118386, 118487, 118613, 118682, 118810, 118892, 118906, 119076, 119099, 119116, 119266, 119278, 119279, 119339, 119341, 119378, 119391, 119675, 119703, 119914, 119923, 119947, 119985, 120071, 120132, 120136, 120152, 120377, 120437, 120537, 120555, 120737, 120738, 120821, 120832, 120891, 121017, 121076, 121135, 121154, 121272, 121566, 121624, 121695, 121816, 121833, 121963, 122219, 122284, 122318, 122512, 122542, 122543, 122636, 122746, 122800, 123009, 123076, 123355, 123508, 123536, 123553, 123569, 123723, 123867, 123898, 124139, 124140, 124283, 124490, 124500, 124511, 124593, 124653, 124692, 124784, 125005, 125023, 125036, 125089, 125133, 125234, 125461, 125481, 125523, 125568, 125698, 125763, 125840, 126041, 126175, 126235, 126346, 126500, 126515, 126562, 126780, 126893, 126979, 126981, 127014, 127111, 127132, 127329, 127347, 127369, 127481, 127569], 'var_function-call-9772360271843666231': {'min': 13, 'max': 127570}, 'var_function-call-17096305328570719460': [{'_id': '6944f121311e1de8e604755e', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6944f121311e1de8e604755f', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6944f121311e1de8e6047560', 'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'_id': '6944f121311e1de8e6047561', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '6944f121311e1de8e6047562', 'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-13766394313769607760': {}, 'var_function-call-16514271034045290253': {'meta_count': 6696, 'articles_count': 5, 'overlap_count': 1, 'samples': [{'id': 13, 'title': 'Google IPO Auction Off to Rocky Start'}]}, 'var_function-call-3329559544456987844': 'file_storage/function-call-3329559544456987844.json', 'var_function-call-13688558663543767915': {'South America': 375, 'Europe': 365, 'Asia': 374, 'North America': 354, 'Africa': 382}, 'var_function-call-1071897199243019569': 'file_storage/function-call-1071897199243019569.json'}

exec(code, env_args)
