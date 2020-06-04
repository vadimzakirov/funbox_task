from response_types import Response
from store.storage import MainStorage
from fastapi import FastAPI, Query
from config import RedisConfig
import models
import time

config = RedisConfig().get_config()
api = FastAPI()
store = MainStorage(config)


@api.post('/visited_links/')
def upload_links(link_request: models.UploadLinks):
    request_time = int(time.time())
    try:
        store.store_domains(link_request.extract_domains(), request_time)
        return Response().json()
    except Exception as e:
        return Response(status=str(e)).json()


@api.get('/visited_links/')
def get_links(to: str, q: str = Query(None, alias="from")):
    try:
        filtered_domains = store.filter_domains_by_time(time_from=q, time_to=to)
        return Response(details={'domains': filtered_domains}).json()
    except Exception as e:
        return Response(status=str(e)).json()

