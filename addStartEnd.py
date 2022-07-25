"""
Maverick
将with open 打开的文件改为自己原始文件路劲
ff 路径改为 加完开头、结尾后保存的文件
如果不加"http://"  搜索删除
如果不加结尾  '-10.4.100.111'搜索删除 
"""

ff=open("C:\\Users\\Administrator\\Desktop\\sumechw\\ip\\sumec07.txt",'w')  #打开一个文件，可写模式
with open("C:\\Users\\Administrator\\Desktop\\sumechw\\ip\\sumec0725.txt",'r') as f:  #打开一个文件只读模式
    line = f.readlines()
    i = 0
    for line_list in line:
        line_new =line_list.replace('\n','')  #将换行符替换为空('')
        # b = str(label) #主要是这一步 将之前列表数据转为str才能加入列表
        line_new = "http://"+ line_new +'-10.4.100.111' +'\n'
        i += 1
        print(line_new)
        ff.write(line_new) #写入一个新文件中
