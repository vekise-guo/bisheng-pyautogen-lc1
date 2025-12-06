from autogen.agentchat.assistant_agent import AssistantAgent

def test_assistant_agent_init():
    agent = AssistantAgent(name="assistant")
    assert agent.name == "assistant"
    assert agent.system_message == AssistantAgent.DEFAULT_SYSTEM_MESSAGE
    assert agent.human_input_mode == "NEVER"
