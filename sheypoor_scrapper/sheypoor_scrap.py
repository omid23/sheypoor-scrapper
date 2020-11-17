import sys
import traceback
import requests
from bs4 import BeautifulSoup


def all_posts(city='مشهد', category='املاک', crawling_pages=10):
    try:
        page_number = 1
        all_tokens = []
        while page_number <= crawling_pages:
            url = "https://www.sheypoor.com/" + city + "/" + category + "?p=" + str(
                page_number)

            headers_sheypoor_base = {
                'authority': 'www.sheypoor.com',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                          'application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-dest': 'empty',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/80.0.3987.132 Safari/537.36',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'same-origin',
                'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
                'cookie': 'plog=False; _lba=false; analytics_campaign={'
                          '%22source%22:%22google%22%2C%22medium%22:%22organic%22}; '
                          'analytics_token=66e37d88-f3af-6ae8-26ef-010c846dbd8d; '
                          'analytics_session_token=0714239e-ea90-1c1a-43db-17f083f659b7; '
                          'yektanet_session_last_activity=3/11/2020; ts=b2ecac2f7de89ccc87c58333abdaaf38; '
                          'track_id=cbbcf53672644d61c0d6f540e7e23598; AMP_TOKEN=%24NOT_FOUND; '
                          '_ga=GA1.2.251578156.1583894892; _gid=GA1.2.413968112.1583894892; '
                          '_yngt=11b2f399-0aa2-454a-c509-8f924230ae0f; yk_sstidsmap={'
                          '%2234b53f6b-1354-4645-99a2-5c776662989a%22:%220714239e-ea90-1c1a-43db-17f083f659b7%22}; '
                          'province=%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86-%D8%B1%D8%B6%D9%88%DB%8C; provinceID=11; '
                          'city=%D9%85%D8%B4%D9%87%D8%AF; cityID=444; geo=city; '
                          'searchKey=eyJfdXJsIjoic2VhcmNoIiwiYyI6IjQzNjA2IiwiY3QiOiI0NDQiLCJyIjoiMTEifQ%3D%3D '
            }
            response = requests.request("GET", url, headers=headers_sheypoor_base)
            if response.status_code != 200:
                return 0
            response = response.text.encode('utf8').decode()
            soup_main_page = BeautifulSoup(response, 'lxml')
            posts = soup_main_page.find_all('span', {'class': 'icon-star-empty'})
            all_tokens += [post.attrs['data-save-item'] for post in posts]
            page_number += 1
    except BaseException as ex:
        ex_type, ex_value, ex_traceback = sys.exc_info()
        trace_back = traceback.extract_tb(ex_traceback)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                "File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print("\n Exception type : %s " % ex_type.__name__)
        print("\n Exception message : %s" % ex_value)
        print("\n Stack trace : %s" % stack_trace)
        return 0


def single_post_detail(token):
    try:
        additional_data = dict()

        specific_post_url = "https://www.sheypoor.com/zim-" + str(token) + ".html"
        specific_post_headers = {
            'authority': 'www.sheypoor.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-dest': 'empty',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'same-origin',
            'referer': 'https://www.sheypoor.com/%D9%85%D8%B4%D9%87%D8%AF/%D8%A7%D9%85%D9%84%D8%A7%DA%A9/%D8%B1%D9%87%D9%86-%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%AE%D8%A7%D9%86%D9%87-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'cookie': 'plog=False; _lba=false; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=66e37d88-f3af-6ae8-26ef-010c846dbd8d; analytics_session_token=0714239e-ea90-1c1a-43db-17f083f659b7; yektanet_session_last_activity=3/11/2020; ts=b2ecac2f7de89ccc87c58333abdaaf38; track_id=cbbcf53672644d61c0d6f540e7e23598; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.251578156.1583894892; _gid=GA1.2.413968112.1583894892; _yngt=11b2f399-0aa2-454a-c509-8f924230ae0f; yk_sstidsmap={%2234b53f6b-1354-4645-99a2-5c776662989a%22:%220714239e-ea90-1c1a-43db-17f083f659b7%22}; province=%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86-%D8%B1%D8%B6%D9%88%DB%8C; provinceID=11; city=%D9%85%D8%B4%D9%87%D8%AF; cityID=444; geo=city; searchKey=eyJfdXJsIjoic2VhcmNoIiwiYyI6IjQzNjA2IiwiY3QiOiI0NDQiLCJyIjoiMTEifQ%3D%3D'
        }

        response = requests.request("GET", specific_post_url, headers=specific_post_headers)
        response = response.text.encode('utf8').decode()
        soup_page_detail = BeautifulSoup(response, 'lxml')
        title = soup_page_detail.find('title').text
        top_nav = soup_page_detail.find('nav', {'id': "breadcrumbs"}).find('ul').find_all('li')
        category = top_nav[-1].text
        additional_data['category'] = category

        place = top_nav[3].find('a').text
        item_details = soup_page_detail.find('section', {'id': 'item-details'})
        if item_details != None:
            if item_details.find('span', {'class': 'item-price'}) != None:
                price = soup_page_detail.find('section', {'id': 'item-details'}).find('span',
                                                                                      {
                                                                                          'class': 'item-price'}).find(
                    'strong').text
                additional_data['price'] = price
        features = soup_page_detail.find_all('th', {'scope': 'row'})
        for feature in features:
            feature_key = feature.text
            feature_value = feature.parent.find('td').text
            additional_data[feature_key] = feature_value
        phone = soup_page_detail.find('span', {'class': 'blue'}).text
        phone = phone
        description = soup_page_detail.find('p', {'class': 'description'}).text
        img_data_slick = soup_page_detail.find('div', {'class': 'slides-wrapper'})
        image = ''

        if img_data_slick is not None:
            img = img_data_slick.find('img')['src']
            image = img

        description = description
        url = specific_post_url
        return {
            'address': place,
            'title': title,
            'description': description,
            'token': token,
            'image': image,
            'phone': phone,
            'url': url,
            'additional_data': additional_data}
    except:
        print("error occured")


if __name__ == '__main__':
    pass
