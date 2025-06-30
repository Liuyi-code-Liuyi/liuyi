from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random

def get_cnki_articles():
    # 设置 ChromeDriver 路径
    chrome_driver_path = r'D:\tools\chromedriver.exe'  # 请替换为你的 chromedriver 路径
    service = Service(chrome_driver_path)

    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')  # 最大化窗口，模拟真实浏览器行为
    # chrome_options.add_argument('--headless')  # 如果想在后台运行浏览器，取消注释此行

    # 启动浏览器
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 访问知网（CNKI）网站
    driver.get('https://www.cnki.net/')

    # 等待页面加载并处理弹出框（例如同意条款或登录）
    try:
        # 等待同意按钮可点击并点击同意
        agree_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='同意并登录']"))
        )
        agree_button.click()  # 点击“同意并登录”
        print("点击同意按钮")
    except Exception as e:
        print(f"没有找到同意按钮，可能页面已加载: {e}")

    # 等待搜索框加载，使用 WebDriverWait 进行智能等待
    try:
        # 等待搜索框可用，确保页面完全加载
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txt_SearchText"))  # 搜索框的正确定位方法
        )
    except Exception as e:
        print(f"搜索框加载失败，检查定位是否正确: {e}")
        driver.quit()
        return

    # 选择搜索字段（如 "主题"）
    try:
        # 点击选择框以显示下拉菜单
        db_field_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "DBFieldBox"))
        )
        db_field_box.click()  # 点击“主题”选择框

        # 选择“主题”搜索类型
        theme_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@value='SU']"))
        )
        theme_option.click()  # 点击“主题”选项
    except Exception as e:
        print(f"选择搜索类型失败: {e}")
        driver.quit()
        return

    # 进行搜索，模拟用户输入（你可以自定义搜索关键词）
    try:
        # 确保搜索框元素可交互并输入搜索内容
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "txt_SearchText"))
        )
        search_box.clear()  # 清空已有文本
        search_box.send_keys("机器学习")  # 输入搜索关键词

        # 模拟按下回车键（提交搜索）
        search_box.send_keys(Keys.RETURN)  # 通过回车提交搜索
    except Exception as e:
        print(f"无法输入文本或提交搜索: {e}")
        driver.quit()
        return

    # 等待页面加载，确保动态内容加载完成
    time.sleep(5)

    # 模拟页面滚动，确保所有动态内容加载
    for _ in range(3):  # 滚动页面3次，加载更多内容
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)  # 等待滚动后内容加载

    # 获取页面的 HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 打印页面内容，检查是否加载了正确的内容
    print(soup.prettify())  # 查看页面结构，确保你能找到文章数据

    # 找到引用量信息及文章标题
    # 请根据实际页面修改选择器
    articles = soup.find_all('div', class_='result')  # 确认这里是包含文章的容器

    # 提取文章标题及引用量
    if articles:
        for i, article in enumerate(articles[:10]):  # 取前10篇
            title_tag = article.find('a')  # 假设文章标题在 <a> 标签中
            title = title_tag.text.strip() if title_tag else '未知标题'

            citation_tag = article.find('span', {'class': 'citation'})  # 假设引用量信息在此
            citations = citation_tag.text.strip() if citation_tag else '0'

            print(f"排名 {i + 1}: {title}, 引用量: {citations}")
    else:
        print("没有找到文章数据，检查页面结构")

    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    get_cnki_articles()
