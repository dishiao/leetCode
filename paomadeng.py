'''
    有意思的跑马灯
    1. 每次切片 然后
    2. 把 第一个字放在最后一个
    3. 清屏 
    4. 重新输出
'''
import os 
import time 

def main():
    content = '让我们撒欢儿跑。。。'
    while True:
        # 清屏
        os.system('cls')
        print (content)
        # 休眠300毫秒
        time.sleep(0.3)
        content = content[1:] + content[0]

if __name__=='__main__':
    main()
