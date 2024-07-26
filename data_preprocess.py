from DataProcessing.text_preprocessing import SECFilingsProcessor


base_dir = 'sec-edgar-filings'
processor = SECFilingsProcessor(base_dir)
    
cleaned_texts = processor.process_filings()

# Save to JSONL
output_file_jsonl = 'formatted_sec_filings_with_companies.jsonl'
processor.save_to_jsonl(cleaned_texts, output_file_jsonl)

print("Text extraction and formatting with company names completed.")