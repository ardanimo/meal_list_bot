# Meal_List_Bot
  This is a bot that sends the day's meal list in student cafeteria of Hacettepe University to the wanted Whatsapp group to inform students.
It scrapes and processes data from the web, then sends it to a Whatsapp group.
  It can be easily modified to send any data to any Whatsapp group by changing some variable names and xpath values. I have explained how to do that later on this readme.

**Bot does three main things respectively:**
1. Scraping today's date
2. Scraping today's meal with the help of previous data
3. Sending today's meal to the selected Whatsapp group

## Built With
I used Visual Studio as an IDE.
These are the libraries I used the most:
* BeautifulSoup
* Requests
* Selenium

## How To Install And Modify 

### 1. Change the group name and xpath info to your desired group's.

#### Replace the **contact** variable with your wanted group's name
```
contact = "food bot test group"
```
#### Replace the **selected_contact** variable with your wanted group's Xpath
* First open *Whatsapp Web and your browser's developer tools (Chrome is adviced).
* Search the group's name on the search bar. (This is important as the xpath might change before and after searching the name)
* Right click on the group and click inspect. You can also manually go through the html. Find the parent division that includes all the elements of that group.
* Right click on the divison and copy **Xpath**. (You can copy **full Xpath** if the program cant find the group.)
* Replace the **selected_contact** variable's string with the copied Xpath.
```
selected_contact = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]')
```
