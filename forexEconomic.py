import cloudscraper
from bs4 import BeautifulSoup

def fetch_event_details(detail_url):
    scraper = cloudscraper.create_scraper()
    response = scraper.get(detail_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print raw HTML content for inspection
    print("Raw HTML content:")
    print(soup.prettify())

    # Find and print intermediate elements
    title_element = soup.find('span', class_="calendar__event-title")
    description_element = soup.find('td', class_="calendarspecs__specdescription")
    speaker_element = soup.find('td', class_="calendarspecs__spec")
    expected_outcome_element = soup.find('td', class_="calendarspecs__specdescription")

    print("\nIntermediate Elements:")
    print("Title Element:", title_element)
    print("Description Element:", description_element)
    print("Speaker Element:", speaker_element)
    print("Expected Outcome Element:", expected_outcome_element)

    title = title_element.text.strip() if title_element else 'N/A'
    description = description_element.text.strip() if description_element else 'N/A'
    speaker = speaker_element.text.strip() if speaker_element else 'N/A'
    expected_outcome = expected_outcome_element.text.strip() if expected_outcome_element else 'N/A'

    return {
        "Title": title,
        "Speaker": speaker,
        "Description": description,
        "Expected": expected_outcome,
    }

# Example detail URL (adjust as needed)
detail_url = 'https://www.forexfactory.com/calendar?day=jul9.2024#detail=140389'
details = fetch_event_details(detail_url)
print("\nExtracted Details:")
print(details)

# Print the URL for troubleshooting
print(f"Scraped URL: {detail_url}")
