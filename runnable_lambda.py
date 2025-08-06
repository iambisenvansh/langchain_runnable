from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# ✅ Define the Gemini model (1.5 Flash)
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# ✅ Simple function to count words
def word_count(text):
    return len(text.split())

# ✅ Prompt for joke generation
prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# ✅ Output parser
parser = StrOutputParser()

# ✅ Chain to generate the joke
joke_gen_chain = RunnableSequence(prompt, model, parser)

# ✅ Run joke and word count in parallel
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

# ✅ Final chain: Generate joke → pass into parallel → get joke + word count
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# ✅ Invoke the chain
result = final_chain.invoke({'topic': 'AI'})

# ✅ Format the result
final_result = f"{result['joke']}\nWord Count - {result['word_count']}"

print(final_result)
