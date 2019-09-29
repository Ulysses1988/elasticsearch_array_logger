import logging.handlers
from elasticsearch import Elasticsearch
from es_array_logger.es_handler import *


if __name__ == "__main__":
    es = Elasticsearch(hosts=[{"host": "127.0.0.1", "port": 9200}])
    es_handler = ESArrayHandler(es_client = es, key = "demacia1123", index = "m1egac111orp")
    hand_format = logging.Formatter('[%(levelname)s] %(asctime)s : %(message)s')
    es_handler.setFormatter(hand_format)
    ranlogger = logging.Logger('123')
    ranlogger.addHandler(es_handler)
    for item in range(0, 7):
        putinfo = "{:-^12}".format(item)
        print(putinfo)
        ranlogger.info(putinfo)