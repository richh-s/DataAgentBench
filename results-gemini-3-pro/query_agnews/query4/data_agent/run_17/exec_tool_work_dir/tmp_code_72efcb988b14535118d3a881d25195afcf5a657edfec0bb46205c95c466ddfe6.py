code = """import json
import re
from collections import Counter

with open(locals()['var_function-call-10118669966329867769'], 'r') as f:
    id_data = json.load(f)
    target_ids = set(id_data['article_ids'])
    id_to_region = {int(k): v for k, v in id_data['id_to_region'].items()}

with open(locals()['var_function-call-10182139380038142378'], 'r') as f:
    articles = json.load(f)

relevant_articles = [a for a in articles if int(a['article_id']) in target_ids]

base_categories = {
    "Sports": ["sport", "game", "cup", "match", "team", "win", "won", "loss", "lost", "score", "olympic", "championship", "champion", "league", "football", "baseball", "basketball", "hockey", "tennis", "golf", "soccer", "athlete", "coach", "medal", "tournament", "stadium", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "racing", "driver", "f1", "cricket", "rugby", "player", "club", "fc", "united", "city", "real", "barcelona", "chelsea", "arsenal", "liverpool", "manchester", "milan", "juventus", "bayern", "munich", "athens", "beijing", "race", "circuit", "lap", "round", "final", "semifinal", "quarterfinal", "referee", "foul", "penalty", "goal", "touchdown", "homerun", "strikeout", "inning", "boxing", "wrestling", "swimming", "track", "field", "marathon", "sprint", "gold", "silver", "bronze", "defeat", "beat", "victory", "triumph", "hit", "run", "basket"],
    
    "Business": ["oil", "price", "market", "stock", "share", "trade", "profit", "loss", "economy", "economic", "bank", "company", "firm", "corp", "inc", "ceo", "cfo", "merger", "acquisition", "deal", "dollar", "euro", "yen", "currency", "inflation", "rate", "fed", "reserve", "wall street", "nasdaq", "dow", "invest", "revenue", "sales", "quarter", "growth", "budget", "deficit", "finance", "financial", "retail", "store", "shop", "consumer", "customer", "brand", "advertising", "marketing", "manager", "executive", "board", "shareholder", "dividend", "yield", "bond", "asset", "liability", "debt", "loan", "mortgage", "housing", "real estate", "manufacturing", "industry", "sector", "production", "gm", "ford", "toyota", "boeing", "airbus", "airline", "wal-mart", "mcdonalds", "starbucks", "coke", "pepsi", "job", "workforce", "layoff", "hiring", "unemployment", "chrysler", "santander"],
    
    "Sci/Tech": ["technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "microsoft", "google", "apple", "intel", "ibm", "server", "chip", "science", "space", "nasa", "orbit", "research", "study", "scientist", "drug", "virus", "cancer", "medical", "phone", "mobile", "wireless", "broadband", "satellite", "robot", "linux", "browser", "spam", "hacker", "digital", "gadget", "astronomy", "planet", "galaxy", "universe", "telescope", "physics", "biology", "chemistry", "lab", "laboratory", "experiment", "discovery", "environment", "climate", "global warming", "pollution", "energy", "fuel", "engine", "network", "system", "data", "device", "screen", "display", "video", "audio", "camera", "image", "file", "download", "upload", "user", "app", "application", "program", "code", "developer", "videogame", "console", "ipod", "itunes", "firefox", "explorer", "windows", "yahoo", "amazon", "ebay", "aol", "blog"],
    
    "World": ["war", "peace", "military", "army", "troop", "soldier", "rebel", "attack", "kill", "dead", "died", "bomb", "blast", "president", "minister", "parliament", "government", "official", "election", "vote", "party", "leader", "politic", "congress", "senate", "bush", "kerry", "putin", "blair", "iraq", "iran", "israel", "palestine", "gaza", "syria", "afghanistan", "darfur", "sudan", "russia", "china", "un", "united nations", "treaty", "nuclear", "weapon", "crisis", "hostage", "terror", "police", "court", "law", "legal", "trial", "judge", "security", "protest", "strike", "talks", "diplomat", "foreign", "international", "hurricane", "storm", "typhoon", "quake", "tsunami", "country", "nation", "state", "region", "border", "territory", "island", "city", "capital", "village", "town", "people", "citizen", "refugee", "immigrant", "migration", "human rights", "democracy", "dictator", "regime", "coup", "rebellion", "insurgent", "militant", "terrorist", "terrorism", "al-qaeda", "bin laden", "saddam", "arafat", "sharon", "rice", "powell", "rumsfeld", "ukraine", "lebanon", "egypt", "saudi", "korea", "indonesia", "pakistan", "india", "kashmir", "nepal", "haiti", "venezuela", "colombia", "german", "germany", "french", "france", "british", "britain", "uk", "spanish", "spain", "italian", "italy", "european", "african", "asian", "american", "latin", "middle east", "migrant", "rally", "riot", "demonstration", "clash", "violence", "arrest", "jail", "prison", "parade", "ceremony", "royal", "queen", "king", "prince", "pope", "vatican", "religion", "catholic", "muslim", "islam", "jewish", "christian", "priest", "bishop", "malaysia", "thailand", "vietnam", "philippines", "australia", "canada", "mexico", "brazil", "argentina", "chile", "peru", "libya", "nigeria", "kenya", "south africa", "zimbabwe", "congo"]
}

categories = {}
for cat, keywords in base_categories.items():
    expanded = set(keywords)
    for k in keywords:
        expanded.add(k + "s") # simple plural
    categories[cat] = list(expanded)

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    words = re.findall(r'\w+', text)
    for word in words:
        for cat, keywords in categories.items():
            if word in keywords:
                scores[cat] += 1
    
    # Heuristics
    if "iraq" in text or "baghdad" in text: scores["World"] += 2
    if "olympic" in text: scores["Sports"] += 5
    if "microsoft" in text or "google" in text: scores["Sci/Tech"] += 2
    if "stocks" in text or "dow jones" in text: scores["Business"] += 2
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

world_counts = Counter()
unknown_count = 0

for article in relevant_articles:
    text = article['title'] + " " + article['description']
    category = classify(text)
    if category == "World":
        aid = int(article['article_id'])
        region = id_to_region.get(aid)
        if region:
            world_counts[region] += 1
    elif category == "Unknown":
        unknown_count += 1

print("__RESULT__:")
print(json.dumps({"counts": world_counts, "unknown": unknown_count}))"""

