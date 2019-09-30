# elasticsearch array logger
将日志按照组格式存储到elasticsearch，每条日志为一个数组元素

## Intasll 安装
source install
```
python setup.py install
```
pypi install
```
pip install es-array-logger
```
## Usage 使用
```
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
```
_doc in Elasticsearch 在Elasticsearch中查询文档
```
{
"_index": "test",
"_type": "_doc",
"_id": "test0",
"_version": 8,
"_score": 1,
"_source": {
    "count": 7,
    "logs": [
        "[INFO] 2019-09-30 15:11:53,502 : -----0------",
        "[INFO] 2019-09-30 15:11:53,552 : -----1------",
        "[INFO] 2019-09-30 15:11:53,581 : -----2------",
        "[INFO] 2019-09-30 15:11:53,602 : -----3------",
        "[INFO] 2019-09-30 15:11:53,623 : -----4------",
        "[INFO] 2019-09-30 15:11:53,652 : -----5------",
        "[INFO] 2019-09-30 15:11:53,674 : -----6------"
        ]
    }
}
```
    
    
