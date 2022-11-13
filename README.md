# download-google-slides-as-PNG-images

## Motivation
This code is intended to facilitate the process of downloading Google Slides as PNG images. Since users can modify the pixels for a Google slide, it's possible to capture high-resolution images in various formats. In addition, downloading multiple slides can be a tedious process and this code can automate the task. Since the program connects to an existing Chrome browser, users can use the Google Slides account saved on their machine.

## Build Status
At the moment this code runs without any bugs as long as the proper setting are enabled on Google Chrome **(Auto-download should be enabled on Chrome and Google Slides needs to have permission to download multiple files. This can be set in the settings or when the dialog box appears when running the code)**

## Tech/Framework used
Python 3.10.6 

## Features
The code is able to connect to an existing Chrome browser and download Google Slides as PNG images from the link provided. 

## How to Use?
1. Install Python 3
2. Install pip
3. If you're on Windows, add Google Chrome to your path
4. Download a Chrome Driver that has the same version as your exisiting Chrome Browser. You can check your current Chrome Browser version by doing the following: **Open Chrome -> Settings -> 'About Chrome'.** Chrome Drivers are currently available here: **https://chromedriver.chromium.org/downloads** 
5. Note that most Chrome Browsers are updated automatically so it may be necessary to download a new Chrome Driver if you're planning to use the code over time.  
6. Clone the repository
7. Download Selenium and dotenv using pip
8. Replace **CHROME_DRIVER_PATH** in the code with the path where you've installed your Chrome Driver
9. **Close all Chrome Browser windows that are open**
10. Copy the path for the 'User Data' folder on you machine. For Windows users, it'll be something like the following (Make sure to change PLACE_HOLDER with the username on you machine): **C:\Users\<PLACE_HOLDER>\AppData\Local\Google\Chrome\User Data** For Mac users it will be soemthing like the following (Make sure to change PLACE_HOLDER with the username on you machine): **Users/<PLACE_HOLDER>/Library/Application Support/Google/Chrome/Default**
11. Go to the command line and write the follwing (After replaceing PLACE_HOLDER with the 'User Data' folder path inside of double quotes): **chrome.exe --remote-debugging-port=9250 --user-data-dir=PLACE_HOLDER** For Windows users, it's necessary to add Chrome to the path for this command to work.
12. **Make sure auto-download is enabled**
13. **Make sure Google Slides has permission to download multiple files. It's possible to enable this from the settings or by clicking yes to the dialog box that appears when running the code**
14. Run the code by writing **python file.py** in the command line (in the path where the code is located)

## Code Style
Standard

## Code Examples
**python file.py** or **python3 file.py**

## Contribute
You may add more features to the program. For example, the code can be modified to account for different image formats or image quality. 

## API reference
NA

## Tests
NA

## License
MIT