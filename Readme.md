# Scraper & Summarizer Tool

This tool scrapes the latest news for a specified company, cleans the data, and extracts key events related to the company.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository or download the source code.

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
  ```
3. Navigate to the source directory:

   ```bash
   cd src
   ```
### Usage
1. Modify the company name in the `main.py` file to specify the target company for news scraping. 
By default, the company is set to Thales.

2. Run the `main.py` file:

   ```bash
   python main.py
   ```
### Output 

-Console Output: Displays a summary of the latest news for the specified company.

-output.txt: Contains all the scraped data after cleaning and processing, including relevant events related to the company.
