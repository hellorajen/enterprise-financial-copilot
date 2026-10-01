# app/agent.py
from google.adk.agents import Agent
from google.adk.apps import App
from app.tools import get_portfolio_stock_data

root_agent = Agent(
    name="financial_copilot_agent",
    model="gemini-3.8-flash",
    instruction=(
        "You are an Enterprise Financial Copilot designed for executive portfolio reporting. "
        "When responding to queries about portfolio holdings, stock performance, or monthly charts:\n"
        "1. ALWAYS call the `get_portfolio_stock_data` tool to fetch ground-truth metrics.\n"
        "2. Present financial numbers cleanly using Markdown tables or concise bullet points.\n"
        "3. Include the link to the monthly stock chart as an embedded Markdown image: "
        "![Monthly Chart](URL).\n"
        "4. Keep executive takeaways concise, professional, and grounded solely in tool outputs."
    ),
    tools=[get_portfolio_stock_data],
)

app = App(
    name="financial-copilot",
    root_agent=root_agent,
)