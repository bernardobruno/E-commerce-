# E-commerce

Test file for GitHub clone (README. Visual Studio Code) and Webscraping.

## Code for Data Cleaning (Attached).

## Scraping Smartphones

1-) create search_urls.txt which will contain all the product pages. You can use a for loop to change the page number.

2-) Create search.yml which contains all the element paths from where the informations would be extracted.

3-) Run search.py which takes search_urls.txt and search.yml as inputs and write the basic product details to search_output.jsonl. 

4-)Also it should write the urls of the products in product_urls.txt.

5-) Create the products.yml to select particular informations from product pages.

6-) Remember that, 'products.yml' would change based on the type of products you are scraping as the css elements of one product type generally do not match with the other product type. 

7-) Sometimes this can be real tricky to know the elemenets.

To create / modify this yaml file you can use selector gadget. 

There is a chrome extension which you have to install and use for the same.

8-) Run the product.py takes product_urls.txt and products.yml as inputs and output the product_output.jsonl

9-) The same thing you have to repeat for all of the product types that you want to scrap. 

10-) Once you have obtained the json file containing the product informations, you have to create a dataframe for each of these product types, i.e., one for Processors, one for laptops etc. As this is a nested json file, it is always a challenge to create a simple dataframe out of it.
