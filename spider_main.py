import url_manager, html_outputer, html_downloader, html_parser
class SpiderMain():
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

        
    def craw(self, url):
        pass

if __name__ == '__main__':
    root_url = ''
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    