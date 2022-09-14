import requests
from bs4 import BeautifulSoup


#dictonary
products_to_track = [
    {
        "product_URL": "https://www.amazon.in/BIBA-Cotton-line-DRESSES1172OWHT_Off-White_38/dp/B08M7HBBPW/ref=sr_1_5?crid=13OGR2HNKSXZM&keywords=dress&qid=1663131379&refinements=p_36%3A4595088031&rnid=4595083031&s=apparel&sprefix=dres%2Caps%2C372&sr=1-5&th=1&psc=1",
        "name": "BIBA Women Dress",
        "target_price": 3000
    },
    {
        "product_URL": "https://www.amazon.in/Lymio-Womens-Polyester-D-554-Sky-Blue-L/dp/B0B3T6VF6S/ref=sr_1_32?crid=13OGR2HNKSXZM&keywords=dress&qid=1663077290&sprefix=dres%2Caps%2C372&sr=8-32&th=1&psc=1",
        "name": "Lymio Women's White Color Round Neck Half Sleeve Lycra Dress",
        "target_price": 620  # dictionary
    },
    {
        "product_URL": "https://www.amazon.in/HARPA-Synthetic-a-line-Dress-GR5759_Black_X-Large/dp/B07MMGSR6H/ref=sxin_17_slsr_d_i_fs4star_fa_1_B07MMGSR6H?content-id=amzn1.sym.a33bdcd4-0f7f-48bd-8bc3-6d0db1130d64%3Aamzn1.sym.a33bdcd4-0f7f-48bd-8bc3-6d0db1130d64&crid=13OGR2HNKSXZM&cv_ct_cx=dress&keywords=dress&pd_rd_i=B07MMGSR6H&pd_rd_r=fdabb141-d38a-423b-8928-a58529a9502d&pd_rd_w=ajEoA&pd_rd_wg=Rluvv&pf_rd_p=a33bdcd4-0f7f-48bd-8bc3-6d0db1130d64&pf_rd_r=A28DKQ33ZSEYE5JY9XRF&psc=1&qid=1663128611&sprefix=dres%2Caps%2C372&sr=1-2-41e0d225-3819-4755-898e-7f0f48633b47",
        "name": "Harpa Women Maxi A-Line Dress",
        "target_price": 650
    },
    {
        "product_URL": "https://www.amazon.in/RUDRAPRAYAG-Womens-Georgette-Material-5407_Red_Free/dp/B07H7KVQTB/ref=sr_1_8?crid=13OGR2HNKSXZM&keywords=dress&qid=1663131379&refinements=p_36%3A4595088031&rnid=4595083031&s=apparel&sprefix=dres%2Caps%2C372&sr=1-8",
        "name" : "RUDRAPRAYAG Women's Faux Georgette Semi-Stitched Dress Material",
        "target_price": 1800

    },
    {
        "product_URL" : "https://www.amazon.in/Ethnic-Yard-Georgette-Stitched-SSEY-F1349_Purple_Free/dp/B091FPNDFT/ref=sr_1_25?crid=13OGR2HNKSXZM&keywords=dress&qid=1663131379&refinements=p_36%3A4595088031&rnid=4595083031&s=apparel&sprefix=dres%2Caps%2C372&sr=1-25",
        "name" : "Ethnic Yard Women's Georgette Semi Stitched Anarkali Gown",
        "target_price": 1600
    }

]
#function

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

    }
    page = requests.get(URL, headers=headers)

    broth = BeautifulSoup(page.content, 'html.parser')
    # print(broth.prettify())

    product_price = broth.find("span", class_="a-price-whole").text
    #if (product_price == None):
   # product_price = broth.find("span", class_="a-offscreen").text
    return product_price


    #print(product_price)
#open file
result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_URL"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[0:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' - \t' + 'Available at Target Price' + ' current price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")
#close file
finally:
    result_file.close()





