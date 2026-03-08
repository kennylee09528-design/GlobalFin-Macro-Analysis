import pandas as pd

def compare_etf_fees(etf_list):
    """
    Simple tool to compare expense ratios of different ETFs.
    """
    # Placeholder data for demonstration
    data = {
        'Ticker': ['VOO', 'IVV', 'SPY'],
        'Expense_Ratio': [0.03, 0.03, 0.09]
    }
    df = pd.DataFrame(data)
    print("Analyzing ETF Expense Ratios...")
    return df.sort_values(by='Expense_Ratio')

if __name__ == "__main__":
    print(compare_etf_fees(['VOO', 'IVV', 'SPY']))
