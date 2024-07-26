import os
import re
import json
from bs4 import BeautifulSoup

class SECFilingsProcessor:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.companies = {
            "Coinbase Global, Inc.": "COIN",
            "Marathon Digital Holdings, Inc.": "MARA",
            "Riot Platforms, Inc.": "RIOT"
        }


    def read_text_from_txt(self, file_path):
        print("reading")
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    def read_texts_from_directory(self, directory, company_name):
        all_texts = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    text = self.read_text_from_txt(file_path)
                    all_texts.append({'company': company_name, 'text': text})
        return all_texts

    def clean_text(self, text):
        print("cleaning the text")
        text = text.replace('unknown status keyword', '')
        soup = BeautifulSoup(text, 'lxml')
        cleaned_text = soup.get_text(separator=' ', strip=True)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]+', ' ', cleaned_text)
       
        return cleaned_text

    def process_filings(self):
        print("process fillings")
        all_company_texts = []
        for company_name, ticker in self.companies.items():
            company_directory = os.path.join(self.base_dir, ticker)
            company_texts = self.read_texts_from_directory(company_directory, company_name)
            all_company_texts.extend(company_texts)

        # Modify this part to create instruction, input, and output fields
        cleaned_texts = []
        for item in all_company_texts:
            cleaned_text = self.clean_text(item['text'])
            cleaned_texts.append({
                'instruction': 'Clean and process SEC filing text',
                'input': f"Company: {item['company']}, Text: {item['text'][:100]}...",  # truncated input text
                'output': cleaned_text
            })

        return cleaned_texts

    def save_to_jsonl(self, data, output_file):
        print("saving")
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for entry in data:
                json.dump(entry, outfile)
                outfile.write('\n')













'''import os
import re
import json
from bs4 import BeautifulSoup

class SECFilingsProcessor:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.companies = {
            "Coinbase Global, Inc.": "COIN",
            "Marathon Digital Holdings, Inc.": "MARA",
            "Riot Platforms, Inc.": "RIOT"
        }

    def read_text_from_txt(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    def read_texts_from_directory(self, directory, company_name):
        print("read text from directory")
        all_texts = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    text = self.read_text_from_txt(file_path)
                    all_texts.append({'company': company_name, 'text': text})
        return all_texts

    def clean_text(self, text):
        print("Cleaning the text")
        # Preprocess the text to replace problematic markup
        text = text.replace('unknown status keyword', '')
        
        # Use BeautifulSoup with 'lxml' parser for more robust parsing
        soup = BeautifulSoup(text, 'lxml')
        cleaned_text = soup.get_text(separator=' ', strip=True)
        
        # Further clean the text by removing extra whitespace and non-ASCII characters
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)

        # Remove sequences of non-alphanumeric characters
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]+', ' ', cleaned_text)
        
        # Further filter out any remaining unwanted text
        cleaned_text = re.sub(r'\b[A-Z0-9]{2,}\b', ' ', cleaned_text)
        
        return cleaned_text

    def process_filings(self):
        print("process_fillings")
        all_company_texts = []
        for company_name, ticker in self.companies.items():
            company_directory = os.path.join(self.base_dir, ticker)
            company_texts = self.read_texts_from_directory(company_directory, company_name)
            all_company_texts.extend(company_texts)

        cleaned_texts = [{'company': item['company'], 'text': self.clean_text(item['text'])} for item in all_company_texts]

        return cleaned_texts

    def save_to_jsonl(self, data, output_file):
        print("save to jsonl")
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for entry in data:
                json.dump(entry, outfile)
                outfile.write('\n')'''



