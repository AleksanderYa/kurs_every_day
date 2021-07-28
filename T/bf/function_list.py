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

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.T.settings")
django.setup()

from bf.models import InPlay


class BFSearch():
    list_simbol = [
        'EN',
        'END',
        'INPLAY',
        'HT',
        'H'
    ]

    def setUp(self):
        #         self.driver = webdriver.Firefox()
        PATH = r'C:\Users\Sales2\Desktop\kurs_every_day\T\chrom_driver\chromedriver.exe'
        #         PATH = r'C:\Users\yablu\OneDrive\Desktop\kurs_every_day\kurs_every_day\T\chrom_driver\chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(PATH, options=chrome_options)
        # self.driver.get('https://www.betfair.com/exchange/plus/inplay/football')
        self.driver.wait = WebDriverWait(self.driver, 7)
        print('connect to driver ok')

    def tearDown(self):
        self.driver.quit()

    def seven_elem(self, list_):
        """
        return  ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
        """
        try:
            if type(list_) == list:
                dell = list_.pop()[1::]
                dell = self.price_del_coma(dell)
                list_.append(dell)
                if list_[:1] not in self.list_simbol:
                    dell = int(list_.pop(0)[:-1])
                    dell_2 = int(list_.pop(0)[1::])
                    sum_ = dell + dell_2
                    list_.append(sum_)
                else:
                    dell = list_.pop(0)
                    if dell == 'HT':
                        dell = -101
                        list_.append(dell)
                    else:
                        list_.append(-200)

                return list_  # ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
            else:
                print('seven_list Error type')
        except IndexError:
            print('End list of elements')

    def six_elem(self, list_):
        """
        return  ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
        """
        try:
            if type(list_) == list:
                dell = list_.pop()[1::]
                dell = self.price_del_coma(dell)
                list_.append(dell)
                if list_[0] not in self.list_simbol:  # ['PER','1', '0', 'FC Kuusysi', 'FC Futura', '93']
                    dell = list_.pop(0)[:-1]
                    list_.append(dell)
                else:
                    dell = list_.pop(0)
                    if dell == 'HT':
                        dell = -101
                        list_.append(dell)
                    else:
                        list_.append(-301)

                return list_  # ['1', '0', 'FC Kuusysi', 'FC Futura', '93', '13']
            else:
                print('six_list Error type')
        except IndexError:
            print('End list of elements')

    def four_elem(self, list_):
        """
        return ['In-Play', 'PKKU/2', 'FC Kontu', '545']
        """
        try:
            if type(list_) == list:
                dell = list_.pop()[1::]
                dell = self.price_del_coma(dell)
                list_.append(dell)
                list_.append('-201')
                list_.reverse()
                list_.pop()
                list_.append('-1')
                list_.append('-1')
                list_.reverse()
                return list_  # ['In-Play','In-Play', 'PKKU/2', 'FC Kontu', '545', 'In-Play']
            else:
                print('four_list Error type')
        except IndexError:
            print('End list of elements')

    def price_del_coma(self, elem: str):
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
                print('list_len > Error')
        except Exception as e:
            print(e)

    def find_coupon_table(self):
        try:
            self.res = self.driver.find_elements_by_class_name('coupon-table')
            return self.res
        except Exception as e:
            print('not find_coupon_table', e)
        finally:
            print(self.res)

    def find_mod_link_inplay(self):
        try:
            if type(self.res) == list:
                res = self.res[0]
                time.sleep(0.5)
                self.res = res.find_elements_by_class_name('mod-link')
                print('Ok, finded mod-link')
                print(self.res)
                return self.res
        except Exception as e:
            print('not find_mod link', e)

    def find_mod_link_today(self):
        try:
            if type(self.res) == list:
                if len(self.res) == 2:
                    res = self.res[1]
                    time.sleep(0.5)
                    self.today = res.find_elements_by_class_name('mod-link')
                    print('Ok, finded mod-link')
                    print(self.today)
                    return self.today
                else:
                    res = self.res[0]
                    time.sleep(0.5)
                    self.today = res.find_elements_by_class_name('mod-link')
                    print('Ok, finded mod-link')
                    print(self.today)
                    return self.today
        except Exception as e:
            print('not find_mod link', e)

    def find_text(self, todays=False):
        if todays:
            if self.today:
                for i in self.today:
                    print(i.text)
        else:
            if self.res:
                # list_inplays = self.res[0]
                for i in self.res:
                    print(i.text)

    def in_play(self):
        self.all_match_info = []
        if self.res:
            for i in self.res:
                list_ = []

                text = i.text
                text = text.split('\n')
                info_list = self.list_len(text)
                list_.append(info_list)

                name_of_liga = i.get_attribute('data-competition-or-venue-name')
                list_.append(name_of_liga)

                match_url = i.get_attribute('href')
                list_.append(match_url)

                self.all_match_info.append(list_)
            print(self.all_match_info)
            return self.all_match_info
            # self.all_match_info = all_match_info

    def today_list(self, text):
        if text:
            text = text[:3]
            print(text)

    def to_day(self):
        self.all_match_info_today = []
        if self.today:
            for i in self.today:
                list_ = []

                text = i.text
                text = text.split('\n')
                info_list = self.today_list(text)

    #                 list_.append (info_list)

    #                 name_of_liga = i.get_attribute ('data-competition-or-venue-name')
    #                 list_.append (name_of_liga)

    #                 match_url = i.get_attribute ('href')
    #                 list_.append (match_url)

    #                 self.all_match_info_today.append (list_)
    #             print(self.all_match_info_today)
    #             return self.all_match_info_today

    def to_dict(self):
        pass

    def append_to_db(self):
        for i in self.all_match_info:
            model = InPlay()
            model.time_inplay = i[0][5]
            model.amaunt_match = i[0][4]
            model.runner_away = i[0][3]
            model.runner_home = i[0][2]
            model.scorre_away = i[0][1]
            model.scorre_home = i[0][0]
            model.football_liga = i[1]
            model.url_match = i[2]
            model.save()
            print(model.runner_home, ' add to base')

    def click_gb(self):
        self.driver.get('https://www.betfair.com/exchange/plus/inplay/football')
        time.sleep(4)

        self.driver.find_element_by_class_name('ssc-hls').click()
        self.driver.find_element_by_class_name('ssc-en_GB').click()
        time.sleep(7)



