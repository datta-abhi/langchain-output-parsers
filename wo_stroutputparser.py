from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# input arguments
topic = "Need for data governance for banking institution."

# instantiate model
model = ChatOllama(model="llama3.2")


# 1st prompt to create a detailed report on a topic
template1 = ChatPromptTemplate([
    ('system',"You are a helpful research assistant who gives detailed reports."),
    ('human',"Write a detailed_report on {topic}")])

chain1 = template1 | model
response1 = chain1.invoke({'topic': topic})
cleaned_response1 = response1.content
print(cleaned_response1)
print('--'*30)

# 2nd prompt to summarize from detailed report
template2 = ChatPromptTemplate([
    ('system',"You are a helpful research assistant who summarizes detailed reports coherently."),
    ('human',"Create a summary in 3 bullet points from the following report. \n {text}")])


chain2 = template2 | model
response2 = chain2.invoke({'text': cleaned_response1})
cleaned_response2 = response2.content
print(cleaned_response2)