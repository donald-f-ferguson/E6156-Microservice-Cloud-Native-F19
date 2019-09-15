import requests
import json
import time
import multiprocessing
from queue import Queue
from time import sleep
import copy


import threading
from threading import Thread
import requests

_base_url = "https://dff-e6156.s3.amazonaws.com/E6156/mock_api/"


def get_info(**kwargs):
    sleep(1)

    info_kind=kwargs["info_kind"]
    key = kwargs["key"]
    url = _base_url + info_kind + "/" + key + ".json"
    result = requests.get(url)
    result = result.json()
    return result


def in_sequence():
    start_time = time.time()

    rsp1 = get_info(info_kind="profile_info", key="donfe1")
    rsp2 = get_info(info_kind="customer_info", key="donfe1")
    rsp3 = get_info(info_kind="account_info", key="donfe1")

    full_rsp = {
        "customer_info": rsp2,
        "profile_info": rsp1,
        "account_info": rsp3
    }

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time = ", str(elapsed_time*1000), "ms")
    print("Rsp = \n", json.dumps(full_rsp, indent=2))


def call_it(func=None, t_n=None, q=None, **kwargs):

    res = func(**kwargs)
    if q is not None:
        q.put(copy.copy((t_n, res)))


def in_parallel():

    start_time = time.time()
    q = Queue()

    ts = []

    ts.append(Thread(target=call_it,
                kwargs=dict(func=get_info, t_n="profile_info", q=q,
                info_kind="profile_info", key="donfe1")))
    ts.append(Thread(target=call_it,
                kwargs=dict(func=get_info, t_n="account_info", q=q,
                            info_kind="account_info", key="donfe1")))
    ts.append(Thread(target=call_it,
                kwargs=dict(func=get_info, t_n="customer_info", q=q,
                            info_kind="customer_info", key="donfe1")))
    for t in ts:
        t.start()


    all_res = {}
    i = 0

    done = False
    while not done:
        ans = q.get()
        all_res[ans[0]] = ans[1]
        i = i + 1
        if i > len(ts):
            done = True


        i = i + 1

    for t in ts:
        t.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time = ", str(elapsed_time * 1000), "ms")
    print("The full answer = \n", json.dumps(all_res, indent=2))


in_sequence()
in_parallel()

#t1()
