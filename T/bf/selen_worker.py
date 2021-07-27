import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
django.setup()
from bf.models import InPlay

class BFSearch():

    def setUp(self):
        #         self.driver = webdriver.Firefox()
        PATH = r'C:\Users\Sales2\Desktop\kurs_every_day\T\chrom_driver\chromedriver.exe'
        # PATH = r'C:\Users\yablu\PycharmProjects\FootballParser\chrom_driver\chromedriver.exe'
        chrome_options = Options ()
        chrome_options.add_argument ("start-maximized")
        self.driver = webdriver.Chrome (PATH, options=chrome_options)
        # self.driver.get('https://www.betfair.com/exchange/plus/inplay/football')
        self.driver.wait = WebDriverWait (self.driver, 7)


    def tearDown(self):
        self.driver.quit ()

    def seven_elem(self, list_):
        """
        return  ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
        """
        try:
            if type (list_) == list:
                dell = list_.pop()[1::]
                dell = self.price_del_coma (dell)
                list_.append (dell)
                if str(list_[:1]) not in ['ПЕР', 'КОНЕЦ']:
                    dell = int (list_.pop (0)[:-1])
                    dell_2 = int (list_.pop (0)[1::])
                    sum_ = dell + dell_2
                    list_.append (sum_)
                else:
                    dell = list_.pop(0)
                    list_.append (dell)

                return list_  # ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
            else:
                print ('seven_list Error type')
        except IndexError:
            print('End list of elements')

    def six_elem(self, list_):
        """
        return  ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
        """
        try:
            if type (list_) == list:
                dell = list_.pop()[1::]
                dell = self.price_del_coma(dell)
                list_.append(dell)
                if list_[0] not in ['ПЕР', 'КОНЕЦ']: # ['PER','1', '0', 'FC Kuusysi', 'FC Futura', '93']
                    dell = list_.pop(0)[:-1]
                    list_.append(dell)
                else:
                    dell = list_.pop (0)
                    list_.append (dell)

                return list_  # ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
            else:
                print ('six_list Error type')
        except IndexError:
            print('End list of elements')

    def four_elem(self, list_):
        """
        return ['In-Play', 'PKKU/2', 'FC Kontu', '545']
        """
        try:
            if type (list_) == list:
                dell = list_.pop()[1::]
                dell = self.price_del_coma (dell)
                list_.append(dell)
                list_.append('-1')
                list_.reverse()
                list_.pop()
                list_.append ('-1')
                list_.append('-1')
                list_.reverse()
                return list_  # ['In-Play','In-Play', 'PKKU/2', 'FC Kontu', '545', 'In-Play']
            else:
                print('four_list Error type')
        except IndexError:
            print('End list of elements')

    def price_del_coma(self, elem:str):
        try:
            elem = elem.split(',')
            elem = ''.join(elem)
            elem = int(elem)
            return elem
        except Exception as e:
            print(e)

    def list_len(self, list_):
        try:
            # list_ = self.list_
            len_list = len(list_)
            if len_list == 4:
                return self.four_elem(list_)
            elif len_list == 6:
                return self.six_elem(list_)
            elif len_list == 7:
                return self.seven_elem(list_)
            else:
                print ('list_len > Error')
        except Exception as e:
            print (e)

    def find_coupon_table(self):
        try:
            driver = WebDriverWait(self.driver, 7)
            # driver = self.driver
            # driver.get ('https://www.betfair.com/exchange/plus/inplay/football')
            result = driver.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'coupon-table')))
            # result = self.res.find_elements_by_class_name('coupon-table')
            print(result)
            time.sleep(0.5)
            elem = result[0]
            self.elem = elem.find_elements_by_class_name('mod-link')
            print()
            # return elem
        except Exception as e:
            print ('find_coupon_table', e)
            self.driver.quit ()

    def in_play(self):
        all_match_info = []
        elem = self.elem
        for i in elem:
            list_ = []

            text = i.text
            text = text.split('\n')
            info_list = self.list_len(text)
            list_.append(info_list)

            name_of_liga = i.get_attribute ('data-competition-or-venue-name')
            list_.append(name_of_liga)

            match_url = i.get_attribute ('href')
            list_.append(match_url)

            all_match_info.append(list_)
            self.all_match_info = all_match_info
            # self.all_match_info
        # return all_match_info

    def to_dict(self):
        pass

    def append_to_db(self):
        model = InPlay()
        all_match_info = self.all_match_info
        for i in all_match_info:
            model.time_inplay = i[0][5]
            model.amaunt_match = i[0][4]
            model.runner_away = i[0][3]
            model.runner_home = i[0][2]
            model.scorre_away = i[0][1]
            model.scorre_home = i[0][0]
            model.football_liga = i[1]
            model.url_match = i[2]
            model.save()

        print('All add to base')

    def click_gb(self):
        driver = self.driver
        driver.get('https://www.betfair.com/exchange/plus/inplay/football')


        driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ssc-hls'))).click()
        # driver.find_element_by_class_name('ssc-ie').click()
        driver.find_element_by_class_name('ssc-en_GB').click()


        # self.driver.find_element_by_class_name('ssc-hls').click()

        # 'ssc-hls'
        # 'ssc-en_GB'
