code = """import json
import os

# Load the articles from the file path
data_var = locals()['var_function-call-2439153792258543021']
with open(data_var, 'r') as f:
    articles = json.load(f)

# Define keywords
categories = {
    "Science/Technology": [
        "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "digital", 
        "mobile", "phone", "wireless", "network", "data", "robot", "space", "nasa", "mars", "orbit", "galaxy", 
        "astronomy", "telescope", "biology", "physics", "chemistry", "research", "lab", "laboratory", "study", 
        "medical", "health", "disease", "virus", "gene", "dna", "drug", "invention", "innovation", "engine", 
        "machine", "device", "gadget", "app", "video game", "gaming", "gameboy", "nintendo", "sony", "microsoft", 
        "apple", "google", "intel", "linux", "windows", "hacker", "security", "broadband", "satellite", "stem",
        "browser", "server", "chip", "processor", "screen", "monitor", "keyboard", "mouse", "laptop", "tablet",
        "smartphone", "algorithm", "code", "program", "developer", "engineer", "scientist", "astronomer", "physicist",
        "biologist", "chemist", "math", "mathematics", "energy", "power", "shuttle", "probe", "sun"
    ],
    "Sports": [
        "sport", "game", "match", "race", "team", "player", "coach", "athlete", "champion", "win", "score", 
        "cup", "league", "season", "olympic", "medal", "stadium", "football", "soccer", "basketball", "baseball", 
        "tennis", "golf", "hockey", "cricket", "rugby", "boxing", "wrestling", "nfl", "nba", "mlb", "nhl", "fifa", 
        "uefa", "tournament", "championship", "club", "squad", "roster", "quarterback", "receiver", "pitcher", 
        "striker", "goal", "touchdown", "homerun", "basket", "points", "ranking", "standings", "pro bowl", "cornerback",
        "giants", "dodgers", "red sox", "yankees", "mets"
    ],
    "Business": [
        "business", "company", "corp", "inc", "market", "stock", "share", "price", "profit", "loss", "revenue", 
        "economy", "finance", "financial", "bank", "trade", "deal", "sale", "investment", "investor", "ceo", 
        "manager", "industry", "growth", "dollar", "euro", "currency", "oil", "gas", "gold", "commodity", 
        "inflation", "tax", "budget", "fed", "recession", "employment", "job", "wage", "salary", "contract", 
        "merger", "acquisition", "retail", "consumer", "product", "brand", "marketing", "advertising", "sales", "mining"
    ],
    "World": [
        "world", "international", "nation", "country", "government", "politics", "political", "election", "president", 
        "minister", "prime minister", "war", "peace", "military", "army", "police", "attack", "bomb", "terror", 
        "terrorist", "terrorism", "crisis", "protest", "conflict", "treaty", "un", "united nations", "foreign", 
        "global", "aid", "refugee", "earthquake", "tsunami", "disaster", "nuclear", "weapon", "law", "court", 
        "judge", "parliament", "congress", "senate", "vote", "poll", "campaign", "party", "democrat", "republican",
        "iraq", "iran", "afghanistan", "syria", "israel", "palestine", "russia", "china", "usa", "europe", "asia", 
        "africa", "middle east", "latin america", "kabul", "baghdad"
    ]
}

def classify_article(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                scores[cat] += 1
                
    # Ambiguity handling
    if "video game" in text or "computer game" in text or "gameboy" in text or "xbox" in text or "playstation" in text:
        scores["Science/Technology"] += 5
        scores["Sports"] -= 2
        
    if "oil" in text and "price" in text:
        scores["Business"] += 2
        
    if "game" in text and scores["Sports"] == scores["Science/Technology"] and scores["Sports"] > 0:
        # Tie breaker. Check for team names or specific sports terms?
        # Default to Sports if generic game, unless tech terms present.
        pass

    best_cat = max(scores, key=scores.get)
    # If all zero, default to World (often most generic) or Unknown.
    if max(scores.values()) == 0:
        return "World" # Fallback
        
    return best_cat

count_total = 0
count_tech = 0
tech_articles = []

for article in articles:
    count_total += 1
    cat = classify_article(article.get('title', ''), article.get('description', ''))
    if cat == "Science/Technology":
        count_tech += 1
        tech_articles.append({"title": article.get('title'), "desc": article.get('description')})

fraction = count_tech / count_total if count_total > 0 else 0

result = {
    "total_articles": count_total,
    "tech_articles_count": count_tech,
    "fraction": fraction,
    "tech_samples": tech_articles[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15106460062194814033': [{'author_id': '218'}], 'var_function-call-1726960274727472925': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-5375187615211989018': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-9561070632733876648': [{'_id': '69448d26019ad6c1848e35d7', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69448d26019ad6c1848e3d88', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69448d26019ad6c1848e4033', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69448d26019ad6c1848e40c2', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69448d26019ad6c1848e4292', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-8397979660664494105': {'total_articles': 5, 'tech_articles_count': 3, 'fraction': 0.6, 'tech_articles_sample': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award'], 'all_categorization_sample': [{'title': 'GameBoy mini-games win prize', 'cat': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Science/Technology'}, {'title': 'Energy from waves  teenager wins science award', 'cat': 'Science/Technology'}, {'title': 'China #39;s appetite boosts BHP', 'cat': 'Business'}]}, 'var_function-call-15095893432800042883': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}}, 'var_function-call-9779007843861641593': [], 'var_function-call-15492065944510889192': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 1000}, 'var_function-call-2439153792258543021': 'file_storage/function-call-2439153792258543021.json'}

exec(code, env_args)
