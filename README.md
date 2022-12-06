# Meal_List_Bot
  This is a bot that sends the day's meal list in student cafeteria of Hacettepe University to the wanted Whatsapp group to inform students.
It scrapes and processes data from the web, then sends it to a Whatsapp group.
  It can be easily modified to send any data to any Whatsapp group by changing some variable names and Xpath values. I have explained how to do that later on this readme.

**Bot does three main things respectively:**
1. Scraping today's date
2. Scraping today's meal with the help of previous data
3. Sending today's meal to the selected Whatsapp group

## Built With
I used Python with Visual Studio as an IDE and I analyzed HTML content using developer tools in Chrome.
These are the libraries I used the most:
* BeautifulSoup
* Requests
* Selenium

## How To Install And Modify 

### 1. Install the needed packages
Check the required packages with **pipreqs** and use **pip** to install them.

### 2. Change the **contact** variable with your wanted group's name
```
contact = "food bot test group"
```
### 3. Change the **selected_contact** variable with your wanted group's Xpath
* First open Whatsapp Web and your browser's developer tools (Chrome is adviced).
* Search the group's name on the search bar. (This is important as the Xpath might change before and after searching the name)
* Right click on the group and click inspect. You can also manually go through the html. Find the parent division that includes all the elements of that group.
* Right click on that divison and copy **Xpath**. (You can copy **full Xpath** if the program couldn't find the group.)
* Replace the **selected_contact** variable's string with the copied Xpath.
```
selected_contact = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]')
```
### 4. Change the keywords.
Bot will send a message only when it detects these words. You can replace the existing words in the **keywords** variable.
```
keywords = ["keyword1", "keyword2"]
```
### 5. Change the message to send.
You can do these by changing the food_today variable. You can do this in two ways:
* Replacing the scraped meal list with any string.
```
food_today = "The string you want the bot to send"
```
* Replacing the scraped meal list with another scraped string
```
food_today = new_scraped_string.text.strip()
```
You can also disable the default scraping part of the code if you wish to send another scraped string.

### 6. Rewrite the Chrome path of **options** and **driver** variables with wherever your chrome.exe and chrome user data is located.
```
options.add_argument("user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\whatsappbot")
driver = webdriver.Chrome("executable_path=C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", options=options)
```
### 7. Launch the program
Note that you will need to scan a qr code in the first time you launch it.

### Other things to note
The site where the date is scraped and the days of the week are named Turkish because I designed this bot to work compatible with the Uni's website which uses Turkish.
However, you can replace all of these data with your desired ones and check the date of any time zone. 

## How Does It Work?
Here, I will explain how each piece of code works and what do they do.

### Scraping the date
First, I parsed the content of a site which shares the date(Turkish time zone) momentarily.
```
calender_page = requests.get("https://www.turktakvim.com")
calender_soup = BeautifulSoup(calender_page.content, "html.parser")
```

Then I parsed the divison which has the data about the day and I decomposed some unwanted divisons to make storing the data easier.
```
date_division = calender_soup.find(class_ = "tarihay")
date_division.find("br").decompose()
date_division.find("br").decompose()
```

Finally, I matched the data with the strings of the days and stored it inside the variable *today*.
```
days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cuma", "Cumartesi", "Pazar"]
today = ""
for date_element in date_division:
    for day in days:
        if date_element.text.strip() == day:
            today = day

```
Like I previously mentioned, the date site and the day names can be changed to store any time zone's day.

### Scraping the meal list
First, I scraped the content of Hacettepe University Cafeteria's site and parsed the divisions which has the value to each day's meal list.
```
food_today = ""
food_page = requests.get("http://www.sksdb.hacettepe.edu.tr/bidbnew/grid.php?parameters=qbapuL6kmaScnHaup8DEm1B8maqturW8haidnI%2Bsq8F%2FgY1fiZWdnKShq8bTlaOZXq%2BmwWjLzJyPlpmcpbm1kNORopmYXI22tLzHXKmVnZykwafFhImVnZWipbq0f8qRnJ%2BioF6go7%2FOoplWqKSltLa805yVj5agnsGmkNORopmYXam2qbi%2Bo5mqlXRrinJdf1BQUFBXWXVMc39QUA%3D%3D")
food_soup = BeautifulSoup(food_page.content, "html.parser")
food_divisions = food_soup.find_all(class_ = "panel-grid-cell col-md-6")
```

Then I found the division which has the matching date with the previously stored **today** variable.
```
for food_division in food_divisions:
    food_date_division = food_division.find(class_ = "popular")
    food_date = food_date_division.find(text = True, recursive = False)
    if today in food_date.text.strip():
        food_today = food_division
        break
food_today = food_today.text.strip()
```
Each division looks like this so it has the date info on it.

![meal list division](https://user-images.githubusercontent.com/118556737/205858108-d3b610de-5ccd-4cfe-8b0d-1642056acbb9.png)


### Automating Whatsapp Web
Here I modified the options of Chrome driver to not launch from a new default directory each time. This way I didn't have to scan the qr code each time I launched the bot.
```
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\whatsappbot")
driver = webdriver.Chrome("executable_path=C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", options=options)
```

This piece of code opens Whatsapp Web, waits until its loaded then clicks on the searchbox.
You can change the amount of the time it sleeps if your driver is slower and it gives error about not being able to locate the **inp_xpath_search** element.  
```
contact = "food bot test group"
driver.get("https://web.whatsapp.com")
time.sleep(20)
inp_xpath_search = '//*[@id="side"]//div[1]//div//div//div[2]//div//div[2]'
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.XPATH, inp_xpath_search))
input_box_search.click()
```

After clicking the search bar, bot types down the string stored inside the **contact** variable. Then it clicks on the contact.
```
time.sleep(1)
input_box_search.send_keys(contact)
time.sleep(1)    
selected_contact = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]')
selected_contact.click()
time.sleep(1)
```

Using **while** method, program checks for the keywords in the last sent message repeatedly. If one or both of the keywords are included,
meal list stored inside the **food_today** variable is sent to the chat.
```
keywords = ["yemekhane", "yemek"]
while True:
    last_message = driver.find_element(By.CLASS_NAME, '_1qB8f')
    for keyword in keywords:
        if keyword in last_message.text.strip().lower():
            inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = driver.find_element(By.XPATH, inp_xpath)
            time.sleep(1)
            input_box.send_keys(food_today + Keys.ENTER)
            print("List has been sent.")
            time.sleep(3)
            break
        else:
            print(f"Keyword {keyword} is not included in the last message")
            time.sleep(1)
```

## Communication
* ardanimoxd@gmail.com

## Legal
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk.
