import requests
from bs4 import BeautifulSoup
import time
import notify2
import re


def get_minecraft_pe_price(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        price_element = soup.find("span", class_='VfPpkd-vQzf8d')

        if price_element:
            price_string = price_element.text.strip()
            price_match = re.search(r'\d+\,\d+', price_string)

            if price_match:
                price_str = price_match.group()
                price_float = float(price_str.replace(",", ".")) 
                return price_float
            else:
                print("Price could not be extracted using the provided regex pattern.")
        else:
            print("Price element with the specified class not found on the page.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred fetching the price: {e}")

    return None


if __name__ == "__main__":
    url_minecraft_pe = "https://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=pt_BR"
    price = get_minecraft_pe_price(url_minecraft_pe)

    if price:
        print(f"The current price of Minecraft PE is: R$ {price:.2f}")
    elif price == 'Instalar' or price == 'Download' or price == 'Adquirir' or price == 0.00:
        prit(f'Minecraft is free now in Playstore, install now!')
    else:
        print("Price could not be determined.")

    time.sleep(3600)