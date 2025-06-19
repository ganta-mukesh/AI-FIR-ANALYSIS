from .summarizer import summarize_fir

def find_similar_firs(query_text):
    firs = [
        {
            "text": "On 10th May 2023, a robbery took place in the MG Road area of Bangalore. The victim reported the loss of a mobile phone and cash.",
            "score": 0.13
        },
        {
            "text": "An accident occurred on 8th April 2023 at Andheri East, Mumbai. Two vehicles were involved and one person was injured.",
            "score": 0.07
        },
        {
            "text": "A burglary was reported on 2nd March 2023 at a residence in Sector 15, Gurgaon, where electronic items were stolen.",
            "score": 0.04
        }
    ]

    for fir in firs:
        fir["summary"] = summarize_fir(fir["text"])

    return firs