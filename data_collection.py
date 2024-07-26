from sec_edgar_downloader import Downloader

# Initialize the downloader
dl = Downloader("sec_filings",email_address="naveensakthivel3251@gmail.com")

# List of companies and their ticker symbols
companies = {
    "Coinbase Global, Inc.": "COIN",
    "Marathon Digital Holdings, Inc.": "MARA",
    "Riot Platforms, Inc.": "RIOT"
}

# List of filing types to download
filing_types = ["10-K", "10-Q", "8-K"]

# Download the filings for each company
for company_name, ticker in companies.items():
    for filing_type in filing_types:
        print(f"Downloading {filing_type} filings for {company_name} ({ticker})")
        dl.get(filing_type, ticker)

print("Downloads completed.")
