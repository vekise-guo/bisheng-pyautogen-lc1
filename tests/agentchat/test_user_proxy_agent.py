from autogen.agentchat.user_proxy_agent import UserProxyAgent

def test_user_proxy_agent_init():
    agent = UserProxyAgent(name="user")
    assert agent.name == "user"
    assert agent.human_input_mode == "ALWAYS"
    assert agent.llm_config is False
