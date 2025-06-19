# 🕵️‍♂️ AI-Based FIR Analysis System

This project leverages artificial intelligence to assist law enforcement agencies in analyzing First Information Reports (FIRs). It extracts key information from FIR text, classifies the type of crime, summarizes the content, and finds similar past FIRs to help identify potential suspects or related cases.

---

## 🚀 Features

- 🧠 **Named Entity Recognition (NER):** Extracts key entities like names, locations, and dates from FIRs.
- 🏷️ **Crime Classification:** Identifies the type of crime (e.g., Theft, Assault) using keyword-based logic.
- ✂️ **FIR Summarization:** Generates concise summaries from FIR content.
- 🔍 **Similarity Detection:** Compares current FIR with past FIRs using TF-IDF and cosine similarity to find relevant matches.
- 🧩 **Modular Design:** Clean separation of logic into reusable modules (`classifier.py`, `ner_extractor.py`, `summarizer.py`, `similarity.py`).

---

## 🛠 Technologies Used

- Python
- Scikit-learn (`TfidfVectorizer`, `cosine_similarity`)
- Basic NLP techniques
- File I/O for FIR text handling

---

## 🗂️ Project Structure
fir-analysis/
├── main.py
├── classifier.py
├── ner_extractor.py
├── summarizer.py
├── similarity.py
├── sample_fir.txt


---

## 📌 How It Works

1. Load FIR text from a file (`sample_fir.txt`)
2. Extract named entities (e.g., names, locations, dates)
3. Classify the crime type using keyword logic
4. Generate a summary using sentence slicing
5. Compare with past FIRs to find similar cases

---

## 🖥️ Sample Output
--- Named Entities ---
{'Name': 'John Doe', 'Location': 'Hyderabad', 'Date': '2023-05-12'}

--- FIR Classification ---
Category: Theft

--- Summary ---
A mobile phone was stolen near the park on May 10th.
--- Similar Past FIRs ---
A mobile phone was stolen near the park on May 10th. (Similarity: 0.73)
A robbery occurred in the local bank on April 3rd. (Similarity: 0.52)
---
## ▶️ Run the App
bash:->Run the Project
python main.py
Make sure your working directory contains:

sample_fir.txt
All .py files mentioned above
📖 Future Improvements
Integrate a trained ML/NLP model for classification instead of rule-based logic
Use a real NER model (like spaCy or transformers)
Web dashboard for interactive analysis

📂 License
This project is open-source and available under the MIT License.
