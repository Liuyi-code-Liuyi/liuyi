import os

def rename_images(names_file, images_dir):
    with open(names_file, 'r', encoding='utf-8') as f:
        names = [line.strip() for line in f if line.strip()]

    # 硬编码的图片顺序，根据用户最初提供的附件顺序
    # 请确保这些文件存在于 images_dir 目录下
    ordered_image_files = [
        '0a01b28cf1fcf2cfe2d71f29d731ced4.png',
        '0bc93446a10037c9dc172196e6a091d3.png',
        '0d7181956a1557a4c04a54fac101a7a9.png',
        '0e4fc158a04f115df5790aff81e5f7ed.png',
        '0e480bfcb517a317a31751d7547816a3.png',
        '0f312652ecbe7048446f4337a8534aee.png',
        '0f69525b0c7c80c3289ca7428390c961.png',
        '1d976b7d91985185f2aba402315a8d97.png',
        '02f31defa56eb14b6c0c8b29c1fd3b7c.png',
        '2a515616393fe569f8c7d91870834df9.png',
        '2eac0399608eb148c9f323bb5631b71e.png',
        '3abec6ffc979df972fb0dc7230c03529.png',
        '3cb89360d808cbfb5de4259e46137a32.png',
        '3cc87f3b0e49fa277cdf5fe026148d10.png',
        '3d9ff739bf8e5405f1d71942e892af41.png',
        '3f804589285c952bd6a1f4ae0915c233.png',
        '4b113e899126e33fe4558eb8f3763fcd.png',
        '4c6a57b5a73b7bf65ef9616c60d2722b.png',
        '4c73bff49fbdec20865f3deda396d3de.png',
        '4d5fea0afb49251aa6f92361a84ee5a7.png',
        '4ddb515e898fa18e0903379947b45494.png',
        '4e32a022a8f33372ede7f585069c483b.png',
        '05b48aa7c18c38ba677dbede07dac3bc.png',
        '05ce007803a016736db30d88ef579a82.png',
        '5a0c830d7347d2bb0c51df4815176a79.png'
    ]

    if len(names) != len(ordered_image_files):
        print(f"错误：名字文件中的名字数量 ({len(names)}) 与硬编码的图片文件数量 ({len(ordered_image_files)}) 不匹配。")
        return

    for i, new_name in enumerate(names):
        old_name = ordered_image_files[i]
        old_path = os.path.join(images_dir, old_name)
        file_extension = os.path.splitext(old_name)[1]
        new_path = os.path.join(images_dir, f"{new_name}{file_extension}")

        try:
            # 检查原始文件是否存在
            if not os.path.exists(old_path):
                print(f"错误：原始文件 \'{old_path}\' 不存在，跳过重命名。")
                continue

            # 检查目标文件是否已经存在，如果存在则跳过或处理
            if os.path.exists(new_path):
                print(f"警告：目标文件 \'{new_path}\' 已存在，跳过重命名 \'{old_name}\'。")
                continue

            os.rename(old_path, new_path)
            print(f"已将 \'{old_name}\' 重命名为 \'{new_name}{file_extension}\'")
        except OSError as e:
            print(f"重命名文件 \'{old_name}\' 失败: {e}")

if __name__ == '__main__':
    # 请根据您的实际路径修改以下两行
    names_file_path = r'D:\\下载\\python各种\\PythonProject4\\day2\\作业\\名字.txt'
    images_directory = r'D:\\下载\\python各种\\PythonProject4\\day2\\作业\\文件'
    rename_images(names_file_path, images_directory)


