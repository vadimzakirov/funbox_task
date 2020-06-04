from pydantic import BaseModel
from urllib.parse import urlparse


class UploadLinks(BaseModel):
    """
    Represent /visited_links POST request body
    """
    links: list

    def extract_domains(self):
        return [urlparse(link).netloc for link in self.append_http(self.links)]

    @staticmethod
    def append_http(list_of_urls):
        http_url_list = []
        for url in list_of_urls:
            if url[:7] != 'http://' and url[:8] != 'https://':
                http_url_list.append('http://' + url)
            else:
                http_url_list.append(url)
        return http_url_list


class GetLinks(BaseModel):
    """
    Represent /visited_links GET query params
    """
    class Config:
        fields = {
            'from_': 'from'
        }

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        d['from'] = d.pop('from_')
        return d
