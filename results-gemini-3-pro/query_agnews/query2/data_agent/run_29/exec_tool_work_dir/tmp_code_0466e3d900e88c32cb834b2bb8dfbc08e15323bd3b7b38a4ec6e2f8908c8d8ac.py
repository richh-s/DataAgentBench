code = """import json
import re

file_path = locals()['var_function-call-12444996472603000635']
with open(file_path, 'r') as f:
    articles = json.load(f)

keywords = {
    "Science/Technology": {
        "science": 2, "technolog": 2, "computer": 2, "internet": 2, "web": 1, "software": 2, "hardware": 2, 
        "biology": 2, "physics": 2, "chemistry": 2, "astronomy": 2, "nasa": 2, "space": 2, "robot": 2, 
        "genetic": 2, "medical": 1, "cancer": 1, "disease": 1, "health": 1, "microsoft": 2, "google": 2, 
        "apple": 2, "linux": 2, "video game": 3, "gameboy": 3, "console": 2, "hacker": 2, "virus": 1, 
        "cyber": 2, "online": 1, "digital": 1, "network": 1, "wireless": 2, "satellite": 2, "mars": 2, 
        "moon": 2, "solar": 2, "nuclear": 1, "innovation": 1, "device": 1, "gadget": 2, "mobile": 1, 
        "phone": 1, "lab": 1, "research": 1, "study": 1, "discovery": 1, "engine": 1, "power": 1, "energy": 1,
        "shuttle": 2, "mission": 1, "telescope": 2, "galaxy": 2, "planet": 2, "probe": 2, "automotive": 1, 
        "electric": 1, "electronic": 1, "nanotech": 2, "biotech": 2, "broadband": 2, "server": 2, "browser": 2,
        "ipod": 2, "mp3": 2, "gps": 2, "dvd": 1
    },
    "Sports": {
        "sport": 2, "football": 2, "soccer": 2, "baseball": 2, "basketball": 2, "cricket": 2, "rugby": 2, 
        "hockey": 2, "tennis": 2, "golf": 2, "f1": 2, "racing": 2, "race": 1, "olympic": 3, "athlete": 2, 
        "stadium": 2, "wimbledon": 2, "nba": 2, "nfl": 2, "mlb": 2, "nhl": 2, "fifa": 2, "uefa": 2, 
        "champion": 2, "tournament": 2, "game": 1, "team": 1, "coach": 2, "manager": 1, "player": 1, 
        "match": 1, "cup": 1, "medal": 2, "score": 1, "victory": 1, "defeat": 1, "league": 2, "club": 1,
        "boxing": 2, "motorsport": 2, "driver": 1, "qualify": 1, "final": 1, "super bowl": 2, "world cup": 2
    },
    "Business": {
        "finance": 2, "economy": 2, "market": 2, "stock": 2, "share": 2, "trade": 2, "industry": 1, 
        "profit": 2, "revenue": 2, "invest": 2, "bank": 2, "imf": 2, "wto": 2, "dollar": 2, "euro": 2, 
        "currency": 2, "merger": 2, "acquisition": 2, "ceo": 2, "cfo": 2, "business": 1, "company": 1, 
        "firm": 1, "loss": 1, "sale": 1, "deal": 1, "price": 1, "cost": 1, "employ": 1, "job": 1, 
        "tax": 1, "budget": 1, "debt": 1, "deficit": 1, "inflation": 2, "recession": 2, "growth": 1, 
        "earning": 2, "oil": 1, "gas": 1, "wall street": 2, "dow jones": 2, "nasdaq": 2
    },
    "World": {
        "politics": 2, "government": 2, "president": 2, "minister": 2, "senate": 2, "congress": 2, 
        "parliament": 2, "elect": 1, "democrat": 2, "republican": 2, "war": 2, "peace": 2, "military": 2, 
        "army": 2, "navy": 2, "police": 2, "crime": 2, "court": 2, "judge": 2, "terror": 2, "rebel": 2, 
        "earthquake": 2, "tsunami": 2, "flood": 2, "hurricane": 2, "typhoon": 2, "kill": 1, "bomb": 2, 
        "hostage": 2, "kidnap": 2, "treaty": 2, "un": 2, "nato": 2, "iraq": 2, "afghan": 2, "palestin": 2, 
        "israel": 2, "world": 1, "international": 1, "country": 1, "nation": 1, "state": 1, "region": 1, 
        "city": 1, "law": 1, "legal": 1, "prison": 1, "jail": 1, "attack": 1, "dead": 1, "death": 1, 
        "injure": 1, "victim": 1, "protest": 1, "explosion": 1, "blast": 1
    }
}

debug_info = {}

sci_tech_count = 0
for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    scores = {cat: 0 for cat in keywords}
    
    for cat, words in keywords.items():
        for word, weight in words.items():
            if " " in word:
                if word in text:
                    scores[cat] += weight
            else:
                if re.search(r'\b' + re.escape(word), text):
                    scores[cat] += weight
                    
    if sum(scores.values()) == 0:
        predicted_category = "Unknown"
    else:
        sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        predicted_category = sorted_scores[0][0]
        
    if predicted_category == "Science/Technology":
        sci_tech_count += 1
        
    if str(article['article_id']) == "192":
        debug_info["192"] = {"scores": scores, "pred": predicted_category}

print("__RESULT__:")
print(json.dumps({"sci_tech_count": sci_tech_count, "debug": debug_info}))"""

env_args = {'var_function-call-1250528354804147004': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-10631316298380501498': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-13227321165050657980': [{'_id': '6944a8bc539490c90ae0e94f', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a8bc539490c90ae0f100', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a8bc539490c90ae0f3ab', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a8bc539490c90ae0f43a', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a8bc539490c90ae0f60a', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-3961297852927952309': {'sci_tech_count': 0, 'total_articles': 5, 'fraction': 0.0}, 'var_function-call-15113086755179134874': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}}, 'var_function-call-2864496782204551437': [], 'var_function-call-6771614803194680542': [{'_id': '6944a8bd539490c90ae19e52', 'article_id': '46531', 'title': 'Ex-Astronaut Casts Doubt on Space Tourism', 'description': 'PRAGUE, Czech Republic -- Eugene Cernan, the last man to walk on the moon during the final Apollo landing, said Thursday he doesn\'t expect space tourism to become reality in the near future, despite a strong demand.   Cernan, now 70, who was commander of NASA\'s Apollo 17 mission and set foot on the lunar surface in December 1972 during his third space flight, acknowledged that "there are many people interested in space tourism."     But the former astronaut said he believed "we are a long way away from the day when we can send a bus of tourists to the moon." He spoke to reporters before being awarded a medal by the Czech Academy of Sciences for his contribution to science...'}], 'var_function-call-14511158998194222407': 5, 'var_function-call-17149797998112667276': [{'_id': '6944a8bc539490c90ae0f811', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-3796667446012513113': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-12444996472603000635': 'file_storage/function-call-12444996472603000635.json', 'var_function-call-7822202230559142960': {'sci_tech_count': 0, 'total_articles': 111, 'fraction': 0.0}, 'var_function-call-9206705025700677689': {'sci_tech_count': 0, 'total_articles': 111, 'fraction': 0.0}, 'var_function-call-11948631349389781123': {'_id': '6944a8bc539490c90ae0e94f', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, 'var_function-call-13390419578149446994': {'sci_tech_count': 0, 'total_articles': 111, 'fraction': 0.0}}

exec(code, env_args)
