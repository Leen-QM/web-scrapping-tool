import traceback
from scrapper_v2 import fetch_main_content_advanced, process_bio_page
from finalCrawling import crawl_and_extract_links


# Main script
if __name__ == "__main__":
    website_type = input("Please choose the type of website:\n1. Collection\n2. Encyclopedia\nEnter the number corresponding to your choice: ").strip()

    # Ensure website_type is an integer
    try:
        website_type = int(website_type)
    except ValueError:
        print("Invalid input. Please enter a valid number (1 or 2).")
        exit()

    crawl_first = input("Crawl whole website? T/F: ").strip().upper()
    url = input("Enter the URL: ").strip()

    if crawl_first == 'T':
        url_path = input("Enter specific path: ").strip()
        url_list = crawl_and_extract_links(url, website_type, url_path)
        print(f"Crawling finished. Found {len(url_list)} bio pages.")
    elif crawl_first == 'F':  
        url_list = [url]

    # Assign folder name based on website type
    if website_type == 1:
        folder_name = "QM Collections"
    elif website_type == 2:
        folder_name = "Mathaf Encyclopedia"
    else:
        print("Invalid website type. Exiting.")
        exit()

    # Enter the phrases for scraping content
    start_phrase = input("Enter the starting phrase: ").strip()
    end_phrase = input("Enter the ending phrase: ").strip()

    # Process each bio page
    for url_list in url_list:
        try:
            print(f"\nFetching content for {url_list}...")
            chunks = fetch_main_content_advanced(url_list, start_phrase, end_phrase)
            print("Content fetched successfully!")
            #print(chunks)
            #print("\nExtracting entities...")
            process_bio_page(url_list, chunks, folder_name, website_type)

        except Exception as e:
            print(f"An error occurred while processing {url_list}: {e}")
            traceback.print_exc()
