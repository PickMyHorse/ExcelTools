import pandas as pd
import os
file=input('文件路径(直接把需要拆分的excel拖到这个框框里):')
extension = os.path.splitext(file)[1] #split the path name into a pair root and ext.
filename = os.path.splitext(file)[0]
pth = os.path.dirname(file) #used to get the directory name from the specified path
data=pd.read_excel(file,0)
colpick=input('选择需要拆分的列:')
rows=data.shape[0]
cols_list=[]
for i in range(rows):
    temp=data[colpick][i]
    if temp not in cols_list:
        cols_list.append(temp)  #同一类放在一个列表中
print("生成了以下文件:")
for col in cols_list:
    new_df=pd.DataFrame()
    newfile=os.path.join(pth, str(col) + extension)  
    print(newfile)
    for i in range(0,rows):
        if  data[colpick][i]==col:
            new_df=pd.concat([new_df,data.iloc[[i]]],axis=0,ignore_index=True)
    new_df.to_excel(newfile,index=False)     

