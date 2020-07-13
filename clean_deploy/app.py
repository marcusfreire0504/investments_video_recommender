import os.path
from flask import Flask
import run_backend
import os
import json
import time

app = Flask(__name__)

def get_predictions():

    videos = []

    novos_videos_json = 'novos_videos.json'

    if not os.path.exists(novos_videos_json):
        run_backend.update_db()
    
    last_update = os.path.getmtime(novos_videos_json)

    #if time.time_ns() - last_update > (720*3600*1e9):
        #run_backend.update_db()

    with open("novos_videos.json", 'r') as data_file:
        for line in data_file:
            line_json = json.loads(line)
            videos.append(line_json)

    predictions = []
    for video in videos:
        predictions.append((video['video_id'], video['title'], float(video['score'])))

    predictions = sorted(predictions, key=lambda x: x[2], reverse=True)[:30]

    predictions_formatted = []
    for e in predictions:
        predictions_formatted.append("<tr><th><a href=\"{link}\">{title}</a><th><tr>{score}</th></tr>".format(title=e[1], link=e[0], score=e[2]))

    return '\n'.join(predictions_formatted), last_update


@app.route('/')
def main():
    preds, last_update = get_predictions()

    table_of_contents = """ <head><h1>Vídeos de investimento no YouTube recomendados por modelo de Machine Learning</h1></head>
    <body>
    Tempo desde a última atualização: {}
    <table>
        {}
    </table>
    </body>""". format((time.time_ns() - last_update)/1e9, preds)

    return table_of_contents

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
