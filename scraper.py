import requests
from bs4 import BeautifulSoup
import time
import re
import csv

def persian_to_english_nums(text):
    """Converts Persian numbers to English numbers for math operations."""
    if not text: return ""
    persian_nums = '۰۱۲۳۴۵۶۷۸۹'
    english_nums = '0123456789'
    translation_table = str.maketrans(persian_nums, english_nums)
    return text.translate(translation_table)

def extract_value_by_label(soup, label_text):
    """Finds a label like 'رنگ بدنه' and extracts the value under it."""
    label = soup.find(lambda tag: tag.name == "span" and label_text in tag.text)
    if label:
        parent_div = label.find_parent('div')
        if parent_div:
            spans = parent_div.find_all('span')
            if len(spans) >= 2:
                return spans[-1].text.strip()
    return "N/A"

def scrape_bama_samand(target_count=50, min_year=1385):
    base_url = "https://bama.ir"
    list_url = f"{base_url}/car/samand"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    collected_cars = []
    page = 1

    print(f"Starting scraper. Looking for {target_count} Samand cars manufactured after {min_year}...")

    while len(collected_cars) < target_count:
        print(f"\n[Scanning List Page {page}...]")
        response = requests.get(f"{list_url}?page={page}", headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}.")
            break

        list_soup = BeautifulSoup(response.text, 'html.parser')
        
        ad_links = list_soup.find_all('a', href=re.compile(r'/car/detail-'))
        
        if not ad_links:
            print("No more cars found. The site might be blocking us or we hit the end of the list.")
            break

        unique_links = list(set([a['href'] for a in ad_links]))

        for link in unique_links:
            if len(collected_cars) >= target_count:
                break
            
            full_link = link if link.startswith('http') else base_url + link
            
            time.sleep(1.5) # Sleep to avoid getting IP blocked
            
            try:
                detail_response = requests.get(full_link, headers=headers)
                detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
                
                year_mileage_tag = detail_soup.find(string=re.compile(r'کارکرد'))
                year, mileage = 0, "N/A"
                
                if year_mileage_tag:
                    clean_text = persian_to_english_nums(year_mileage_tag)
                    year_match = re.search(r'\b(13\d{2}|14\d{2})\b', clean_text)
                    if year_match:
                        year = int(year_match.group(1))
                    
                    mileage_match = re.search(r'کارکرد\s*([\d,]+)', clean_text)
                    if mileage_match:
                        mileage = mileage_match.group(1)

                if year > min_year:
                    price_label = detail_soup.find(string=re.compile(r'تومان'))
                    price = "N/A"
                    if price_label:
                        price_parent = price_label.find_parent('p') or price_label.find_parent('div')
                        if price_parent:
                            price_text = persian_to_english_nums(price_parent.text)
                            price = re.sub(r'[^\d,]', '', price_text)

                    desc_label = detail_soup.find(string=re.compile(r'توضیحات'))
                    description = "N/A"
                    if desc_label:
                        desc_parent = desc_label.find_parent('div').find_next_sibling('div')
                        if desc_parent:
                            description = desc_parent.text.strip()

                    car_data = {
                        'Production_Year': year,
                        'Price_Toman': price,
                        'Mileage_KM': mileage,
                        'Color': extract_value_by_label(detail_soup, 'رنگ بدنه'),
                        'Transmission': extract_value_by_label(detail_soup, 'گیربکس'),
                        'Description': description,
                        'URL': full_link
                    }
                    
                    collected_cars.append(car_data)
                    
                    # --- THIS IS THE NEW PRINT BLOCK ---
                    print(f"\n--- [ {len(collected_cars)} / {target_count} ] New Match Found ---")
                    print(f"Year:         {car_data['Production_Year']}")
                    print(f"Price:        {car_data['Price_Toman']} Toman")
                    print(f"Mileage:      {car_data['Mileage_KM']} KM")
                    print(f"Color:        {car_data['Color']}")
                    print(f"Transmission: {car_data['Transmission']}")
                    print(f"Description:  {car_data['Description']}")
                    print(f"URL:          {car_data['URL']}")
                    print("-" * 45)

            except Exception as e:
                print(f"Error parsing ad {full_link}: {e}")
                continue

        page += 1

    return collected_cars

if __name__ == "__main__":
    data = scrape_bama_samand(target_count=50, min_year=1385)
    
    print("\n--- Scraping Complete ---")
    
    if data:
        print(f"Successfully extracted data for {len(data)} vehicles.")
        
        # Save to CSV
        filename = 'bama_samand_data.csv'
        keys = data[0].keys()
        
        with open(filename, 'w', newline='', encoding='utf-8-sig') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
            
        print(f"\n Data successfully saved to {filename}")
        
    else:
         print("No data was extracted to save.")