import logging
from elasticsearch import ElasticsearchException
from elasticsearch.client import IndicesClient

__all__ = [
    "IndexNotFoundError",
    "ESArrayHandler",
]


class IndexNotFoundError(ElasticsearchException):
    """
    raise elasticsearch index not found
    """


class ESArrayHandler(logging.Handler):

    __DEFAULT_MAX_MESSAGE = 16777216
    __DEFAULT_KE_NAME = "logs"

    def __init__(self, es_client, key, index=__name__, max_messages=__DEFAULT_MAX_MESSAGE, level=logging.NOTSET):
        logging.Handler.__init__(self, level)
        self.index = index
        self.key = key
        self.es_client = es_client
        self.max_messages = max_messages
        if not IndicesClient(es_client).exists(index):
            raise IndexNotFoundError
        self.es_client.index(index=index, body={ESArrayHandler.__DEFAULT_KE_NAME:list(), "count":0}, id=self.key)

    def emit(self, record):
        try:
            source = "if (ctx._source.count < {0}){{ctx._source.{1}.add(params.{1});ctx._source.count += 1}}".format(
                self.max_messages,  ESArrayHandler.__DEFAULT_KE_NAME
            )
            body = {
                "script": {
                    "source": source,
                    "lang": "painless",
                    "params": {
                        ESArrayHandler.__DEFAULT_KE_NAME: self.format(record)
                    }
                }
            }
            self.es_client.update(index=self.index,  body=body,  id=self.key)
        except ElasticsearchException:
            pass