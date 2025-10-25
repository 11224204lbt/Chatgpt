# 暑期資料結構期中報告  學號:11224204  學生:林柏廷


## 期中題目六: Stack的定義及其應用（python）

### stack簡述
Stack是一種資料結構，遵循著後進先出的原則，最晚放入堆疊的資料會被最先取出(LIFO Last-In-First-Out)，最早放入堆疊的資料會被最後取出(FILO First-In-Last-Out)

生活中的例子
想像你在疊盤子：
你先放第 1 個盤子（在最下面）
再放第 2 個盤子（在中間）
最後放第 3 個盤子（在最上面）
現在你想拿盤子，只能從「最上面」拿（第 3 個盤子），因為下面的被壓住了。
這就是 Stack 的行為。

## 圖例說明
![03](https://github.com/11224204lbt/stack/blob/main/1.png))
## 代碼作用
Node 類：

| 功能           | 用法說明         |
| ------------ | ------------ |
| `__init__`   | 建立空的棧，準備儲存資料 |
| `push()`     | 新資料放進棧頂      |
| `pop()`      | 把棧頂資料拿出來     |
| `peek()`     | 查看棧頂資料，但不移除  |
| `is_empty()` | 判斷棧是否為空      |
| `size()`     | 回傳目前棧中資料數量   |


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
