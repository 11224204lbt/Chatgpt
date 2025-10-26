# 軟體工程期中報告  11224204林柏廷,11224210賴宣妤


## 題目:不寫一行程式碼，利用 ChatGPT 從零生成一個批量加水印工具

## 批量水印生成工具 (Batch Watermark Generator)

一個 簡單易用的 Python GUI 工具，用於 批量給圖片添加文字水印。支援 JPG、PNG 和 BMP 格式，並提供字體自訂與半透明效果，非常適合作品保護、品牌宣傳或批量處理圖片。
此專案由 Python 與 ChatGPT 協作開發，展示了 AI 輔助程式開發的實際應用。

### 功能特色

批量加水印:
一次處理資料夾內所有圖片，節省手動加水印的時間。

自動調整字體大小:
根據圖片寬度自動計算文字大小，最小字體限制為 20，適合各種尺寸圖片。

半透明水印:
水印文字疊加於圖片上，保持底圖細節清晰。JPG/PNG 都能正確呈現效果。

自選字體:
支援 .ttf TrueType 字體，使用者可選擇喜歡的字體樣式。

輸出管理:
處理後的圖片會自動存放於 output 子資料夾，原始圖片不會被覆蓋。

穩定處理:
自動忽略損壞或非圖片檔案，避免程式中斷。

## 圖例說明
![03](https://github.com/11224204lbt/Chatgpt/blob/main/1.png)
先安裝必要套件

pip install pillow



## 具體代碼

    class Node(object):
    """
    定義單向鏈表節點
    """
    def __init__(self, item):
        self.item = item
        self.next = None

    class Stack(object):
    """
    用鏈表實作堆疊，支持 push, pop, peek, is_empty, size
    """
    def __init__(self):
        self.top = None  # 指向堆疊頂端節點
        self.count = 0   # 堆疊大小

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def push(self, item):
        node = Node(item)
        node.next = self.top  # 新節點指向原頂端
        self.top = node       # 頂端更新為新節點
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法pop")
        item = self.top.item
        self.top = self.top.next  # 頂端往下一個節點移動
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法peek")
        return self.top.item

    if __name__ == '__main__':
       stack = Stack()
       stack.push(1)
       stack.push(2)
       stack.push(3)
       print("堆疊大小:", stack.size())  # 3
       print("堆疊頂端:", stack.peek())  # 3
       print("pop:", stack.pop())        # 3
       print("pop:", stack.pop())        # 2
       print("堆疊頂端:", stack.peek())  # 1
       print("堆疊大小:", stack.size())  # 1

### 中序表達式轉成後序表達式（逆波蘭表示法）       
         
    class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

    class Stack(object):
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法pop")
        item = self.top.item
        self.top = self.top.next
        self.count -= 1
        return item

     def peek(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法peek")
        return self.top.item

    def infix_to_postfix(infix_expr):
     prepare = {'*':3, '/':3, '+':2, '-':2, '(':1}

     postfix_list = []
     infix_list = infix_expr.split()
     op_stack = Stack()

    for item in infix_list:
        if item in "0123456789" or item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfix_list.append(item)
        elif item == '(':
            op_stack.push(item)
        elif item == ')':
            top = op_stack.pop()
            while top != '(':
                postfix_list.append(top)
                top = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prepare[op_stack.peek()] >= prepare[item]):
                postfix_list.append(op_stack.pop())
            op_stack.push(item)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

    if __name__ == '__main__':
      print(infix_to_postfix("A * B + C * D"))     # 輸出: A B * C D * +
      print(infix_to_postfix("( A + B ) * C"))     # 輸出: A B + C *

## 運行結果
![01](https://github.com/11224204lbt/stack/blob/main/code.png)

![01](https://github.com/11224204lbt/stack/blob/main/code1.png)

## 其他應用
堆疊還有很多其他應用，比如在系統程式設計中，四則運算會利用堆疊來達成先乘除、後加減、括號優先處理的目的。
某些程式語言在呼叫函式時，可以傳入不定數量的參數，也和堆疊的運用有關。
總的來說，在解決工程學問題時，堆疊是很常見的應用，但是大多數程式語言的函式庫都已經提供了現成工具，讓我們在開發商務軟體或系統時，能在不知不覺中使用堆疊，減少了直接碰觸堆疊的需要。
