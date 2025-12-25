code = """import json
import re

# Load the articles
# Check if the variable is a string (file path) or list
data = locals()['var_function-call-16647193750153873959']
if isinstance(data, str):
    if data.endswith('.json'):
        with open(data, 'r') as f:
            articles = json.load(f)
    else:
        # It might be the truncated string if something went wrong, but usually it's a file path if large
        # Or it might be a list if it wasn't too large.
        articles = data # Assuming it's the data if not file path
else:
    articles = data

# Define keywords
scitech_keywords = {
    "science", "technology", "tech", "computer", "internet", "web", "software", "hardware", "digital", "network", "data", "cyber", 
    "virus", "hacker", "security", "robot", "ai", "artificial", "intelligence", "space", "nasa", "astronomy", "mars", "moon", 
    "planet", "galaxy", "universe", "physics", "chemistry", "biology", "genetics", "dna", "stem", "clone", "medical", "health", 
    "disease", "cancer", "aids", "hiv", "flu", "vaccine", "drug", "therapy", "doctor", "hospital", "research", "study", "laboratory", 
    "experiment", "energy", "power", "solar", "wind", "nuclear", "engine", "battery", "phone", "mobile", "cellphone", "smartphone", 
    "app", "tablet", "laptop", "gadget", "device", "video", "game", "gaming", "nintendo", "sony", "xbox", "playstation", "wii", 
    "microsoft", "google", "apple", "amazon", "facebook", "intel", "ibm", "linux", "windows", "browser", "search", "engine", "email", 
    "online", "blog", "wireless", "broadband", "satellite", "telecom", "nanotech", "innovation", "scientist", "telescope", "microscope",
    "biotech", "fossil", "fuel", "climate", "warming", "environment", "pollution", "emission", "carbon"
}

business_keywords = {
    "business", "economy", "economic", "finance", "financial", "market", "stock", "share", "wall", "street", "dow", "jones", "nasdaq", 
    "invest", "investor", "profit", "loss", "revenue", "earnings", "sales", "trade", "deal", "merger", "acquisition", "buyout", "bank", 
    "banking", "interest", "rate", "inflation", "tax", "budget", "deficit", "currency", "dollar", "euro", "yen", "oil", "gas", "price", 
    "cost", "consumer", "retail", "corp", "corporation", "company", "firm", "industry", "sector", "ceo", "cfo", "manager", "executive", 
    "employment", "job", "unemployment", "labor", "strike", "union", "wto", "imf", "fed", "federal", "reserve", "treasury", "growth",
    "recession", "bankruptcy", "dividend", "shareholder"
}

sports_keywords = {
    "sport", "football", "soccer", "baseball", "basketball", "hockey", "cricket", "rugby", "tennis", "golf", "boxing", "racing", "f1", 
    "formula", "one", "nascar", "olympic", "athlete", "player", "team", "coach", "manager", "club", "league", "tournament", "championship", 
    "cup", "medal", "score", "goal", "touchdown", "homerun", "basket", "point", "win", "lose", "draw", "match", "game", "season", 
    "playoff", "final", "stadium", "arena", "fan", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "premier", "world", "super", "bowl",
    "quarterback", "receiver", "pitcher", "striker", "goalkeeper", "wimbledon", "masters", "tour"
}

world_keywords = {
    "world", "international", "global", "nation", "country", "state", "government", "politics", "political", "politician", "president", 
    "prime", "minister", "senate", "congress", "parliament", "election", "vote", "voter", "campaign", "party", "democrat", "republican", 
    "conservative", "liberal", "socialist", "communist", "dictator", "regime", "leader", "official", "diplomat", "ambassador", "treaty", 
    "summit", "conference", "war", "peace", "conflict", "fight", "battle", "army", "military", "soldier", "troops", "navy", "air", "force", 
    "weapon", "bomb", "blast", "explosion", "attack", "terror", "terrorism", "terrorist", "al", "qaeda", "iraq", "iran", "afghanistan", 
    "israel", "palestine", "syria", "russia", "china", "usa", "uk", "france", "germany", "un", "united", "nations", "eu", "european", "union", 
    "nato", "police", "crime", "court", "law", "judge", "justice", "prison", "protest", "riot", "demonstration", "disaster", "earthquake", 
    "tsunami", "flood", "hurricane", "storm", "famine", "refugee", "human", "rights", "foreign", "policy", "korea"
}

def categorize(title, description):
    text = (title + " " + description).lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    
    scores = {
        "Science/Technology": 0,
        "Business": 0,
        "Sports": 0,
        "World": 0
    }
    
    for word in words:
        if word in scitech_keywords: scores["Science/Technology"] += 1
        if word in business_keywords: scores["Business"] += 1
        if word in sports_keywords: scores["Sports"] += 1
        if word in world_keywords: scores["World"] += 1
    
    # Heuristics for ambiguity
    # "Game": if video/console -> Tech, else if team/score -> Sports
    if "game" in words or "games" in words:
        tech_context = any(w in words for w in ["video", "console", "nintendo", "xbox", "ps2", "ps3", "computer", "software", "online"])
        sports_context = any(w in words for w in ["team", "coach", "league", "cup", "score", "win", "season", "football", "baseball"])
        if tech_context and not sports_context:
            scores["Science/Technology"] += 3
        elif sports_context and not tech_context:
            scores["Sports"] += 3
    
    # "Oil": Business or Sci/Tech (energy)? Usually Business unless "environment" or "spill"
    if "oil" in words and "price" in words:
        scores["Business"] += 2
        
    # "Apple"/"Google": Business or Tech?
    if any(w in words for w in ["apple", "google", "microsoft"]):
        if any(w in words for w in ["stock", "market", "share", "profit", "revenue"]):
            scores["Business"] += 2
        else:
            scores["Science/Technology"] += 2
            
    # "Space": could be office space (Business) or Outer Space (Tech)
    # usually "space" alone is weak, but "nasa", "orbit" etc are strong.
    
    best_cat = max(scores, key=scores.get)
    # If all 0, default to World? Or Unknown?
    if scores[best_cat] == 0:
        return "World" # Default
        
    return best_cat

count_scitech = 0
total = len(articles)
results = []

for article in articles:
    cat = categorize(article.get('title', ''), article.get('description', ''))
    if cat == "Science/Technology":
        count_scitech += 1
    results.append({"id": article.get("article_id"), "title": article.get("title"), "cat": cat})

fraction = count_scitech / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "scitech_count": count_scitech,
    "fraction": fraction,
    "sample_results": results[:10]
}))"""

env_args = {'var_function-call-4900156496155206436': [{'author_id': '218'}], 'var_function-call-12198714421739599460': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15666126011967161689': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-16647193750153873959': [{'_id': '6944b9dddb8150d8433ea0cf', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b9dddb8150d8433ea880', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b9dddb8150d8433eab2b', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b9dddb8150d8433eabba', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b9dddb8150d8433ead8a', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
