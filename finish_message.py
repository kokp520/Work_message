#for 每天傳送預約客戶簡訊 with 簡訊王


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#輸入電話
def onOK():
    global a 
    a = (format(entry.get()))
    window.destroy()

   #輸入電話視窗
window = tk.Tk()
window.title("phonenumber")
window.geometry("300x100+250+150")

alabel = tk.Label(window,text = "phone number")
alabel.pack()

entry = tk.Entry(window,
    width = 30)
entry.pack()

button =tk.Button(window,text = 'ok', command= onOK)
button.pack()

window.mainloop()
#webdriver
PATH = "D:/python/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)

#登入
driver.get("https://www.kotsms.com.tw/index.php")
user = driver.find_element_by_id("usernames")
user.send_keys("USERNAME") #enter your username.
user2 = driver.find_element_by_id("passwords")
user2.send_keys("PASSWORD") #enter your password.
user2.send_keys(Keys.RETURN)

prompt = Alert(driver)
prompt.accept()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Image1"))
    )

#choose normal message
sendmessage = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[1]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[7]/td/div/a/img")
sendmessage.click()

#輸入電話

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td/fieldset/table/tbody/tr[3]/td[2]/textarea"))
    )

phoneno = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td/fieldset/table/tbody/tr[3]/td[2]/textarea")
phoneno.send_keys(a)

#加入電話

submit = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td/fieldset/table/tbody/tr[3]/td[3]/input")
submit.click()

#訊息內容
msgbox = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/textarea")
msgbox.send_keys("您的車輛已經完工...")

pas = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[6]/td/input")
pas.click()

prompt.accept()

#傳送

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/fieldset/center/input[1]"))
    )
final = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/fieldset/center/input[1]")
final.click()
prompt.accept()
driver.quit()

