from  bf.selen_worker import BFSearch

bf_search = BFSearch()
bf_search.setUp()
bf_search.click_gb()
bf_search.find_coupon_table()

# bf_search.in_play()
# bf_search.append_to_db()
bf_search.tearDown()




