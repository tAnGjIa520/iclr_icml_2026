#!/usr/bin/env python3
"""
Convert ICML 2026 Official Database CSV to ICLR-like format
"""
import csv
import json
import sys

def parse_icml_row(row):
    """Parse a row from ICML CSV and extract structured data"""
    try:
        # The 'results' column contains JSON string
        results_str = row['results']
        data = eval(results_str)  # Using eval since it's Python dict format

        # Extract fields matching ICLR format
        paper_id = data.get('uid', '')
        title = data.get('name', '')

        # Extract authors
        authors_list = data.get('authors', [])
        authors = ', '.join([a.get('fullname', '') for a in authors_list])
        author_ids = ', '.join([str(a.get('id', '')) for a in authors_list])

        # Venue/Status
        decision = data.get('decision', '')
        venue = f"ICML 2026 {decision}"

        # Primary area (ICML doesn't have this, use topic or empty)
        primary_area = data.get('topic', '') or ''

        # TL;DR (not in ICML data)
        tldr = ''

        # Keywords
        keywords_list = data.get('keywords', [])
        keywords = ', '.join(keywords_list) if keywords_list else ''

        # Abstract
        abstract = data.get('abstract', '')

        # Code URL (not in ICML data)
        code_url = 'No Code Provided'

        # PDF and Forum URLs
        pdf_url = data.get('paper_pdf_url', '') or ''
        forum_url = data.get('paper_url', '')

        # Submit date (not in ICML data)
        submit_date = ''

        return {
            'Paper ID': paper_id,
            'Title': title,
            'Authors': authors,
            'Author IDs': author_ids,
            'Venue (Status)': venue,
            'Primary Area': primary_area,
            'TL;DR': tldr,
            'Keywords': keywords,
            'Abstract': abstract,
            'Code URL': code_url,
            'PDF Link': pdf_url,
            'Forum URL': forum_url,
            'Submit Date': submit_date
        }
    except Exception as e:
        print(f"Error parsing row: {e}", file=sys.stderr)
        return None

def main():
    input_file = '/mnt/shared-storage-user/tangjia/book/ICLR_ICML_2026/ICML_2026_Official_Database.csv'
    output_file = '/mnt/shared-storage-user/tangjia/book/ICLR_ICML_2026/ICML_2026_All_Data_Extracted.csv'

    # Read input CSV
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Read {len(rows)} rows from input file")

    # Process each row
    processed_data = []
    for i, row in enumerate(rows, 1):
        parsed = parse_icml_row(row)
        if parsed:
            processed_data.append(parsed)
        if i % 100 == 0:
            print(f"Processed {i}/{len(rows)} rows...")

    print(f"Successfully processed {len(processed_data)} papers")

    # Write output CSV
    if processed_data:
        fieldnames = [
            'Paper ID', 'Title', 'Authors', 'Author IDs', 'Venue (Status)',
            'Primary Area', 'TL;DR', 'Keywords', 'Abstract', 'Code URL',
            'PDF Link', 'Forum URL', 'Submit Date'
        ]

        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed_data)

        print(f"Output written to {output_file}")
    else:
        print("No data to write!")

if __name__ == '__main__':
    main()
