import requests
import pandas as pd

def fetch_13f_filings(cik):
    """
    通过 CIK 编号获取机构最新的 13F 申报信息列表。
    例如：巴菲特的伯克希尔哈撒韦 CIK 是 0001067983
    """
    url = f"https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json"
    headers = {
        'User-Agent': 'GlobalFinanceProject/1.0 (contact: your-email@example.com)'
    }
    
    print(f"Fetching filings for CIK: {cik}...")
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # 提取申报记录
        filings = data['filings']['recent']
        df = pd.DataFrame(filings)
        
        # 筛选出 13F-HR 报告
        f13_reports = df[df['form'] == '13F-HR'][['accessionNumber', 'filingDate', 'reportDate']]
        return f13_reports.head(5)
    except Exception as e:
        return f"Error fetching data: {e}"

if __name__ == "__main__":
    # 以伯克希尔哈撒韦为例
    berkshire_cik = "1067983"
    reports = fetch_13f_filings(berkshire_cik)
    print("Latest 13F-HR Filings:")
    print(reports)
