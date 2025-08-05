from functools import lru_cache

from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from src.utils.state import AgentState
from src.utils.tools import tools

# OpenAIのクライアント呼び出す。
@lru_cache(maxsize=4)
def _get_model():
    model = ChatOpenAI(temperature=0, model="gpt-4o-mini").bind_tools(tools)
    return model


# 今は何だこれと思っててOK。Function CallingというOpenAI APIの機能で使われます。
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"

system_prompt = """Be a helpful assistant"""

# OpenAIのモデル呼び出して、prompt組んで、発行する関数
def call_model(state: AgentState, config: RunnableConfig):
    messages = state["messages"]
    messages = [{"role": "system", "content": system_prompt}] + list(messages)
    model = _get_model()
    response = model.invoke(messages)
    
    return {"messages": [response]}

# 次の次の説明で登場
tool_node = ToolNode(tools)