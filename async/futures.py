from async.sync import request_img, save_img, show, main
from concurrent import futures

WORKERS_MAX = 20


def download_one(name):
    img_raw = request_img(name)
    show(name)
    save_img(img_raw, name)
    return name


def download_many(cc_list):
    ws_count = min(WORKERS_MAX, len(cc_list))

    with futures.ThreadPoolExecutor(ws_count) as executor:
        gen = executor.map(download_one, cc_list)

    return len(list(gen))

main(download_many)
