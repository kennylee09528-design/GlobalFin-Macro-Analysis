import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_performance_chart(tickers, years=5):
    """
    模拟并可视化不同 ETF 的历史增长对比。
    """
    print(f"Generating performance comparison for: {tickers}")
    
    # 模拟数据生成
    np.random.seed(42)
    dates = pd.date_range(start='2019-01-01', periods=years*12, freq='M')
    
    # 模拟 VOO (标普500) 和 QQQ (纳斯达克100) 的走势
    voo_growth = np.cumprod(1 + np.random.normal(0.008, 0.04, size=len(dates)))
    qqq_growth = np.cumprod(1 + np.random.normal(0.012, 0.06, size=len(dates)))
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, voo_growth, label='VOO (S&P 500)', color='blue')
    plt.plot(dates, qqq_growth, label='QQQ (Nasdaq 100)', color='green')
    
    plt.title('ETF Performance Comparison (Simulation)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Cumulative Return', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 在开源项目中，我们通常将图表保存为图片供 README 调用
    plt.savefig('etf_performance_sample.png')
    print("Chart saved as 'etf_performance_sample.png'")

if __name__ == "__main__":
    generate_performance_chart(['VOO', 'QQQ'])
