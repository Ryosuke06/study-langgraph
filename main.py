from typing import Literal
from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict
from src.sample.utils.nodes import (
    call_model,
    should_continue,
    tool_node,
)
from src.sample.utils.state import AgentState

# 超おまじないです。
workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("action", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END,
    },
)
workflow.add_edge("action", "agent")

# StateGraphをコンパイルしたものを変数として置いておきます。
graph = workflow.compile()