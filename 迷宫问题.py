'''
迷宫有一个入口，一个出口。一个人从入口走进迷宫，目标是找到出口。阴影部分和迷宫的外框为墙，每一步走一格，每格有四个可走的方向，探索顺序为地图方向：南（下）、东（右）、北（上）、西（左）。

迷宫示意图
0 0 0 0 0 1 0 0
1 0 1 1 0 0 0 0
0 0 0 1 1 1 0 1
0 1 1 1 0 0 0 0
0 0 0 0 1 0 1 1
1 1 0 0 0 0 0 0
0 1 1 1 0 1 0 0
0 0 0 0 0 0 0 0->出口
输入：输入迷宫数组。第一行数据表示一个 n*n (n<=100)的迷宫；第二行开始的n行为迷宫数据。
其中：0表示路，1表示墙，起点在左上角 <1,1> 的位置，终点在右下角 <n,n> 的位置。
输出：若有解，输出从入口到出口的一条路径，否则输出 there is no solution!
例（上图所示的迷宫数组）
'''
scale=input('请输入迷宫的规模,行数n，列数m：')
scl=scale.split()
n=int(scl[0])#行数
m=int(scl[1])#列数
maze=[[0 for i in range(n)] for j in range(n)]#建立一个二维数组 0~n-1
path=[]#记录当前的路径
for i in range(n):
    temp=input().split()
    for j in range(m):
        maze[i][j]=int(temp[j])#记录迷宫的每个点的值
visited=[[0 for i in range(n)] for j in range(m)]#记录当前位置是否被访问过,0表示未访问，1表示访问过
row=0#当前行
col=0#当前列
path.append((row,col))#当前点加入路径
visited[row][col]=1#当前点被访问过
found=False#是否找到出口
while found==False:
    #如果下一个位置的visited是0，表示没有被访问过，如果是1，表示已经被访问过，并且一定走不通
    if row+1<n and visited[row+1][col]==0 and maze[row+1][col]==0:#如果下方的点没有被访问过，并且是0
        path.append((row+1,col))
        row=row+1
        visited[row][col]=1
    elif col+1<m and visited[row][col+1]==0 and maze[row][col+1]==0:#如果右方的点没有被访问过，并且是0
        path.append((row,col+1))
        col=col+1
        visited[row][col]=1
    elif row-1>=0 and visited[row-1][col]==0 and maze[row-1][col]==0:#如果上方的点没有被访问过，并且是0
        path.append((row-1,col))
        row=row-1
        visited[row][col]=1
    elif col-1>=0 and visited[row][col-1]==0 and maze[row][col-1]==0:
        path.append((row,col-1))
        col=col-1
        visited[row][col]=1
    else:#如果四个方向都没有路了，那么久回到上一个位置
        if len(path)!=0:
            lastPosition=path.pop()
            row=lastPosition[0]
            col=lastPosition[1]
            visited[row][col]=1
            continue
        else:#如果路径为空，说明没有出口
            print("没有出口")
            break
    if row==n-1 and col==m-1:#如果到达出口
        found=True
        for i,j in path:
            print(f'<{i+1},{j+1}>',end=' ')
        break
