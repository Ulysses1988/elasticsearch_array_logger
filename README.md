# elasticsearch array logger
## intasll
import logging
from elasticsearch import Elasticsearch
from es_array_logger import es_handler

es = Elasticsearch(hosts=[{"host": "127.0.0.1", "port": 9200}])
es_handler = es_handler.ESArrayHandler(es_client=es, key="test0", index="test")
ranlogger = logging.Logger('x')
ranlogger.addHandler(es_handler)
for item in range(0, 7):
    putinfo = "{:-^12}".format(item)
    ranlogger.info(putinfo)
    
    
