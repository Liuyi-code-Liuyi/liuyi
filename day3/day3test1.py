import requests
from bs4 import BeautifulSoup


def get_top_movies():
    # 定义爬取网址
    url = "https://movie.douban.com/chart"

    # 定义浏览器表头信息，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    # 向目标网站发送请求并获取网页源码
    rs = requests.get(url, headers=headers)

    if rs.status_code != 200:
        print(f"请求失败，状态码：{rs.status_code}")
        return

    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(rs.text, 'html.parser')

    # 获取电影条目，通常在 class 为 'pl2' 的 div 中
    movie_list = soup.find_all('div', class_='pl2')

    # 提取前十部电影的信息
    top_movies = []
    for i, movie in enumerate(movie_list[:10]):
        title_tag = movie.find('a')
        title = title_tag.text.strip() if title_tag else '未知'
        link = title_tag['href'] if title_tag else ''
        rating_tag = movie.find('span', class_='rating_nums')
        rating = rating_tag.text if rating_tag else '暂无评分'

        top_movies.append({
            '排名': i + 1,
            '电影名称': title,
            '链接': link,
            '评分': rating
        })

    # 打印前十部电影的信息
    for movie in top_movies:
        print(f"排名: {movie['排名']}, 电影名称: {movie['电影名称']}, 评分: {movie['评分']}, 链接: {movie['链接']}")


if __name__ == "__main__":
    get_top_movies()
