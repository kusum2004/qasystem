# QA System with PDF & Streamlit

A question-answering system over PDF documents, built using LLMs and deployed via a Streamlit app.  
This project ingests PDF files, creates embeddings, and enables users to ask questions interactively based on the content of those documents.

---

## 🚀 Features

- Load and parse PDF documents  
- Create text embeddings from document chunks  
- Store and query vector embeddings  
- Chat‑style interface using Streamlit  
- Supports querying large documents via retriever + LLM  
- Logging for debugging and monitoring  
- Optional notebook experiments for testing and development  

---

## 📁 Repository Structure

```
.
├── Data/                    # (Optional) sample or test data
├── Experiments/             # Notebooks and exploratory code
├── QAWithPDF/                # Main logic for ingestion, embedding, and querying
├── build/lib/QAWithPDF/       # Built package files
├── logs/                      # Log files
├── notebook/                  # Jupyter notebooks, intermediate stores
├── storage/                    # Serialized vector stores and docstores
├── StreamlitApp.py             # Main Streamlit app entry point
├── template.py                  # Optional templates or helper scripts
├── exception.py                 # Custom exception handling
├── logger.py                     # Logging setup
├── requirements.txt             # Python dependencies
├── setup.py                        # Package setup script
└── .gitignore                   # Defines files/folders to be ignored by Git
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/kusum2004/qasystem.git
   cd qasystem
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up credentials / API keys**  
   If you're using any external LLM APIs (e.g. Google Gemini, OpenAI, etc.), make sure to configure them via environment variables or config files according to your local setup.

5. **Run the Streamlit app**  
   ```bash
   streamlit run StreamlitApp.py
   ```
   Once running, you’ll get a local URL in the terminal. Open it in your browser to interact with the QA interface.

---

## 🎯 How to Use

- Upload or point to your PDF documents via the provided interface  
- The app will process the PDFs, create embeddings, and build a vector store  
- Then you can ask natural language questions and receive answers based on the document content

You can also explore the Jupyter notebooks in the `notebook/` folder for experimenting with:

- Custom chunking and embedding logic  
- Alternative retriever settings  
- Debugging and visualizing results

---

## 🛠️ Development Tips

- Use the notebooks in `Experiments/` to test out document ingestion and embedding logic  
- Check logs in `logs/` if something goes wrong  
- If you make changes to the core logic in `QAWithPDF/`, you can rebuild your package using:
  ```bash
  python setup.py install
  ```
- Consider adding a `.env` file or environment variables to manage sensitive API keys  

---

## ✅ Contributing

Feel free to open issues or pull requests!  
If you decide to extend this project, here are a few ideas:

- Support for more file formats (Word, TXT, etc.)  
- Embedding caching or incremental updates  
- More advanced prompt‑engineering or LLM backends  
- User authentication in Streamlit for multi-user access  
- Deployment on cloud platforms (Heroku, AWS, GCP, etc.)

---

## 📫 Contact

If you have questions or want to discuss this project further, you can reach me at: **kusumakusuma9347@gmail.com**
