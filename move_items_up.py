import os
import shutil
import send2trash

def move_items_up(folders):
    for folder in folders:
        # 获取文件夹内的所有子文件夹和文件
        items = os.listdir(folder)

        for item in items:
            item_path = os.path.join(folder, item)
            destination = os.path.join(os.path.dirname(folder), item)

            # 移动子文件夹和文件到上一层
            shutil.move(item_path, destination)

        # 将文件夹移动到回收站
        send2trash.send2trash(folder)

def main():
    while True:
        print("请输入要处理的文件夹路径，每个路径用回车分隔，输入完成后按回车两次结束输入：")

        folders = []
        while True:
            folder = input()
            if folder == "":
                break
            folders.append(folder)

        if not folders:
            print("没有输入任何文件夹路径。")
        else:
            move_items_up(folders)
            print("文件和文件夹已上移一层，并且文件夹已移动到回收站。")

        # 询问用户是否继续
        continue_input = input("是否继续处理其他文件夹？(y/n): ").strip().lower()
        if continue_input != 'y':
            break

if __name__ == "__main__":
    main()
