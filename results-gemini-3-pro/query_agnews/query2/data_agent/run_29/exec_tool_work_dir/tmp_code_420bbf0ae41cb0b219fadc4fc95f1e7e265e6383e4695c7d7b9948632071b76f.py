code = """import json
import re

# Load the articles
file_path = locals()['var_function-call-12444996472603000635']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Categories and keywords (expanded with plurals and variations)
# For simplicity, we will check if the keyword appears as a substring for long words, 
# and use word boundaries for short words.
# Actually, let's just add common variations manually to be safe.

categories = {
    "Science/Technology": [
        "science", "sciences", "technology", "technologies", "tech", "computer", "computers", "computing",
        "internet", "web", "software", "hardware", "chip", "chips", "phone", "phones", "mobile", "mobiles",
        "wireless", "network", "networks", "satellite", "satellites", "space", "nasa", "astronomy", "robot", "robots", "robotic",
        "gadget", "gadgets", "device", "devices", "innovation", "innovations", "physics", "physicist", "biology", "biologist",
        "chemistry", "chemist", "genetics", "genetic", "research", "researcher", "lab", "labs", "laboratory", "laboratories",
        "scientist", "scientists", "discovery", "discoveries", "study", "studies", "medical", "medicine", "drug", "drugs",
        "cancer", "disease", "diseases", "health", "microsoft", "google", "apple", "intel", "linux", "windows",
        "sony", "nintendo", "gameboy", "xbox", "playstation", "wii", "video game", "video games", "console", "consoles",
        "browser", "browsers", "server", "servers", "data", "digital", "cyber", "virus", "viruses", "hacker", "hackers",
        "security", "online", "email", "emails", "spam", "blog", "blogs", "search engine", "mp3", "ipod", "dvd", "dvds",
        "hdtv", "gps", "battery", "batteries", "engine", "engines", "automotive", "ev", "electric vehicle",
        "shuttle", "shuttles", "mission", "missions", "moon", "mars", "probe", "probes", "telescope", "telescopes",
        "galaxy", "galaxies", "planet", "planets", "solar", "energy", "power"
    ],
    "Sports": [
        "sport", "sports", "football", "soccer", "baseball", "basketball", "cricket", "rugby", "hockey", "tennis", "golf",
        "boxing", "f1", "racing", "motorsport", "olympics", "olympic", "athlete", "athletes", "player", "players",
        "team", "teams", "coach", "coaches", "manager", "managers", "club", "clubs", "league", "leagues",
        "tournament", "tournaments", "championship", "championships", "match", "matches", "score", "scores", "scored",
        "win", "wins", "winner", "winners", "winning", "won", "loss", "losses", "lost", "draw", "draws", "cup", "cups",
        "medal", "medals", "stadium", "stadiums", "wimbledon", "nba", "nfl", "mlb", "nhl", "fifa", "uefa",
        "super bowl", "world cup", "grand slam", "game", "games", "play", "plays", "playing", "victory", "victories",
        "defeat", "defeats", "qualify", "qualified", "final", "finals", "semi-final", "semi-finals", "quarter-final"
    ],
    "Business": [
        "business", "businesses", "finance", "financial", "economy", "economic", "economics", "market", "markets",
        "stock", "stocks", "share", "shares", "trade", "trading", "industry", "industries", "company", "companies",
        "corporate", "corporation", "firm", "firms", "profit", "profits", "revenue", "revenues", "loss", "losses",
        "invest", "investment", "investor", "investors", "bank", "banks", "banking", "imf", "wto", "dollar", "dollars",
        "euro", "euros", "oil", "gas", "price", "prices", "cost", "costs", "sale", "sales", "deal", "deals",
        "merger", "mergers", "acquisition", "acquisitions", "ceo", "cfo", "chairman", "executive", "executives",
        "employ", "employment", "job", "jobs", "work", "worker", "workers", "strike", "strikes", "union", "unions",
        "fed", "rate", "rates", "tax", "taxes", "budget", "budgets", "debt", "debts", "deficit", "deficits",
        "inflation", "recession", "growth", "nasdaq", "dow jones", "wall street", "earnings"
    ],
    "World": [
        "world", "international", "politics", "political", "government", "governments", "president", "presidents",
        "minister", "ministers", "premier", "senate", "congress", "parliament", "election", "elections", "vote", "votes",
        "voters", "party", "parties", "democrat", "democrats", "republican", "republicans", "war", "wars", "peace",
        "military", "army", "navy", "air force", "police", "crime", "crimes", "court", "courts", "judge", "judges",
        "law", "laws", "legal", "prison", "prisons", "jail", "jails", "attack", "attacks", "bomb", "bombs", "bombing",
        "blast", "blasts", "terrorism", "terrorist", "terrorists", "rebel", "rebels", "protest", "protests", "protesters",
        "riot", "riots", "disaster", "disasters", "earthquake", "earthquakes", "tsunami", "flood", "floods", "hurricane",
        "hurricanes", "typhoon", "typhoons", "storm", "storms", "fire", "fires", "accident", "accidents", "crash",
        "crashes", "kill", "kills", "killed", "killing", "die", "died", "dead", "death", "deaths", "injure", "injured",
        "injury", "injuries", "victim", "victims", "hostage", "hostages", "kidnap", "kidnapped", "nuclear", "weapon",
        "weapons", "treaty", "agreement", "agreements", "un", "united nations", "eu", "european union", "nato",
        "country", "countries", "nation", "nations", "state", "states", "region", "regions", "city", "cities",
        "town", "towns", "village", "villages", "border", "borders", "iraq", "afghanistan", "iran", "korea", "palestinian", "israel", "gaza"
    ]
}

sci_tech_count = 0
total_articles = len(articles)

for article in articles:
    # Use title + description
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for keyword in keywords:
            # Word boundary search
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                scores[cat] += 1
    
    # Debug print for first few articles
    # if total_articles > 0 and sci_tech_count == 0 and scores["Science/Technology"] > 0:
    #    # Print candidates
    #    pass

    # Determine category
    if sum(scores.values()) == 0:
        predicted_category = "Unknown"
    else:
        # Tie-breaking:
        # If SciTech and Business are tied? E.g. "Tech Company Profits".
        # If SciTech and Sports tied? E.g. "Game" (Sports) vs "Video Game" (SciTech).
        # We can favor SciTech if "technology" or "science" is explicitly mentioned?
        # Let's just pick the max. If tie, Python's max returns the first encountered (Science/Technology is first in dict?).
        # `max` on dictionary keys/items depends on iteration order.
        # Let's make it deterministic.
        sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0])) # Sort by score desc, then name asc
        predicted_category = sorted_scores[0][0] # 'Business', 'Science/Technology', 'Sports', 'World' alphabetically if tied
    
    if predicted_category == "Science/Technology":
        sci_tech_count += 1

result = {
    "sci_tech_count": sci_tech_count,
    "total_articles": total_articles,
    "fraction": sci_tech_count / total_articles if total_articles > 0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1250528354804147004': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-10631316298380501498': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-13227321165050657980': [{'_id': '6944a8bc539490c90ae0e94f', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a8bc539490c90ae0f100', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a8bc539490c90ae0f3ab', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a8bc539490c90ae0f43a', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a8bc539490c90ae0f60a', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-3961297852927952309': {'sci_tech_count': 0, 'total_articles': 5, 'fraction': 0.0}, 'var_function-call-15113086755179134874': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}}, 'var_function-call-2864496782204551437': [], 'var_function-call-6771614803194680542': [{'_id': '6944a8bd539490c90ae19e52', 'article_id': '46531', 'title': 'Ex-Astronaut Casts Doubt on Space Tourism', 'description': 'PRAGUE, Czech Republic -- Eugene Cernan, the last man to walk on the moon during the final Apollo landing, said Thursday he doesn\'t expect space tourism to become reality in the near future, despite a strong demand.   Cernan, now 70, who was commander of NASA\'s Apollo 17 mission and set foot on the lunar surface in December 1972 during his third space flight, acknowledged that "there are many people interested in space tourism."     But the former astronaut said he believed "we are a long way away from the day when we can send a bus of tourists to the moon." He spoke to reporters before being awarded a medal by the Czech Academy of Sciences for his contribution to science...'}], 'var_function-call-14511158998194222407': 5, 'var_function-call-17149797998112667276': [{'_id': '6944a8bc539490c90ae0f811', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-3796667446012513113': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-12444996472603000635': 'file_storage/function-call-12444996472603000635.json', 'var_function-call-7822202230559142960': {'sci_tech_count': 0, 'total_articles': 111, 'fraction': 0.0}}

exec(code, env_args)
