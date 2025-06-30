from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_scholar_articles():
    # 设置正确的 ChromeDriver 路径
    chrome_driver_path = r'D:\tools\chromedriver.exe'  # 替换为新的 chromedriver 路径
    service = Service(chrome_driver_path)

    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')  # 最大化窗口，模拟真实浏览器行为
    # chrome_options.add_argument('--headless')  # 如果想在后台运行浏览器，取消注释此行

    # 启动浏览器
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 访问 Google Scholar
    driver.get('https://scholar.google.com/')

    # 等待页面加载
    time.sleep(5)

    # 进行搜索，模拟用户输入（你可以自定义搜索关键词）
    search_box = driver.find_element("name", "q")  # 获取搜索框
    search_box.send_keys("machine learning")  # 输入搜索关键词（你可以修改为任何想查找的内容）
    search_box.submit()  # 提交搜索

    # 等待页面加载
    time.sleep(5)

    # 如果出现验证码，请手动完成，然后再按下一步继续
    print("请手动完成验证码并按任意键继续...")
    input("按回车键继续爬取...")

    # 获取页面的 HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 找到引用量信息及文章标题
    articles = soup.find_all('tr', {'class': 'gsc_a_tr'})

    # 提取文章标题及引用量
    for i, article in enumerate(articles[:10]):
        title_tag = article.find('a', {'class': 'gsc_a_at'})
        title = title_tag.text.strip() if title_tag else '未知标题'

        citation_tag = article.find('a', {'class': 'gsc_a_ac'})
        citations = citation_tag.text.strip() if citation_tag else '0'

        print(f"排名 {i + 1}: {title}, 引用量: {citations}")

    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    get_scholar_articles()
