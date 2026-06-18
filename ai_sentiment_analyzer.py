import re

def analyze_ai_sentiment(text):
    """
    Analyzes the sentiment of a given text towards AI based on predefined Turkish keywords.
    This simulates a very basic form of Natural Language Processing (NLP)
    that was a foundational concept even as deep learning advanced in 2017.
    """
    text = text.lower() # Convert to lowercase for case-insensitive matching

    # Keywords reflecting concerns about AI, as discussed by the anti-AI activist in 2017
    concern_keywords = [
        "endişe", "risk", "tehdit", "etik", "sorun", "kontrol", "korku",
        "aktivist", "yansıma", "tartışma", "kaygı", "zarar"
    ]

    # Keywords reflecting optimism or potential of AI, as felt by tech enthusiasts in 2017
    optimism_keywords = [
        "potansiyel", "gelişim", "heyecan", "fırsat", "ilerleme", "çözüm",
        "yenilik", "akıllı", "makine öğrenimi", "derin öğrenme", "otomasyon", "fayda"
    ]

    concern_score = 0
    optimism_score = 0

    # Check for concern keywords
    for keyword in concern_keywords:
        # Use regex for whole word matching to avoid partial matches (e.g., 'etiket' containing 'etik')
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            concern_score += 1

    # Check for optimism keywords
    for keyword in optimism_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            optimism_score += 1

    # Determine overall sentiment based on scores
    if concern_score > optimism_score:
        return "Endişe/Olumsuz (Concern/Negative)", concern_score, optimism_score
    elif optimism_score > concern_score:
        return "Potansiyel/Olumlu (Potential/Positive)", concern_score, optimism_score
    else:
        if concern_score == 0 and optimism_score == 0:
            return "Nötr/Belirsiz (Neutral/Unclear)", concern_score, optimism_score
        else:
            return "Karışık (Mixed)", concern_score, optimism_score

if __name__ == "__main__":
    print("Yapay Zeka Metin Duygu Analizcisi (Basit Keyword Tabanlı)")
    print("-------------------------------------------------------")
    print("2017'deki Yapay Zeka tartışmalarını yansıtan basit bir metin analizi.")
    print("Çıkmak için 'q' yazın.")
    print("")

    # Example sentences reflecting the article's context (Turkish)
    examples = [
        "Yapay zeka teknolojilerinin etik sorunları hakkında derin endişelerim var.",
        "Makine öğrenimi ve derin öğrenme, gelecekte büyük potansiyel taşıyor.",
        "Bir anti-YZ aktivisti, teknolojinin kontrol dışı kalma riskini vurguladı.",
        "Yapay zeka alanındaki gelişmeler heyecan verici fırsatlar sunuyor.",
        "Bu sadece bir deneme metni, özel bir anlamı yok.",
        "Yapay zeka ilerleme kaydediyor ancak etik kaygılar da artıyor."
    ]

    for i, example_text in enumerate(examples):
        print(f"Örnek {i+1}: \"{example_text}\"")
        sentiment, concern_score, optimism_score = analyze_ai_sentiment(example_text)
        print(f"  Analiz Sonucu: {sentiment}")
        print(f"  Endişe Skoru: {concern_score}, Potansiyel Skoru: {optimism_score}")
        print("-" * 30)

    while True:
        user_input = input("\nMetin girin (veya çıkmak için 'q'): ")
        if user_input.lower() == 'q':
            break
        if not user_input.strip():
            print("Lütfen geçerli bir metin girin.")
            continue

        sentiment, concern_score, optimism_score = analyze_ai_sentiment(user_input)
        print(f"Analiz Sonucu: {sentiment}")
        print(f"Endişe Skoru: {concern_score}, Potansiyel Skoru: {optimism_score}")

    print("\nÇıkış yapılıyor. Hoşça kalın!")
