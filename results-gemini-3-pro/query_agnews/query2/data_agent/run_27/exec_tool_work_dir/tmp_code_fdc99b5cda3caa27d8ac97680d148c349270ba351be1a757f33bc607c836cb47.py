code = """import json
import re

# Load articles from file
file_path = locals()['var_function-call-15463062235749369502']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Categories
cats = ["Science/Technology", "Business", "Sports", "World"]

# Keywords sets
kws = {
    "Science/Technology": set([
        "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", 
        "digital", "cyber", "robot", "ai", "space", "nasa", "astronomy", "biology", "physics", "chemistry", 
        "research", "lab", "laboratory", "gadget", "device", "mobile", "phone", "app", "gaming", "console", 
        "nintendo", "sony", "xbox", "microsoft", "google", "apple", "ibm", "intel", "chip", "processor", 
        "server", "network", "wireless", "broadband", "satellite", "data", "algorithm", "program", "code", 
        "developer", "scientist", "medicine", "medical", "health", "disease", "cancer", "virus", "gene", 
        "telescope", "microscope", "nuclear", "energy", "battery", "electric", "engine", "machine", 
        "gameboy", "wii", "playstation", "ipod", "ipad", "iphone", "linux", "windows", "browser", "email", 
        "spam", "hack", "worm", "hacker", "genome", "stem", "cell", "orbit", "mars", "moon", "solar", 
        "galaxy", "universe", "shuttle", "mission", "probe", "launch", "biotech", "cloning", "dna",
        "search", "engine", "blog", "website", "innovative", "innovation"
    ]),
    "Business": set([
        "business", "market", "stock", "share", "profit", "loss", "revenue", "company", "corp", "inc", "ltd", 
        "bank", "economy", "economic", "trade", "deal", "merger", "acquisition", "price", "rate", "dollar", 
        "euro", "yen", "oil", "gas", "mining", "industry", "invest", "finance", "financial", "nasdaq", "dow", 
        "ceo", "cfo", "sales", "retail", "consumer", "inflation", "budget", "debt", "earnings", "quarter", 
        "growth", "recession", "currency", "job", "jobless", "unemployment"
    ]),
    "Sports": set([
        "sport", "match", "cup", "league", "team", "player", "coach", "win", "lose", "score", "olympic", 
        "football", "soccer", "basketball", "baseball", "tennis", "golf", "race", "racing", "f1", "nascar", 
        "cricket", "rugby", "hockey", "boxing", "champion", "title", "medal", "athlete", "stadium", "club", 
        "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "tournament", "season", "playoff", "super", "bowl", 
        "quarterback", "touchdown", "goal", "striker", "midfielder", "defender", "goalkeeper", "pitcher", 
        "batter", "inning", "lap", "wimbledon", "open", "broncos", "red", "sox", "yankees", "lakers", 
        "giants", "dodgers", "mets", "bulls", "knicks", "rangers", "cowboys", "patriots", "eagles", 
        "steelers", "packers", "bears", "colts", "saints", "falcons", "raiders", "dolphins", "jets", 
        "bills", "ravens", "browns", "bengals", "titans", 'jaguars', 'texans', 'chiefs', 'chargers', 
        'cardinals', '49ers', 'seahawks', 'rams', 'lions', 'vikings', 'buccaneers', 'panthers', 'redskins', 
        'nationals', 'phillies', 'braves', 'marlins', 'athletics', 'angels', 'mariners', 'astros', 
        'diamondbacks', 'rockies', 'padres', 'pirates', 'cubs', 'brewers', 'reds', 'indians', 'tigers', 
        'twins', 'royals', 'white', 'blue', 'jays', 'rays', 'orioles', 'squad', 'roster', 'final', 'semi-final'
    ]),
    "World": set([
        "world", "war", "peace", "politic", "government", "president", "minister", "election", "vote", 
        "country", "nation", "international", "un", "eu", "treaty", "attack", "bomb", "terror", "military", 
        "army", "police", "crime", "law", "court", "judge", "prison", "jail", "protest", "riot", "crisis", 
        "disaster", "earthquake", "flood", "storm", "hurricane", "weather", "climate", "china", "usa", "us", 
        "uk", "iraq", "iran", "korea", "russia", "israel", "palestine", "africa", 'asia', 'europe', 
        'foreign', 'security', 'official', 'leader', 'party', 'parliament', 'congress', 'senate', 
        'democrat', 'republican', 'prime', 'chancellor', 'premier', 'strike', 'blast', 'explosion'
    ])
}

# Precompile specific phrase checks (optional or handle via n-grams, but simpler logic first)
# For simplicity, token matching + phrase boosts.

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    
    scores = {c: 0 for c in cats}
    
    # Check words
    for w in words:
        for c, kw_set in kws.items():
            if w in kw_set:
                scores[c] += 1
                
    # Boosts
    if "video game" in text or "computer game" in text:
        scores["Science/Technology"] += 3
    if "wall street" in text:
        scores["Business"] += 3
    if "prime minister" in text:
        scores["World"] += 2
        
    # Heuristics
    # If tie between Sports and World/Business on generic words like "win", "strike"?
    # If "win" is the only match for Sports but "science" is present, SciTech wins.
    # Scores handle this mostly.
    
    # Specific fix for "win" bias
    if "win" in words and scores["Science/Technology"] > 0:
        # "Students Win Science Competition"
        # win is in Sports.
        pass
        
    # Tie breaking:
    # If SciTech > 0 and others are close, prefer SciTech if specific keywords like "science", "tech", "nasa" exist.
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unclassified"
        
    return best_cat

st_articles = 0
total = len(articles)
debug_list = []

for a in articles:
    cat = classify(a['title'], a['description'])
    if cat == "Science/Technology":
        st_articles += 1
        debug_list.append((a['title'], cat))
    # Optional: print non-ST to check
    # else:
    #     debug_list.append((a['title'], cat))

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "st_count": st_articles,
    "fraction": st_articles / total if total else 0,
    "sample_st": debug_list[:10]
}))"""

env_args = {'var_function-call-7987317297082684956': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1452901468857555102': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-3942691636391642572': [{'_id': '6944a664ca819306ee184bcf', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a664ca819306ee185380', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a664ca819306ee18562b', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a664ca819306ee1856ba', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a664ca819306ee18588a', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-8404083196050665480': {'total': 5, 'st_count': 4, 'fraction': 0.8, 'unclassified': 0, 'sample_classifications': [{'title': 'GameBoy mini-games win prize', 'category': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'category': 'Science/Technology'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Science/Technology'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Science/Technology'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Business'}]}, 'var_function-call-8137620351136744425': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-15463062235749369502': 'file_storage/function-call-15463062235749369502.json'}

exec(code, env_args)
