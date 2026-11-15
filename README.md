# Complete Naive RAG

<p align="center">
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white"></a>
  <a href="https://streamlit.io/"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white"></a>
  <a href="https://www.langchain.com/"><img alt="LangChain" src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?logo=chainlink&logoColor=white"></a>
  <a href="https://www.trychroma.com/"><img alt="Chroma" src="https://img.shields.io/badge/Chroma-vector%20store-5B4BDB"></a>
  <a href="https://ai.google.dev/gemini-api"><img alt="Google Gemini" src="https://img.shields.io/badge/Google%20Gemini-API-4285F4?logo=googlegemini&logoColor=white"></a>
  <a href="https://huggingface.co/"><img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-models-FFD21E?logo=huggingface&logoColor=black"></a>
  <a href="https://huggingface.co/docs/transformers"><img alt="Transformers" src="https://img.shields.io/badge/Transformers-text%20generation-FFD21E?logo=huggingface&logoColor=black"></a>
  <a href="https://pytorch.org/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-local%20inference-EE4C2C?logo=pytorch&logoColor=white"></a>
  <a href="https://www.sbert.net/"><img alt="Sentence Transformers" src="https://img.shields.io/badge/Sentence%20Transformers-embeddings-3C78A9"></a>
  <a href="https://pypdf.readthedocs.io/"><img alt="pypdf" src="https://img.shields.io/badge/pypdf-PDF%20loading-3776AB"></a>
</p>

<p align="center">
  <img src="project-banner.svg" alt="Complete Naive RAG — retrieval-augmented question answering" width="100%">
</p>

**Complete Naive RAG** is a learning project that demonstrates retrieval-augmented generation (RAG) through two small applications. One indexes a set of web pages and answers questions with a local Hugging Face model. The other accepts a PDF and uses Google Gemini for embeddings and answer generation. Jupyter notebooks walk through the underlying RAG steps.

## Contents

