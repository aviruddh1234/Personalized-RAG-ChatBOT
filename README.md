# Trip Organizer RAG Chatbot

This project is an AI-powered chatbot that answers questions about a personalized trip organizer business using Retrieval-Augmented Generation (RAG). It retrieves relevant customer reviews and generates context-aware responses using a language model. The chatbot is accessible through a simple Gradio web interface.

## Features

- **Retrieval-Augmented Generation (RAG):** Combines information retrieval and language generation for accurate, grounded answers.
- **Customer Review Integration:** Uses real customer reviews to provide contextually relevant responses.
- **Gradio Interface:** User-friendly web interface for easy interaction.

## Prerequisites

- **Ollama:**  
  You must install [Ollama](https://ollama.com/) on your system.

- **Pull the required models:**  
  Open your terminal and run:
  ```sh
  ollama pull llama3.2
  ollama pull <embedding-model-name>
  ```
  Replace `<embedding-model-name>` with the embedding model you use in your `vector.py`.

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repo-url>
    cd <project-folder>
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the chatbot:**
    ```sh
    python main.py
    ```

4. **Access the interface:**  
   Open the local URL provided by Gradio in your browser.

## File Structure

- `main.py` — Main application file containing the RAG pipeline and Gradio interface.
- `vector.py` — Contains the retriever logic for fetching relevant reviews.
- `requirements.txt` — Python dependencies.

## Example Usage

Ask questions like:
- "What do customers say about the trip planning service?"
- "How responsive is the support team?"
- "Are the trips customizable?"

## Project Description

An AI chatbot using Retrieval-Augmented Generation (RAG) to answer questions about a personalized trip organizer. It retrieves relevant reviews and generates responses via a simple Gradio web interface.

---

**Note:**  
Replace `<repo-url>`, `<project-folder>`, and `<embedding-model-name>` with your actual repository URL, folder name, and embedding model name.
