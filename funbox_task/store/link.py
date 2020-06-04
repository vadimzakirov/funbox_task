from .__base__ import BaseStore
import uuid


class LinkStore(BaseStore):

    def store_domains(self, domains_list: list, request_time: int):
        z_mapp = {f"{str(uuid.uuid4()).split('-')[-1]}:{domain}": request_time for domain in domains_list}
        self.r.zadd(self.set_name, z_mapp)
        return True

    def filter_domains_by_time(self, time_from, time_to):
        uuid_domains = self.r.zrangebyscore(self.set_name, time_from, time_to)
        print(uuid_domains)
        return self.delete_repeats([domain.decode("utf-8").split(':')[-1] for domain in uuid_domains])

    @staticmethod
    def delete_repeats(arr):
        return list(set(arr))