- [What it does](#what-it-does)
- [How RAG works here](#how-rag-works-here)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Run the Gemini PDF app](#run-the-gemini-pdf-app)
- [Run the URL based app](#run-the-url-based-app)
- [Explore the notebooks](#explore-the-notebooks)
- [Configuration and limitations](#configuration-and-limitations)
- [Roadmap](#roadmap)
- [Contact](#contact)

## What it does

### Gemini PDF question answering

The Streamlit interface in `RAG with Gemeni/app.py` lets you upload a PDF and ask questions about its contents. It loads the PDF, splits its text into chunks, embeds those chunks with Google's embedding API, retrieves up to ten similar chunks from Chroma, and sends the retrieved context to Gemini 1.5 Pro to produce an answer.

### URL based question answering

The root `app.py` loads three example Victoria On Move pages, splits their contents into chunks, embeds them with `sentence-transformers/all-MiniLM-L6-v2`, and uses Chroma plus a local DistilGPT-2 text-generation pipeline to answer questions. Update the URL list in `app.py` to index other pages.

### Notebook walkthroughs

- `naive-rag.ipynb` demonstrates the URL loading, chunking, embedding, retrieval, and local generation workflow.
- `RAG with Gemeni/RAG with Gemeni.ipynb` contains the PDF and Gemini experiment.

## How RAG works here

```text
Source (web pages or PDF)
          ↓
     Load content
          ↓
  Split into text chunks
          ↓
 Create vector embeddings
          ↓
 Store and retrieve with Chroma
          ↓
 Give relevant context to an LLM
          ↓
       Answer question
```

## Project structure

```text
Complete-Naive-RAG/
├── app.py                              # URL based Streamlit app (Hugging Face)
├── naive-rag.ipynb                     # URL based RAG notebook
├── project-banner.svg                  # README banner
├── RAG implemention app.png            # Screenshot of the URL based app
└── RAG with Gemeni/
    ├── app.py                          # PDF upload Streamlit app (Google Gemini)
    ├── RAG with Gemeni.ipynb           # Gemini notebook
    ├── RAG with Gemeni app.png          # Screenshot of the PDF app
    └── my_paper.pdf                    # Example PDF
```

## Requirements

- Python 3.10 or newer
- pip and a virtual environment
- A Google AI API key to run the Gemini PDF app
- Internet access to download model files and, for the URL app, fetch its configured web pages

The applications use different integrations. Install the dependencies for the app you intend to run.

## Run the Gemini PDF app

1. Clone this repository and create a virtual environment:

   ```bash
   git clone https://github.com/Md-Emon-Hasan/Complete-Naive-RAG.git
   cd Complete-Naive-RAG
   python -m venv .venv
   ```

   Activate it before continuing:

   ```bash
   # Windows PowerShell
   .venv\Scripts\Activate.ps1

   # macOS / Linux
   source .venv/bin/activate
   ```

2. Install the Gemini app packages:

   ```bash
   python -m pip install --upgrade pip
   pip install streamlit python-dotenv pypdf langchain langchain-community langchain-chroma langchain-google-genai
   ```

3. Create a `.env` file in the repository root and add your key:

   ```dotenv
   GOOGLE_API_KEY=your_google_ai_api_key
   ```

   Create a key in [Google AI Studio](https://aistudio.google.com/apikey). Keep the key private and do not commit `.env`.

4. Start the app from the repository root:

   ```bash
   streamlit run "RAG with Gemeni/app.py"
   ```

5. Upload a PDF, wait for indexing, and enter a question in the app.

## Run the URL based app

1. Create and activate a virtual environment as described above.
2. Install the URL app packages:

   ```bash
   python -m pip install --upgrade pip
   pip install streamlit langchain langchain-community langchain-huggingface chromadb sentence-transformers transformers torch unstructured
   ```

3. Run the app from the repository root:

   ```bash
   streamlit run app.py
   ```

The app loads its configured URLs and model when Streamlit executes the script. The first run may take longer while the embedding and generation models download. This version runs DistilGPT-2 locally and may need additional memory and setup depending on your machine.

## Explore the notebooks

Install Jupyter if needed, then open either notebook:

```bash
pip install notebook
jupyter notebook
```

Run the cells in order. The URL notebook follows the local Hugging Face workflow; the Gemini notebook requires a valid `GOOGLE_API_KEY` and the packages used by the PDF app.

## Configuration and limitations

- The Gemini app expects a `GOOGLE_API_KEY` environment variable and uses the Gemini 1.5 Pro and `embedding-001` model identifiers currently written in the code. Availability of model identifiers depends on Google's API access and may change.
- The Gemini app's PDF upload currently uses a temporary file and an in-memory Chroma store. Documents are not persisted as a reusable index between app runs.
- The URL app uses a fixed sample URL list and a local DistilGPT-2 model. Change the URLs in `app.py` to use other web content.
- The examples are educational prototypes. Retrieval quality depends on the source text, chunking, embedding model, and language model; answers can be incomplete or incorrect.
- Do not upload sensitive documents to an API-backed workflow unless you have checked the relevant provider's data handling terms.

## Roadmap

- Add configurable chunk size, overlap, and retrieval settings.
- Show source passages alongside answers.
- Add dependency lock files and automated checks for a reproducible setup.
- Improve error handling and document processing for large or scanned PDFs.

## 📬 Connect With Me

- 🌐 **Portfolio:** [emonlabs-ai.hitechparks.com](https://emonlabs-ai.hitechparks.com)
- 💻 **GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)
- 💼 **LinkedIn:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan-695483237/)
- 🤗 **Hugging Face:** [emonHasan01](https://huggingface.co/emonHasan01)
- 📧 **Email:** [emon.mlengineer@gmail.com](mailto:emon.mlengineer@gmail.com)
- 📱 **WhatsApp:** [+880 1834-363533](https://wa.me/8801834363533)

---

If you find this project useful for learning, feel free to star the repository or connect with me.
