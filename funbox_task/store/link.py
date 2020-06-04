from .__base__ import BaseStore
import uuid


class LinkStore(BaseStore):
    """
    Implements Redis operations with Links
    """
    def store_domains(self, domains_list: list, request_time: int):
        """
        :param domains_list: list of domains to store
        :param request_time: request time to store
        :return: True if success else raise Exception
        """
        z_mapp = {f"{str(uuid.uuid4()).split('-')[-1]}:{domain}": request_time for domain in domains_list}
        self.r.zadd(self.set_name, z_mapp)
        return True

    def filter_domains_by_time(self, time_from, time_to):
        """
        Get Redis filtration by Score
        :param time_from: timestamp filter param
        :param time_to: timestamp filter param
        :return: list of unique domains
        """
        uuid_domains = self.r.zrangebyscore(self.set_name, time_from, time_to)
        return self.delete_repeats([domain.decode("utf-8").split(':')[-1] for domain in uuid_domains])

    @staticmethod
    def delete_repeats(arr):
        return list(set(arr))

