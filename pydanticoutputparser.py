
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# getting api keys from env file
load_dotenv()

# instantiate model
# Note: it is throwing error for Ollama Llama 3.2 model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# defining schema as Pydantic object
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description= "Age of person in years")
    city: str = Field(description= "City in India that person belongs to")

# instantiate pydantic parser
parser = PydanticOutputParser(pydantic_object= Person)  

# create prompt for LLM
template = PromptTemplate.from_template("Create a fictional person with name, age and city in the following format: \n {format_instructions}")

# create partial prompt with format instructions
partial_template = template.partial(format_instructions = parser.get_format_instructions())

# chaining
chain = partial_template | model | parser

response = chain.invoke({})
print(response) 