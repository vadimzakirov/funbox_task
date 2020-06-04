import unittest
from models import UploadLinks
from config import RedisConfig
from store.storage import MainStorage


class DomainSeparateTestCase(unittest.TestCase):

    def test_domains_without_http(self):
        test_domains = ['ya.ru',
                        'rambler.ru',
                        'stackoverflow.com']
        FakeModel = UploadLinks(links=test_domains)
        FakeModel.links = test_domains
        self.assertEqual(FakeModel.extract_domains(), test_domains)

    def test_domains_with_http(self):
        test_domains = ['http://ya.ru',
                        'https://rambler.ru',
                        'http://stackoverflow.com']
        assertion_domains = ['ya.ru',
                             'rambler.ru',
                             'stackoverflow.com']
        FakeModel = UploadLinks(links=test_domains)
        FakeModel.links = test_domains
        self.assertEqual(FakeModel.extract_domains(), assertion_domains)

    def test_full_links(self):
        test_links = ['https://pydantic-docs.helpmanual.io/usage/models/',
                      'https://www.yandex.ru/search/?text=ntcnjdsq%20url&lr=43&clid=2186621',
                      'https://nova.rambler.ru/search?query=sdfsdfsdsdfs&utm_source=head&utm_campaign=self_promo&'
                      'utm_medium=form&utm_content=search&_openstat=UmFtYmxlcl9NYWluOzs7']
        assertion_domains = ['pydantic-docs.helpmanual.io',
                             'yandex.ru',
                             'nova.rambler.ru']
        FakeModel = UploadLinks(links=test_links)
        FakeModel.links = assertion_domains
        self.assertEqual(FakeModel.extract_domains(), assertion_domains)


class RedisConnectionTest(unittest.TestCase):

    def setUp(self):
        self.store = MainStorage(RedisConfig().get_config())

    def test_redis_connection(self):
        self.assertEqual(self.store.r.ping(), True)

    def test_set_get_operation(self):
        test_key = 'test_key'
        test_value = 'TEST_VALUE'
        self.store.r.set(test_key, test_value)
        self.assertEqual(self.store.r.get(test_key).decode('utf-8'), test_value)


class StorageTest(unittest.TestCase):

    def setUp(self):
        self.store = MainStorage(RedisConfig().get_config())
        self.store.set_name = 'test_domains'

    def test_domains_range(self):
        domains_with_score = {
            1: ['ya.ru', 'rambler.ru', 'vk.com'],
            2: ['mail.ru', 'stackoverflow.ru', 'vk.com'],
            3: ['fruts.ru', 'funbox.ru']
        }
        result = ['rambler.ru', 'mail.ru',
                  'vk.com', 'ya.ru', 'fruts.ru',
                  'funbox.ru', 'stackoverflow.ru']
        for score in domains_with_score:
            self.store.store_domains(domains_with_score[score], score)
        filtered_domains = self.store.filter_domains_by_time(1, 3)
        self.store.r.delete(self.store.set_name)
        self.assertEqual(filtered_domains.sort(), result.sort())


unittest.main()
