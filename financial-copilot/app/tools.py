# app/tools.py
import json

def get_portfolio_stock_data(symbol: str) -> str:
    """Fetches real-time portfolio metrics, financial fundamentals, and links 
    to monthly stock technical analysis chart images.

    Args:
        symbol (str): The stock ticker symbol (e.g., 'RELIANCE', 'MSFT', 'AAPL').

    Returns:
        str: JSON string containing stock performance, valuation metrics, 
             and GitHub chart image URLs.
    """
    clean_symbol = symbol.strip().upper()

    # Ground-truth mock database (Simulating SQL/Data Vault query backend)
    portfolio_universe = {
        "RELIANCE": {
            "company_name": "Reliance Industries Ltd.",
            "currency": "INR",
            "current_price": 2980.50,
            "ytd_return_pct": "+14.2%",
            "pe_ratio": 24.8,
            "market_cap": "20.17T INR",
            "latest_monthly_chart_url": "https://raw.githubusercontent.com/your-github-username/enterprise-financial-copilot/main/charts/RELIANCE_monthly_2026.png",
            "key_highlights": "Strong performance in retail and digital services; refining margins showing resilience."
        },
        "MSFT": {
            "company_name": "Microsoft Corporation",
            "currency": "USD",
            "current_price": 448.20,
            "ytd_return_pct": "+18.6%",
            "pe_ratio": 35.2,
            "market_cap": "3.33T USD",
            "latest_monthly_chart_url": "https://raw.githubusercontent.com/your-github-username/enterprise-financial-copilot/main/charts/MSFT_monthly_2026.png",
            "key_highlights": "Cloud revenue acceleration driven by Azure AI and Copilot enterprise seat growth."
        },
        "AAPL": {
            "company_name": "Apple Inc.",
            "currency": "USD",
            "current_price": 224.50,
            "ytd_return_pct": "+11.4%",
            "pe_ratio": 31.0,
            "market_cap": "3.44T USD",
            "latest_monthly_chart_url": "https://raw.githubusercontent.com/your-github-username/enterprise-financial-copilot/main/charts/AAPL_monthly_2026.png",
            "key_highlights": "Services sector expansion hitting record highs with Apple Intelligence rollout."
        }
    }

    if clean_symbol in portfolio_universe:
        return json.dumps(portfolio_universe[clean_symbol])
    
    return json.dumps({
        "error": f"Symbol '{clean_symbol}' not found in portfolio tracking database.",
        "available_symbols": list(portfolio_universe.keys())
    })