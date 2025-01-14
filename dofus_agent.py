from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from tools.OCR import get_position, collect_item, get_item_quantities_in_inventory, move_to
from dofus_map import get_item_coordinates


system_prompt = """
You are an intelligent agent designed to play the game Dofus.
Your primary objective is to complete tasks provided in natural language.

Think step by step and use tools sequentially. After each tool call, evaluate whether the task is fully complete or if further actions are required. 

**Ensure that you perform all your actions sequentially, one at a time, and wait for each action to complete before moving to the next.**

Reason explicitly: "I have used [tool] and obtained [result]. Based on this, I need to [next step]."
Continue until the task is fully completed.

Do not invent anything, all your answer must be based on the tool outputs.
"""


# model = ChatOllama(model="llama3.1:8b", temperature=0) 

from langchain_groq import ChatGroq
import os
os.environ["GROQ_API_KEY"]
model = ChatGroq(model="llama3-70b-8192", temperature=0)




memory = MemorySaver()
tools = [get_position, collect_item, get_item_quantities_in_inventory, move_to, get_item_coordinates]
agent_executor = create_react_agent(model, tools, checkpointer=memory, state_modifier=system_prompt)
config = {"configurable": {"thread_id": "abc123"}}



# inputs = {"messages": [("user", "move the player to 3, -15")]}
# for s in agent_executor.stream(inputs, config, stream_mode="values"):
#     message = s["messages"][-1]
#     if isinstance(message, tuple):
#         print(message)
#     else:
#         message.pretty_print()


inputs = {"messages": [("user", "Go harvest some 'ble' nearby")]}
for s in agent_executor.stream(inputs, config, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()



inputs = {"messages": [("user", "Go collect some 'ble' until I have at least 50 ")]}
for s in agent_executor.stream(inputs, config, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()



inputs = {"messages": [("user", "Collect the ble ")]}
for s in agent_executor.stream(inputs, config, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()



inputs = {"messages": [("user", "What are my coordinates ?")]}
for s in agent_executor.stream(inputs, config, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()





inputs = {"messages": [("user", "How many ble, ortie do i have ? ")]}
for s in agent_executor.stream(inputs, config, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()



