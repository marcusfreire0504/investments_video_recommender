import pandas as pd
import re
import joblib as jb 
from scipy.sparse import hstack, csr_matrix
import numpy as np 
import json

map_mes = {'jan.':'Jan',
             'fev.':'Feb',
              'mar.':'Mar',
              'abr.':'Apr',
              'mai.':'May',
              'jun.':'Jun',
              'jul.':'Jul',
              'ago.':'Aug',
              'set.':'Sep',
              'out.':'Oct',
              'nov.':'Nov',
              'dez.':'Dec'}

mdl_lgbm = jb.load("./modelos/lgbm_20200710.pkl.z")
title_vec = jb.load("title_vectorizer_20200710.pkl.z")

def clean_date(data):
    
    data_limpa = list(re.search(r"(\d+) de ([a-z]+)\. de (\d+)", data['watch-time-text']).group())
    if len(data_limpa) == 0:
        return None
    else:
        data_limpa = data_limpa.split('de ')
        data_limpa = [x.strip() for x in data_limpa]
        data_limpa[0] = ['0' + str(data_limpa[0]) if len(data_limpa[0]) == 1 else data_limpa[0]][0]
        data_limpa[1] = [v for k, v in map_mes.items() if k == data_limpa[1]][0]
        data = '-'.join(data_limpa)

        return pd.to_datetime(data)

def clean_view(data):

    raw_views_str = re.match(r"(\d+\.?\d*)", data['watch-view-count'])
    if raw_views_str is None:
        return 0
    
    raw_views_str = raw_views_str.group(1).replace(".", "")

    return int(raw_views_str)

def compute_features(data):

    if 'watch-view-count' not in data:
        return None

    publish_date = clean_date(data)
    if publish_date is None:
        return None


    views = clean_views(data)
    title = data['watch-title']

    features = dict()

    features['tempo_desde_pub'] = (pd.Timestamp.today() - publish_date) / np.timedelta64(1, 'D')
    features['views'] = views
    features['views_por_dia'] = features['views'] / features['tempo_desde_pub']
    del features['tempo_desde_pub']

    vectorized_title = title_vec.transform([title])

    num_features = csr_matrix(np.array([features['views'], features['views_por_dia']]))
    feature_array = hstack([num_features, vectorized_title])

    return feature_array


def compute_prediction(data):
    feature_array = compute_features(data)

    if feature_array is None:
        return 0

    p = mdl_lgbm.predict_proba(feature_array)[0][1]

    log_data(data, feature_array, p)

    return p

def log_data(data, feature_array, p):

    #print(data)
    video_id = data.get('og:video:url', '')
    data['prediction'] = p
    data['feature_array'] = feature_array.todense().tolist()
    #print(video_id, json.dumps(data))


    