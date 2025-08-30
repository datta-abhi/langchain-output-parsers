from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# input arguments
topic = "Need for data governance for banking institution."

# instantiate model
model = ChatOllama(model="llama3.2")

# instntiate parser
parser = StrOutputParser()

# 1st prompt to create a detailed report on a topic
template1 = ChatPromptTemplate([
    ('system',"You are a helpful research assistant who gives 500-600 word detailed reports."),
    ('human',"Write a detailed_report on {topic}")])

# 2nd prompt to summarize from detailed report
template2 = ChatPromptTemplate([
    ('system',"You are a helpful research assistant who summarizes detailed reports coherently."),
    ('human',"Create a summary in 3 short bullet points from the detailed report. \n {text}")])

# chaining templates and parser
chain = template1 | model | parser | template2 | model | parser

str_response = chain.invoke({'topic': topic})
print(str_response)
