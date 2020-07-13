from get_data import *
from ml_utils import *
import time

queries = ['investimentos','finanças','independência+financeira']

def update_db(filename):
    with open (filename, 'w+') as output:
        for query in queries:
            for page in range(1,4): #vai coletar somente as 3 primeiras páginas do youtube
                search_page = download_search_page(query, page)
                video_list = parse_search_page(search_page)

                for video in video_list:
                    video_page = download_video_page(video['link'])
                    video_json_data = parse_video_page(video_page)

                    if 'watch-time-text' not in video_json_data:
                        continue

                    p = compute_prediction(video_json_data)

                    video_id = video_json_data.get('og:video:url', '')
                    data_front = {"title": video_json_data['watch-title'], "score":float(p), "video_id":video_id}
                    data_front["update_time"] = time.time()

                    print(video_id, json.dumps(data_front))
                    output.write("{}\n".format(json.dumps(data_front)))

