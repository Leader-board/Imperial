import time
import sys
import os
from typing import (Dict, List)

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
# https://stackoverflow.com/questions/34338897/python-selenium-find-out-when-a-download-has-completed
def download_wait(directory, timeout, nfiles=None):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds
# lister should be the list of playlists (i.e, lecture modules) that you want to download
lister = ["https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22c1d70666-3291-467d-b576-adb10091a212%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22e27a1ea7-c1d0-4ae4-88fd-adb10089d9fd%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22f8f4277a-92fb-4e56-9c21-adb1010617e9%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%228fdcc9ad-abd7-4daa-9aef-adbf00c6255e%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22acf12982-db3f-42eb-aae5-adb400e59e51%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%226cb20ec7-c4fa-4bf1-9387-adbf00c626f5%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22956dad10-6088-4f9e-984f-adf701081953%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22fece60e0-3c4f-4932-a87c-adb400e5a88e%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%2246529515-5d18-4315-b2cc-adbe009d1e98%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%226c38e106-1533-43e0-9e03-adb400e5aa80%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%2232803767-bdc5-4fcb-bfea-adb400e5ac7f%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22b21eed55-89fa-47ba-b9fc-ae0400b5a30f%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%228a2d59ee-5d93-4623-a07c-adb400e5b083%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22545f344e-14e7-4a5f-82a6-aeb400c8f219%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%2248b782a7-282b-47da-a94f-aa860092f8be%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%2203118bcf-20c6-4f06-a0d3-aa86009301eb%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%227a0d7433-a194-4814-a33f-aa860092fd5f%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%2214dd2578-9cf0-41fd-b902-aa860093040b%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%2267d2b2bb-219a-4fb0-9170-aa860092f9e3%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%2283e83baa-0115-48e7-895a-aa8600930e90%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22d08661de-47c7-4157-b01a-aa86009310c4%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%223bca740a-0935-4a5c-827c-aa8600931306%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%229ca54311-7e75-4717-8968-aa8600931553%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%222e344420-1cc2-45f8-8839-aa8600931776%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22e8f5f57a-de28-4820-9bc8-aa8600931ba1%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%226f8217d0-bb6f-4232-a46d-aa8600931ee2%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%220e31bc3b-5832-4ca7-9af3-aa86009320f9%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%22804c0749-c09e-4b56-9cba-adb70128c171%22", "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%226042170d-ba6e-4c4f-aa87-adc6009a883c%22"]
for lll in lister:
    options = ChromeOptions()
    # replace with the location of default profile
    options.add_argument("user-data-dir=C:\\Users\\Leaderboard\\AppData\\Local\\Google\\Chrome\\User Data") 
    driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver')
    driver.get(lll)
    time.sleep(7)
    print(driver.title)
    tut_name = str(driver.title)
    elems2 = driver.find_elements(by=By.TAG_NAME, value="a")
    href_links2 = []
    for elem in elems2:
        l = elem.get_attribute("href")
        if (l not in href_links2) & (l is not None):
            href_links2.append(l)
    driver.quit()
    # where should the script download videos to?
    new_download = "Y:\\Lecture recordings\\" + tut_name.replace(":", "-").replace("/","-")
    print(new_download)
    if not os.path.exists(new_download):
        os.makedirs(new_download)
    options = ChromeOptions()
    # replace with the location of default profile
    options.add_argument("user-data-dir=C:\\Users\\Leaderboard\\AppData\\Local\\Google\\Chrome\\User Data") 
    options.add_experimental_option('prefs', {
    "download.default_directory": new_download,
    "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
})
    driver2 = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver')
    ptr = 0
    for link in href_links2:
        print(link)
        if ("Viewer" in link):
            driver2.get(link)
            time.sleep(6)
            try:
                driver2.find_element("id","podcastDownload").click()
                ptr = ptr + 1
            except:
                print("Exception caught - it appears that the option to download the video is not available here.") # in case the "download podcast" option does not exist
    print("Time taken = " + str(download_wait(new_download, 200, ptr)) + " seconds")
    driver2.quit()