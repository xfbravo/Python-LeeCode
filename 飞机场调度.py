lst_input=input("请输入机场的跑道数，飞机降落占用跑道时间，飞机起飞占用跑道时间:").split()
#跑道
runway_num=int(lst_input[0])#跑道数
runways=[]#跑道，每个元素表示飞机在跑道上的剩余时间，0表示跑道空闲
runways_busy_time=[]#记录每个跑道的忙碌时间
#降落
land_time=int(lst_input[1])#飞机降落占用跑道时间
plane_to_land_index=5000#飞机降落的索引，从5001开始
plane_to_land=[]#飞机降落的队列
time_of_waiting_to_land=0#飞机降落的总等待时间
#起飞
takeoff_time=int(lst_input[2])#飞机起飞占用跑道时间
plane_to_takeoff_index=0#飞机起飞的索引，从1开始
plane_to_takeoff=[]#飞机起飞的队列
time_of_waiting_to_takeoff=0#飞机起飞的总等待时间
for i in range(runway_num):
    runways.append(0)
    runways_busy_time.append(0)
time=0#当前时间
closed=False#机场是否关闭
while True:
    print(f'当前时间为{time}秒')
    #如果机场没有关闭，输入飞机降落和起飞的数量
    if not closed:
        lst = input().split()
        land_num = int(lst[0])
        takeoff_num = int(lst[1])

        #将要降落和起飞的飞机加入到队列中
        if land_num>0:
            for i in range(land_num):
                plane_to_land_index+=1
                plane_to_land.append(plane_to_land_index)
        if takeoff_num>0:
            for i in range(takeoff_num):
                plane_to_takeoff_index+=1
                plane_to_takeoff.append(plane_to_takeoff_index)
        if land_num<0 and takeoff_num<0:#如果输入的降落和起飞的数量都小于0，表示机场关闭，后续不再输入
            closed=True

    #将跑道的时间减去1，表示跑道的时间已经过去1秒
    for i in range(runway_num):
        if runways[i]>0:#如果跑道上有飞机，时间减去1
            runways[i]-=1
            if runways[i]==0:#如果时间减去1后跑道空闲，那么输出信息表示又空出了一个跑道
                print(f'runway {i+1} is free')
    #将可以降落和起飞的飞机移除队列，并且将飞机的降落和起飞时间加入到跑道中
    for i in range(runway_num):
        if runways[i]==0:#如果跑道空闲，else：如果不空闲的话，说明有飞机在跑道上，不进行操作
            if len(plane_to_land)>0:#如果有飞机在降落，将飞机移除队列，并且将飞机的降落时间加入到跑道中
                runways[i]=land_time
                print(f'airplane{plane_to_land.pop(0)} land on runway {i+1}')
            elif len(plane_to_takeoff)>0:#如果有飞机在起飞，将飞机移除队列，并且将飞机的起飞时间加入到跑道中
                runways[i]=takeoff_time
                print(f'airplane{plane_to_takeoff.pop(0)} takeoff on runway {i+1}')
    #将飞机加入到跑道后，查看是否有飞机在跑道上，如果有飞机，说明此跑到道正在使用
    for i in range(runway_num):
        if runways[i]>0:
            runways_busy_time[i]+=1
    #将飞机加入跑到后，查看是否有飞机在等待降落和起飞，如果有飞机，说明此飞机正在等待
    if len(plane_to_land)>0:
        time_of_waiting_to_land+=len(plane_to_land)
    if len(plane_to_takeoff)>0:
        time_of_waiting_to_takeoff+=len(plane_to_takeoff)
    #如果机场关闭，所有的飞机都已经降落和起飞完毕，退出循环
    if closed:
        plane_on_runway=False
        if len(plane_to_land)==0 and len(plane_to_takeoff)==0:
            for i in range(runway_num):
                if runways[i]>0:
                    plane_on_runway=True
                    break
            if not plane_on_runway:
                break
    time+=1
print("stimulation finished")
print(f"模拟时间为{time}秒")
print(f'飞机平均降落等待时间为%.1f秒'%(time_of_waiting_to_land/(plane_to_land_index-5000)))
print(f'飞机平均起飞等待时间为%.1f秒'%(time_of_waiting_to_takeoff/plane_to_takeoff_index))
for i in range(runway_num):
    print(f'runway {i+1} busy time is {runways_busy_time[i]} seconds')
print(f'runway average busy time percentage is {sum(runways_busy_time)/time/runway_num*100:.1f}%')
