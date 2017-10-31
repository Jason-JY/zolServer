import sys
reload(sys)
sys.setdefaultencoding('utf8')
import subprocess


class scrapy:
    @classmethod
    def scrapy(self):
        cmd1 = "cd /home/jason/project/zol"
        cmd2 = "scrapy crawl cpuSpider"
        cmd3 = "scrapy crawl memSpider"
        cmd4 = "scrapy crawl boardSpider"
        cmd5 = "scrapy crawl powerSpider"
        cmd6 = "scrapy crawl radiatorSpider"
        cmd7 = "scrapy crawl graphicSpider &"
        cmd=cmd1+"&&"+cmd2+"&&"+cmd3+"&&"+cmd4+"&&"+cmd5+"&&"+cmd6+"&&"+cmd7

        subprocess.Popen(cmd,shell=True)
