import requests
from lxml import etree
import os  # 导入os模块


def one():
    url = "http://pic.netbian.com/"

    # 向目标网站发送请求并获取网页源码
    rs = requests.get(url)

    # 指定字符集
    rs.encoding = "gbk"

    # 网页源码
    body = rs.text

    # 使用 lxml 解析 HTML 内容
    html = etree.HTML(body)

    # 获取图片的 src 路径
    listImg = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")

    print("图片：", listImg)

    # 创建保存图片的文件夹（如果不存在）
    save_dir = 'd:\\images\\'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i in range(len(listImg)):
        # 拼接图片路径
        file_path = "http://pic.netbian.com" + listImg[i]

        # 获取图片内容
        rs = requests.get(file_path)

        # 获取图片的二进制内容
        img = rs.content

        # 设置图片保存路径
        path = os.path.join(save_dir, f'{i}.jpg')  # 使用os.path.join确保跨平台兼容性

        # 保存图片
        with open(path, 'wb') as f:
            f.write(img)

        print(f"图片 {i + 1} 下载完毕，保存路径: {path}")


if __name__ == "__main__":
    one()
