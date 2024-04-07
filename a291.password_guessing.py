from sys import stdin
output = ''         # 建立 output，最後再一次輸出 ( 不用每次執行都輸出 )
for s in stdin:     # 讀取逐行輸入
  if s.strip() == '': continue  # 如果遇到換行，就跳過
  pwd = s.split()    # 將正確的密碼變成串列
  dic = {str(k):0 for k in range(10)}   # 建立一個 key 為 0～9 的字典檔 dic
  for i in pwd: dic[i] += 1     # 使用字典檔 dic 記錄密碼中數字出現幾次
  n = int(stdin.readline())     # 再來會出現幾次嘗試的密碼
  for _ in range(n):            # 重複嘗試的次數
    ans = stdin.readline().split()    # 將嘗試的解答拆成串列
    a, b, c, d = 0, 0, pwd[:], dic.copy()
    # 建立四個變數，分別是答案 ab，複製密碼串列的 c，複製 dic 的 d
    # 由於每次判斷都會修改，為了避免修改到原始資料，複製一份出來使用
    for j in range(4):
      if ans[j] == pwd[j]:     # 如果包含數字且位置正確
        d[str(pwd[j])] -= 1    # 將字典對應 key 的數值減少 1
        a = a + 1              # a 增加 1
        c[j] = 'o1'            # 修改複製的密碼位置為 o1
        ans[j] = 'o2'          # 修改嘗試的密碼位置為 o2 ( 下次就不會比對這個 )
    for j in ans:
      if j in c and d[j]>0:    # 如果有包含且字典檔 key 的值還大於 0 ( 表示還沒有被比對 )
        d[j] -= 1              # 字典檔數值減少 1
        b = b + 1              # b 增加 1
    output = output + f'{a}A{b}B\n'   # 將結果記錄到輸出的 output
print(output)