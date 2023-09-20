import requests
from multiprocessing import Process
import time
import sys

img_urls = [
    "https://kartinki.pics/uploads/posts/2022-03/1646983731_1-kartinkin-net-p-krasivie-kartinki-kotov-1.jpg",
    "https://kartinki.pics/uploads/posts/2022-03/thumbs/1646983745_11-kartinkin-net-p-krasivie-kartinki-kotov-12.jpg",
    "https://kartinki.pics/uploads/posts/2022-03/1646983792_19-kartinkin-net-p-krasivie-kartinki-kotov-28.jpg",
    "https://img2.akspic.ru/crops/4/9/4/4/7/174494/174494-milyj_kot-kot-kotenok-belyj_kot-privlekatelnost-1080x1920.jpg",
    "https://img1.akspic.ru/crops/6/6/8/8/3/138866/138866-bakenbardy-chernaya_koshka-dikaya_koshka-meh-kotenok-1080x1920.jpg",
    "https://img3.akspic.ru/crops/7/6/2/2/22267/22267-bengaliya-leopardovaya_koshka-dikaya_koshka-usy-kot-1080x1920.jpg"
]

"""
Запуск из терминала:

python hw4_multiprocessing.py "https://kartinki.pics/uploads/posts/2022-03/1646983731_1-kartinkin-net-p-krasivie-kartinki-kotov-1.jpg", "https://kartinki.pics/uploads/posts/2022-03/thumbs/1646983745_11-kartinkin-net-p-krasivie-kartinki-kotov-12.jpg", "https://kartinki.pics/uploads/posts/2022-03/1646983792_19-kartinkin-net-p-krasivie-kartinki-kotov-28.jpg", "https://img2.akspic.ru/crops/4/9/4/4/7/174494/174494-milyj_kot-kot-kotenok-belyj_kot-privlekatelnost-1080x1920.jpg", "https://img1.akspic.ru/crops/6/6/8/8/3/138866/138866-bakenbardy-chernaya_koshka-dikaya_koshka-meh-kotenok-1080x1920.jpg", "https://img3.akspic.ru/crops/7/6/2/2/22267/22267-bengaliya-leopardovaya_koshka-dikaya_koshka-usy-kot-1080x1920.jpg"

"""
urls = sys.argv[1:] if sys.argv[1:] else img_urls


folder_path = 'downloads/multiprocessing/'

def download(url, path):
    response = requests.get(url)
    filename = path + url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
        print(f"Загружено {url} за {time.time()-start_time:.2f} с.")
        
processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url, folder_path, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
        
    print(f'Время выполнения программы {time.time()-start_time:.2f} с.')