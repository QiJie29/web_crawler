class UrlManager():
    # 初始化定义待爬取url和已爬取url
    def __init__(self):
        self.new_urls = list()
        self.old_urls = list()

    # 添加新url
    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.append(url)

    # 添加新url组
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 获取url
    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop(0)
            self.old_urls.append(url)
            return url
        else:
            return None

    # 判断是否有待爬取url
    def has_new_url(self):
        return len(self.new_urls) > 0


if __name__ == '__main__':
    url_manager = UrlManager()

    url_manager.add_new_url("url1")
    url_manager.add_new_urls(["url1", "url2", "url3"])

    print(url_manager.new_urls, url_manager.old_urls)
    print("=" * 20)
    new_url = url_manager.get_url()
    print(url_manager.new_urls, url_manager.old_urls)
    print("=" * 20)
    new_url = url_manager.get_url()
    print(url_manager.new_urls, url_manager.old_urls)
    print("=" * 20)
    new_url = url_manager.get_url()
    print(url_manager.new_urls, url_manager.old_urls)
    print("=" * 20)
