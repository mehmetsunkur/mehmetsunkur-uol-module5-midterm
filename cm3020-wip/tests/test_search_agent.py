import pytest

from parta.search_agent import CustomOutputParser, AgentAction, AgentFinish

def test_parse_final_answer():
    parser = CustomOutputParser()
    llm_output = "Some text... Final Answer: This is the final answer."
    result = parser.parse(llm_output)
    assert isinstance(result, AgentFinish)
    assert result.return_values["output"] == "This is the final answer."
    assert result.log == llm_output

def test_parse_action_and_input():
    parser = CustomOutputParser()
    llm_output = "Some text... Action: search\nAction Input: AI game playing motivation\n"
    result = parser.parse(llm_output)
    assert isinstance(result, AgentAction)
    assert result.tool == "search"
    assert result.tool_input == "AI game playing motivation"
    assert result.log == llm_output

def test_parse_action_and_input_1():
    parser = CustomOutputParser()
    llm_output = 'Some text... Action: search\nAction Input: AI game playing motivation'
    result = parser.parse(llm_output)
    assert isinstance(result, AgentAction)
    assert result.tool == "search"
    assert result.tool_input == "AI game playing motivation"
    assert result.log == llm_output

def test_parse_action_and_input_2():
    parser = CustomOutputParser()
    llm_output = 'Thought: I should use Custom Search to find academic sources on AI game playing motivation.\nAction: Custom Search\nAction Input: "AI game playing motivation site:.edu"'

    result = parser.parse(llm_output)
    assert isinstance(result, AgentAction)
    assert result.tool == "Custom Search"
    assert result.tool_input == '"AI game playing motivation site:.edu"'
    assert result.log == llm_output

def test_parse_invalid_output():
    parser = CustomOutputParser()
    llm_output = "Some text without proper format"
    with pytest.raises(ValueError, match="Could not parse LLM output"):
        parser.parse(llm_output)