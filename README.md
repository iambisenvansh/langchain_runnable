# LangChain Runnable Examples

This repository demonstrates the use of LangChain's powerful `Runnable` components including:

- `RunnableSequence`
- `RunnableParallel`
- `RunnablePassthrough`
- `RunnableLambda`
- `RunnableBranch`

Each file contains a runnable chain using **Gemini 1.5 Flash** from Google Generative AI via the LangChain interface.

---

## 🔧 Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/langchain_runnable.git
cd langchain_runnable
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables

Create a .env file and add your Google API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_api_key_here
📂 File Overview
File Name	Description
runnable_sequence.py	Chains prompts and models in a linear sequence
runnable_parallel.py	Runs multiple prompts in parallel (e.g., tweet + LinkedIn post)
runnable_passthrough.py	Shows how to pass data directly through one step
runnable_lambda.py	Applies a custom Python function like word count
runnable_branch.py	Dynamically switches prompt path based on conditions

💡 Tech Stack
LangChain

Google Gemini 1.5 Flash API

Python 3.10+

dotenv

🚀 Run an Example
bash
Copy
Edit
python runnable_sequence.py
