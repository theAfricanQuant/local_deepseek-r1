# Local LLM Chatbot with DeepSeek-R1, Streamlit and Langchain

A local chatbot implementation using Deep Seek R1 model, LangChain, and Streamlit.

## Prerequisites

- Windows OS
- Python 3.10.11
- Git
- GitHub account
- Visual Studio Code
- Minimum 5GB free storage space
- Recommended: GPU with sufficient RAM

## Step-by-Step Setup

### 1. Install Ollama
1. Visit [ollama.com](https://ollama.com)
2. Download and install for Windows
3. Verify installation:
```bash
ollama --version
```

### 2. Install Deep Seek R1 Model
```bash
ollama run deep-seek-r1:7b
```

Verify installation:
```bash
ollama list
```

### 3. Set Up Project Repository
1. Create new repository on GitHub
2. Clone locally:
```bash
git clone <your-repo-url>
cd <repo-name>
code .  # Opens VS Code
```

### 4. Install UV Package Manager
Option 1 (Recommended):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
To update UV later:
```bash
uv self update
```

Option 2:
```bash
pip install uv
```


### 5. Initialize Python Environment
```bash
uv init --python 3.10.11
```

### 6. Install Required Packages
```bash
uv add ipykernel langchain langchain-community langchain-ollama streamlit
```

### 7. Create Application Code
Change `hello.py` given to you by uv to `app.py`. The code in the file can be found in this repo.


### 8. Run the Application in Powershell
```bash
streamlit run app.py
```
Access via:
- Local URL: http://localhost:8502
- Network URL: http://192.168.0.59:8502

## Usage
1. Ensure Ollama is running
2. Start the Streamlit app
3. Enter questions in the chat input
4. View model responses in real-time

## Troubleshooting
- If UV commands fail, ensure PowerShell is running as administrator
- Verify Ollama is running before starting Streamlit
- Check port 8502 availability for Streamlit
- Ensure all packages are properly installed in the UV environment

## Model Information
- Using Deep Seek R1 7B parameter model
- Size: ~4.7GB
- All processing happens locally
- No internet required for inference