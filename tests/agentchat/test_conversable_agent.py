import pytest
from autogen.agentchat.conversable_agent import ConversableAgent
from autogen.agentchat.agent import Agent

class TestConversableAgent:
    def test_init(self):
        agent = ConversableAgent(name="test_agent")
        assert agent.name == "test_agent"
        assert agent.system_message == "You are a helpful AI Assistant."

    def test_send_receive(self):
        sender = ConversableAgent(name="sender", llm_config=False, code_execution_config=False)
        receiver = ConversableAgent(name="receiver", llm_config=False, code_execution_config=False)
        
        # sender sends message to receiver
        sender.send("Hello", receiver, request_reply=False)
        
        # receiver should have received the message
        assert len(receiver._oai_messages[sender]) == 1
        assert receiver._oai_messages[sender][0]["content"] == "Hello"
        # The role depends on who sent it. If sender sends to receiver, 
        # receiver sees it as coming from "user" (or the sender's role relative to receiver)
        # Usually ConversableAgent treats incoming messages as 'user' role in the context of LLM generation
        # unless specified otherwise.
        
    @pytest.mark.asyncio
    async def test_a_send_receive(self):
        sender = ConversableAgent(name="sender", llm_config=False, code_execution_config=False)
        receiver = ConversableAgent(name="receiver", llm_config=False, code_execution_config=False)
        
        await sender.a_send("Hello Async", receiver, request_reply=False)
        
        assert len(receiver._oai_messages[sender]) == 1
        assert receiver._oai_messages[sender][0]["content"] == "Hello Async"

    def test_generate_reply_with_mock(self, mock_openai_chatcompletion):
        # We need to provide a valid config list even if mocked, 
        # because some validation might happen before calling create
        llm_config = {
            "config_list": [{"model": "gpt-3.5-turbo", "api_key": "sk-fake-key"}],
        }
        agent = ConversableAgent(name="ai_agent", llm_config=llm_config)
        
        # Manually inject a message to reply to
        messages = [{"role": "user", "content": "Hello"}]
        
        # We can use generate_reply directly
        # Note: generate_reply might trigger other reply functions.
        # By default ConversableAgent has:
        # 1. generate_code_execution_reply
        # 2. generate_function_call_reply
        # 3. generate_oai_reply
        
        # Since code_execution_config is default (None/True?), it might try to execute code if found.
        # "Hello" has no code.
        
        reply = agent.generate_reply(messages=messages, sender=ConversableAgent("user", llm_config=False, code_execution_config=False))
        
        assert reply == "Mocked response"
        mock_openai_chatcompletion[0].assert_called()

    @pytest.mark.asyncio
    async def test_a_generate_reply_with_mock(self, mock_openai_chatcompletion):
        llm_config = {
            "config_list": [{"model": "gpt-3.5-turbo", "api_key": "sk-fake-key"}],
        }
        agent = ConversableAgent(name="ai_agent", llm_config=llm_config)
        
        reply = await agent.a_generate_reply(messages=[{"role": "user", "content": "Hello"}], sender=ConversableAgent("user", llm_config=False, code_execution_config=False))
        
        assert reply == "Mocked response"
        mock_openai_chatcompletion[1].assert_called()
