# this file has the questions and my solution to the unit 2 quiz on hugging face's agents course.


### Question 1: Create a Basic Code Agent with Web Search Capability

# my solution
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

search_tool = DuckDuckGoSearchTool()
model2 = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

agent = CodeAgent(
    tools=[search_tool], model=model2  # Add search tool here  # Add model here
)

# hf solution
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
)

### Score: 10/50
#####################################################################


### Question 2: Set Up a Multi-Agent System with Manager and Web Search Agents

# my solution
# Create web agent and manager agent structure
from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    VisitWebpageTool,
    InferenceClientModel,
)


model = InferenceClientModel(
    "Qwen/Qwen2.5-Coder-32B-Instruct", provider="together", max_tokens=2048
)


web_agent = ToolCallingAgent(
    tools=[
        DuckDuckGoSearchTool(),
        VisitWebpageTool(),
        InferenceClientModel(),
    ],  # Add required tools
    model=model,  # Add model
    max_steps=5,  # Adjust steps
    name="web_agent",  # Add name
    description="find information from the internet",  # Add description
)

manager_agent = CodeAgent(
    model=InferenceClientModel(
        "deepseek-ai/DeepSeek-R1", provider="together", max_tokens=8096
    ),
    tools=[calculate_cargo_travel_time],
    managed_agents=[web_agent],
    additional_authorized_imports=[
        "geopandas",
        "plotly",
        "shapely",
        "json",
        "pandas",
        "numpy",
    ],
    planning_interval=5,
    verbosity_level=2,
    final_answer_checks=[check_reasoning_and_plot],
    max_steps=15,
)

# hf solution
web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],
    model=model,
    max_steps=10,
    name="search",
    description="Runs web searches for you."
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[web_agent],
    additional_authorized_imports=["time", "numpy", "pandas"]
)

### Score: 20/50
#####################################################################


# Question 3: Configure Agent Security Settings

# my solution
from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel(
    "Qwen/Qwen2.5-Coder-32B-Instruct", provider="together", max_tokens=2048
)

agent = CodeAgent(
    tools=[],
    model=model,
    executor_type="e2b",  # run generated code in an E2B sandbox (remote, isolated)
    additional_authorized_imports=[],  # DO NOT widen the import allowlist (stay minimal/locked down)
)


# hf solution
from smolagents import CodeAgent, E2BSandbox

agent = CodeAgent(
    tools=[],
    model=model,
    sandbox=E2BSandbox(),
    additional_authorized_imports=["numpy"]
)

### Score: 20/50
#####################################################################

# Question 4: Implement a Tool-Calling Agent

# my solution
from smolagents import ToolCallingAgent, DuckDuckGoSearchTool, InferenceClientModel


search_tool = DuckDuckGoSearchTool()


model = InferenceClientModel(
    "Qwen/Qwen2.5-Coder-32B-Instruct", provider="together", max_tokens=2048
)

agent = ToolCallingAgent(
    model=model,
    tools=[search_tool],
    name="WebSearchAgent",
    description="An agent that uses web search to retrieve and summarize information.",
    step_limit=5,  # reasonable step limit for basic tasks
)


# hf solution
from smolagents import ToolCallingAgent

agent = ToolCallingAgent(
    tools=[custom_tool],
    model=model,
    max_steps=5,
    name="tool_agent",
    description="Executes specific tools based on input"
)

### Score: 30/50
#####################################################################


# Question 5: Set Up Model Integration

# my solution
# Configure model integration
from smolagents import HfApiModel

model = HfApiModel(model_id="meta-llama/Meta-Llama-3-8B-Instruct")


# hf solution
from smolagents import HfApiModel, LiteLLMModel

# Hugging Face model
hf_model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

# Alternative model via LiteLLM
other_model = LiteLLMModel("anthropic/claude-3-sonnet")

### Score: 35/50
#####################################################################