from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableBranch,
    RunnablePassthrough,
)
from dotenv import load_dotenv

load_dotenv()

# ✅ Gemini 1.5 Flash model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# ✅ Prompt to generate a detailed report
prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# ✅ Prompt to summarize long content
prompt2 = PromptTemplate(
    template='Summarize the following text:\n{text}',
    input_variables=['text']
)

# ✅ Output parser
parser = StrOutputParser()

# ✅ Report generation chain
report_gen_chain = prompt1 | model | parser

# ✅ Conditional summarization branch
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, prompt2 | model | parser),
    RunnablePassthrough()
)

# ✅ Final chain
final_chain = RunnableSequence(report_gen_chain, branch_chain)

# ✅ Run the chain
result = final_chain.invoke({'topic': 'Russia vs Ukraine'})

print(result)
