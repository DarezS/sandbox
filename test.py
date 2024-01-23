import argparse
import csv

def main():
    
    print("Hello, World!")
    parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')    # 2. パーサを作る

    # 3. parser.add_argumentで受け取る引数を追加していく
    parser.add_argument('--arg1',default = 'test2.csv', help='使うcsvファイル')    # 必須の引数を追加
    parser.add_argument('--arg2', default='dist-time', help='どんなグラフを作るか')

    args = parser.parse_args()    # 4. 引数を解析

    print('arg1='+args.arg1)
    print('arg2='+args.arg2)

    filename = args.arg1

    with open(filename, encoding='utf-8-sig', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        content = [row for row in csvreader] #{"frame": ##, "num": ##, "dist": ##}

    

if __name__ == "__main__":
    main()