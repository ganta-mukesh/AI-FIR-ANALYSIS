from models import ner_extractor, classifier, summarizer, similarity

def load_fir(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    fir_text = load_fir("sample_fir.txt")
    
    print("\n--- Named Entities ---")
    entities = ner_extractor.extract_entities(fir_text)
    print(entities)

    print("\n--- FIR Classification ---")
    category = classifier.classify_fir(fir_text)
    print(f"Category: {category}")

    print("\n--- Summary ---")
    summary = summarizer.summarize_fir(fir_text)
    print(summary)

    print("\n--- Similar Past FIRs ---")
    similar_cases = similarity.find_similar_firs(fir_text)
    for case in similar_cases:
        summary_text = case.get('summary', 'No summary available')
        print(f"- {summary_text} (Similarity: {case['score']:.2f})")

if _name_ == "_main_":
    main()