env_args = {'var_function-call-13078718259946536180': 'file_storage/function-call-13078718259946536180.json', 'var_function-call-10118669966329867769': 'file_storage/function-call-10118669966329867769.json', 'var_function-call-3403215652805393396': 6696, 'var_function-call-1384210166536825512': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-1480447670109302999': [{'_id': '6944fdfd639e7f14cbca1f34', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6944fdfd639e7f14cbca1f35', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6944fdfd639e7f14cbca1f36', 'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'_id': '6944fdfd639e7f14cbca1f37', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '6944fdfd639e7f14cbca1f38', 'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-17543352879014527113': 5, 'var_function-call-10182139380038142378': 'file_storage/function-call-10182139380038142378.json', 'var_function-call-3079227003685926854': {'Africa': 565, 'North America': 569, 'Asia': 552, 'Europe': 567, 'South America': 563}, 'var_function-call-14908929006035691630': {'North America': ["What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'Bomb at India Independence Parade Kills 15 (AP)', 'Bombs explode at Nepal luxury hotel, no casualties (Reuters)', 'Suspected Militants Kidnap Iraqi Officer-Jazeera', 'Group Urges EPA for More Pollution Cuts (AP)'], 'Europe': ['News: Warmer Weather, Human Disturbances Interact to Change Forests', "Saturn's Moon Titan: Prebiotic Laboratory", 'News: U.S. tackles Emergency Alert System insecurity', 'Venezuela Opposition Holds Recall Vote', 'Chavez Declares Recall Victory; Foes Claim Fraud']}, 'var_function-call-14752654490867126625': {'counts': {'Asia': 345, 'North America': 352, 'Africa': 371, 'Europe': 352, 'South America': 366}, 'unknown': 593}, 'var_function-call-6833292709182129477': ["Chrysler's Bling King", "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'Marlins Defeat Dodgers 4-2 (AP)', 'German welfare rallies escalate', 'Migrants #39; ordeal ugly side of paradise', 'Williamson Gets Third Opinion on Elbow (AP)', 'Outspoken Winslow Makes Impression at Camp (AP)', "Malaysia's Sea Turtles Are in Trouble (AP)", 'Taylor Is Moving Closer', 'Clemens #39; leg injury isn #39;t serious', 'Yahoo Builds the Yahoo Search Blog', 'Sheppard makes semi-finals', 'Clean-up works on Norfolk Broads', 'Teens Claim to Set New TV-Viewing Record', 'Report: Consumers tuning in to plasma TVs', 'Sun goes down, Empire blows up', 'Away on Business: Making a Difference', 'Greece 88, Angola 56', 'Molina ties career high with four hits', 'Franchitti wins Pikes Peak after pit mishap', 'Santander Plans 3,000 Job Cuts at Abbey (AP)']}

exec(code, env_args)
