import facebook
import json
import code
import pprint

pp = pprint.PrettyPrinter(indent=0)

oauth_access_token = 'OYyMOw7jo7yCDOc3PhSULnz2c8BAqGoxRJThDOQKsPegDgK7c06s4IwCR9EexZJoTNOeFtNJEKqyuFAV6dzX4SwjO5HzHYdqnl89xQC19bwc0uMKd99LVjxSykELH7NS8W6WjJ04NyiV0vazQsj7V3qouqYJ6GfSfEqc5eaUlrODpjdE7xPxRGjEh3WsI2RBzEdN7g3nWlaX8fsZrCNC2yxVH'

msg_pages = []
page_number = 0
mega_list = []

graph = facebook.GraphAPI(oauth_access_token)
object_to_get = "116296039?fields=id,name,inbox"

continue_paging = True

while continue_paging:
    #fb_objects = fb_graphs[0].get_object("1532538649?fields=id,name,inbox")
    msg_pages.append(graph.get_object("116296039?fields=id,name,inbox"))

    with open('kimya_dump.txt', 'w') as outfile:
        json.dump(mega_list, outfile)

    #pp.pprint(fb_objects)

    #json_data = open('data_sample0.txt')
    #data = json.load(json_data)

    data = msg_pages[page_number]
    
    key_list = list(data["inbox"]["data"][1]["comments"].keys())

    block_length = len(data["inbox"]["data"])
    block_number = 0

    msg_length = len(data["inbox"]["data"][block_number]["comments"]["data"])
    msg_number = 0

    for block_number in range(0, block_length):
        msg_length = len(data["inbox"]["data"][block_number]["comments"]["data"])
        for msg_number in range(0, msg_length):
            #print("block_number: " + str(block_number))
            #print("msg_number: " + str(msg_number))
            try:
                mega_list.append(data["inbox"]["data"][block_number]["comments"]["data"][msg_number]["message"])
            except:
                continue
                
    with open('data_dump.txt', 'a') as outfile:
        json.dump(mega_list, outfile)
        
    mega_list = []

    try:
        object_to_get = data["inbox"]["paging"]["next"]
        object_to_get = object_to_get.split('graph.facebook.com/')[1]
        page_number += 1
    except:
        continue_paging = False
        break

    #pp.pprint(mega_list)
    #pp.pprint(data["inbox"]["data"][0]["comments"]["data"][0]["message"])

    #code.interact(local=locals())