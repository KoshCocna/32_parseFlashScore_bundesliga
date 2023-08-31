# parsing the results of bundesliga from flashscore

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

driver = webdriver.Chrome()

driver.get("https://www.flashscore.com.ua/")


#  нажать "Бундеслига" в левом колонке
ligas = driver.find_elements(By.CSS_SELECTOR, '#my-leagues-list .leftMenu__item a')
bundesliga = ligas[1]
bundesliga.click()
sleep(1)

#  в открытом новом окне нажал "таблица"
bundesliga_table = driver.find_element(By.CSS_SELECTOR, ".event__header--noExpand a")
bundesliga_table.click()
sleep(1)

#  перейти в новое открытое окно
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
sleep(1)

#  парсинг результаты
# games = driver.find_elements(By.CLASS_NAME, "tableCellParticipant__name")
games_all_info = driver.find_elements(By.CLASS_NAME, "ui-table__row")

with open("bundesliga.csv", "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Team", "MP", "W", "D", "L", "G", "GD", "PTS"])
    for _ in games_all_info:
        team_name = _.find_element(By.CLASS_NAME, "tableCellParticipant__name").text
        score_info = _.find_elements(By.CLASS_NAME, "table__cell--value")
        MP = score_info[0].text
        W = score_info[1].text
        D = score_info[2].text
        L = score_info[3].text
        G = score_info[4].text
        GD = score_info[5].text
        PTS = score_info[6].text
        writer.writerow([team_name, MP, W, D, L, G, GD, PTS])


sleep(1)
driver.quit()
