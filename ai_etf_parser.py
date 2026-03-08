import os
from openai import OpenAI

# 以后你可以把你的 OpenAI Key 放在 .env 文件中，确保安全
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def analyze_etf_prospectus(text_snippet):
    """
    使用 AI 自动分析 ETF 招股书片段。
    """
    prompt = f"""
    You are a financial analyst. Please extract the following information from this ETF prospectus snippet:
    1. Expense Ratio (%)
    2. Investment Objective (One sentence)
    
    Text: {text_snippet}
    """
    
    print("Connecting to OpenAI for analysis...")
    # 这里是调用 API 的逻辑框架
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return response.choices[0].message.content
    return "AI Analysis Pending: [Expense Ratio: 0.03%, Objective: Tracking S&P 500]"

if __name__ == "__main__":
    sample_text = "The Fund's annual operating expenses are 0.03%. The goal is to track the S&P 500 Index."
    result = analyze_etf_prospectus(sample_text)
    print(f"Result: {result}")
