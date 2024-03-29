from os import times
from typing import List
from urllib.request import urlopen
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
import json
from datetime import datetime
import time


@dataclass
class HttpClient:
    def request_html(self, url) -> BeautifulSoup:
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        else:
            print(response.status_code)
            return None


@dataclass
class KakaoJob:
    title: str
    url_link: str
    tags: str
    recruitment_period: str
    work_palce: str
    company: str
    emp_type: str


@dataclass
class KakaoCrawler:
    base_url: str = field(default="https://careers.kakao.com")
    target_url: str = field(default="/jobs?page=")
    http: HttpClient = field(default_factory=HttpClient)

    def find_total_page(self) -> int:
        url = self.base_url + self.target_url + "1"
        soup = self.http.request_html(url)
        page_query = soup.select_one(".change_page.btn_lst")["href"]
        page = page_query[(page_query.index("=")+1):]
        return int(page)

    def find_recruitment_by_page(self, page: str) -> List[KakaoJob]:
        url = self.base_url + self.target_url + str(page)
        soup = self.http.request_html(url)
        if soup is None:
            return None

        ul = soup.select('ul.list_jobs > li')
        item_list = []
        for li in ul:
            item = KakaoJob(
                li.select_one("h4").get_text(),
                self.base_url + li.select_one(".link_jobs")['href'],
                [a.get_text().strip()
                    for a in li.select(".list_tag > a")],
                li.select(".list_info > dd")[0].get_text(),
                li.select(".list_info > dd")[1].get_text(),
                li.select(".item_subinfo > dd")[0].get_text(),
                li.select(".item_subinfo > dd")[1].get_text()
            )
            # item_list.append(item)
            item_list.append(item.__dict__)
        return item_list


@dataclass
class FileService:
    base_json_dir: str = field(init=False, default="./json")
    base_logs_dir: str = field(init=False, default="./logs")

    def write_logs_in_json(self, file_name, source: list, text_log: str = None):
        file_json_path = self.base_json_dir + "/" + file_name + ".json"
        file_log_path = self.base_logs_dir + "/" + file_name + ".log"
        with open(file_json_path, "w") as out_file:
            json.dump(source, out_file, indent=2, ensure_ascii=False)

        if text_log is not None and len(text_log.strip()) != 0:
            with open(file_log_path, "a") as out_file:
                out_file.write(text_log + f" | 크롤링 결과 위치: .{file_json_path}")
                out_file.write("\n")


def main():
    kakao = KakaoCrawler()
    total_page = kakao.find_total_page()
    result = []

    start = time.time()
    # for p in range(1, total_page+1):
    for p in range(1, 21):
        # result.extend(kakao.find_recruitment_by_page(p))
        result.extend(kakao.find_recruitment_by_page(1))
    end = time.time()
    time_took = end - start

    now = str(datetime.now())
    data = {'timestamp': now}
    data['recruitment'] = []
    data['recruitment'].extend(result)

    f = FileService()
    text_log = f"{now} :: main >>> 크롤링 걸린시간: {time_took} | 크롤링 갯수: {len(result)}"
    f.write_logs_in_json("sample", data, text_log)


if __name__ == "__main__":
    main()
