import facebook
import json
import code
import pprint

def main():
    pp = pprint.PrettyPrinter(indent=0)

    oauth_access_token = 'OYyMOw7jo7yCDOc3PhSULnz2c8BAqGoxRJThDOQKsPegDgK7c06s4IwCR9EexZJoTNOeFtNJEKqyuFAV6dzX4SwjO5HzHYdqnl89xQC19bwc0uMKd99LVjxSykELH7NS8W6WjJ04NyiV0vazQsj7V3qouqYJ6GfSfEqc5eaUlrODpjdE7xPxRGjEh3WsI2RBzEdN7g3nWlaX8fsZrCNC2yxQJ'

    msg_pages = []
    page_number = 0
    mega_list = []

    graph = facebook.GraphAPI(oauth_access_token)
    object_to_get = "3863727091?fields=id,name,inbox"

    #fb_objects = fb_graphs[0].get_object("3863727091?fields=id,name,inbox")
    msg_pages.append(graph.get_object(object_to_get))
    
    with open('data_dump2.txt', 'a') as outfile:
        json.dump(msg_pages, outfile)
    
    #pp.pprint(fb_objects)

    #json_data = open('data_sample0.txt')
    #data = json.load(json_data)
    
    data = msg_pages[page_number]["inbox"]
    
    block_length = len(data["data"])
    block_number = 0

    msg_length = len(data["data"][block_number]["comments"]["data"])
    msg_number = 0

    for block_number in range(0, block_length):
        msg_length = len(data["data"][block_number]["comments"]["data"])
        for msg_number in range(0, msg_length):
            #print("block_number: " + str(block_number))
            #print("msg_number: " + str(msg_number))
            try:
                current = data["data"][block_number]["comments"]["data"][msg_number]
                ID = data["data"][block_number]["comments"]["data"][msg_number]["from"]["id"]
                if ID == 3863727091:
                    mega_list.append(data["data"][block_number]["comments"]["data"][msg_number]["message"])
            except:
                continue
                
    with open('data_dump.txt', 'a') as outfile:
        json.dump(mega_list, outfile)

    mega_list = []

    try:
        object_to_get = data["paging"]["next"]
        object_to_get = object_to_get.split('graph.facebook.com/')[1]
        next_page(object_to_get)
    except:
        return 

    #pp.pprint(mega_list)
    #pp.pprint(data["inbox"]["data"][0]["comments"]["data"][0]["message"])

    #code.interact(local=locals())

def next_page(object_to_get):
    print(object_to_get)
    pp = pprint.PrettyPrinter(indent=0)
    
    mega_list = []

    #fb_objects = fb_graphs[0].get_object("3863727091?fields=id,name,inbox")
    
    #pp.pprint(fb_objects)

    #json_data = open('data_sample0.txt')
    #data = json.load(json_data)
    
    new_graph = nonlocal graph
    
    data = new_graph.get_object(object_to_get)
    data = data["data"]
    pp.pprint(data)

    msg_length = len(data)
    msg_number = 0

    for msg_number in range(0, msg_length):
        try:
            mega_list.append(data[msg_number]["message"])
        except:
            continue
                
    with open('data_dump.txt', 'a') as outfile:
        json.dump(mega_list, outfile)
        
    try:
        object_to_get = data["paging"]["next"]
        object_to_get = object_to_get.split('graph.facebook.com/')[1]
        next_page(object_to_get)
    except:
        return 

main()