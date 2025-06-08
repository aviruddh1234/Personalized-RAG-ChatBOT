from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import gradio as gr

model = OllamaLLM(model="llama3.2", temperature=0.7)

template = """
You are an expert in answering questions about a personalized trip organizer buisness named GuavaTrips 

Here are some relevant reviews: {reviews}

Here is a question about the business: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


# ...existing code...

def guava_trips_chatbot(question):
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    return result

iface = gr.Interface(
    fn=guava_trips_chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Ask a question about GuavaTrips..."),
    outputs="text",
    title="GuavaTrips Chatbot",
    description="Ask any question about the personalized trip organizer business, GuavaTrips!"
)

if __name__ == "__main__":
    iface.launch()