# from  bf.selen_worker import BFSearch
#
# bf_search = BFSearch()
# bf_search.setUp()
# bf_search.click_gb()
# bf_search.find_coupon_table()
#
# # bf_search.in_play()
# # bf_search.append_to_db()
# bf_search.tearDown()

####
##
#


from bf.function_list import BFSearch

def main():
    go = BFSearch()

    go.setUp()
    go.click_gb()
    go.find_coupon_table()
    go.find_mod_link_inplay()
    go.in_play()
    # go.find_text()
    go.append_to_db()
    go.tearDown()


if __name__ == '__main__':
    main()



