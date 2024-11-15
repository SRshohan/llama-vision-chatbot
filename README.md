# Llama-Vision Chatbot

A multimodal chatbot powered by the `llama-vision` model, Streamlit, and Ollama. This application allows users to interact with the chatbot using text and image inputs.

## Prerequisites

- Python 3.7+
- Access to `llama-vision` model through Ollama

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/llama-vision-chatbot.git
cd llama-vision-chatbot
```
### 2. Create a Virtual Environment
To keep your dependencies organized and isolated, create a virtual environment.
```bash
python3 -m venv venv
```

#### Activate the virtual environment:

On macOS/Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
Install the necessary Python packages using requirements.txt.

```bash
pip install -r requirements.txt
```
The requirements.txt file should include dependencies such as:

- streamlit
- ollama 

### 4. Install Ollama and llama-vision Model
#### Install Ollama
Ollama provides access to `llama-vision`. Follow these steps in the [Download and Installation Guide](https://ollama.com/download).
Download the llama-vision Model
Once Ollama is installed, download the llama-vision model:
```bash
ollama pull llama3.2-vision
```

### 5. Run the Streamlit Server
Start the Streamlit server to launch the chatbot application:

```bash
streamlit run app.py
```


### Explanation of Sections

- **Prerequisites**: Lists requirements such as Python and `llama-vision`.
- **Installation and Setup**: Detailed setup instructions, with appropriate command formatting.
- **Usage**: Instructions on interacting with the chatbot.
- **Contributing**: Steps for contributing to the project.
- **License**: Placeholder for licensing information.


