"""
总体思路：
1.函数：
    1.1 calculate_distance:计算两个点之间的距离
    1.2 total_distance:计算总的距离
    1.3 is_valid_solution:检查是否满足约束条件，检查每辆车的载重是否超出容量，检查是否所有客户点都被分配
    1.4 generate_initial_solution:生成初始解
2.模拟退火算法：
    2.1 生成初始解，计算初始解的总距离，将最优解和最优距离先设置为初始解和初始距离
    2.2 迭代max_iterations次,每次迭代中:
        2.2.1 生成新解，在原来解的基础上进行随机的修改
        2.2.2 判断新解是否满足约束条件
        2.2.3 如果不满足约束条件,直接跳过。如果满足约束条件,计算新解的总距离,并计算新解与旧解的差值delta
        2.2.4 如果delta小于0,说明新解更好，直接接受新解，并将当前解设置为新解。
        2.2.5 如果delta大于0,不舍弃新解,仍然以一定的概率接受新解（跳出局部最优,以寻找全局最优）,并将当前解设置为新解。
        2.2.6 比较当前解与最优解的距离，如果当前解更好，则更新最优解和最优距离。
        2.2.7 退火: 温度逐渐降低,直到小于1e-50为止。
    2.3 返回最优解和最优距离
3.输出结果：
    3.1 输出每辆车的路径
    3.2 输出最短距离
    3.3 输出花费时间

"""

import math
import random
import time


# 计算两个点之间的距离
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# 计算总的距离
def total_distance(routes, spots):
    distance = 0
    for route in routes:
        for i in range(len(route) - 1):
            distance += calculate_distance(spots[route[i]], spots[route[i + 1]])
    return distance


# 检查是否满足约束条件
def is_valid_solution(routes, spots, capacity):
    # 检查每辆车的载重是否超出容量
    for route in routes:
        load = sum(spots[customer][2] for customer in route if customer != 0)
        if load > capacity:
            return False
    # 检查是否所有客户点都被分配
    assigned_customers = set(customer for route in routes for customer in route)
    all_customers = set(range(len(spots)))
    if not all_customers.issubset(assigned_customers):
        return False
    return True


# 生成初始解
def generate_initial_solution(spots, capacity, spot_num, car_num):
    routes = [[] for _ in range(car_num)]
    car_capacity = [capacity for _ in range(car_num)]
    customers = list(range(1, spot_num))  # 客户点编号（不包括配送中心）
    random.shuffle(customers)  # 随机打乱客户点顺序

    for customer in customers:
        for j in range(car_num):
            if spots[customer][2] <= car_capacity[j]:
                routes[j].append(customer)
                car_capacity[j] -= spots[customer][2]
                break

    for route in routes:
        route.insert(0, 0)  # 起点为配送中心
        route.append(0)  # 终点为配送中心
    return routes


# 模拟退火算法
def simulated_annealing(spots, car_num, capacity, initial_temp, alpha, max_iterations):
    global count
    # 生成初始解，计算初始解的距离，将最优解和最优距离先设置为初始解和初始距离
    current_solution = generate_initial_solution(spots, capacity, len(spots), car_num)
    current_distance = total_distance(current_solution, spots)
    best_solution = current_solution
    best_distance = current_distance
    temperature = initial_temp

    for _ in range(max_iterations):
        # 生成新解，在原来解的基础上随机选择两辆车中的某个节点进行交换或路径反转或者移动客户到另一辆车
        new_solution = [route[:] for route in current_solution]
        odds = random.random()
        if odds < 0.33:
            # 随机交换car1和car2的其中两个客户点
            car1, car2 = random.sample(range(car_num), 2)
            if len(new_solution[car1]) > 2 and len(new_solution[car2]) > 2:
                index1 = random.randint(1, len(new_solution[car1]) - 2)
                index2 = random.randint(1, len(new_solution[car2]) - 2)
                new_solution[car1][index1], new_solution[car2][index2] = (
                    new_solution[car2][index2],
                    new_solution[car1][index1],
                )
        elif odds < 0.66:
            # 随机选择一辆车，随机选择这辆车的路径的一个区间进行路径反转（前提是至少有两个客户，也就是路径长度最少为4）
            car = random.randint(0, car_num - 1)
            if len(new_solution[car]) > 3:
                start = random.randint(1, len(new_solution[car]) - 3)
                end = random.randint(start + 1, len(new_solution[car]) - 2)
                new_solution[car][start : end + 1] = reversed(
                    new_solution[car][start : end + 1]
                )
        else:
            # 随机选择两辆车，随机选择一号车的一个客户点，将其插入到二号车的路径中的随机一个地方
            car1, car2 = random.sample(range(car_num), 2)
            if len(new_solution[car1]) > 2 and len(new_solution[car2]) > 2:
                index1 = random.randint(1, len(new_solution[car1]) - 2)
                index2 = random.randint(1, len(new_solution[car2]) - 2)
                customer = new_solution[car1].pop(index1)
                new_solution[car2].insert(index2, customer)

        # 如果不符合条件，直接跳过，不用进行退火
        if not is_valid_solution(new_solution, spots, capacity):
            continue

        # 如果符合条件，计算距离
        new_distance = total_distance(new_solution, spots)
        delta = new_distance - current_distance

        # 以一定的概率接受更差的解（跳出局部最优，以寻找全局最优），如果新解更好，那么直接接受
        if delta < 0 or random.random() < math.exp(
            -delta / temperature
        ):  # 随着温度的降低，接受更差解的概率也降低
            current_solution = new_solution
            current_distance = new_distance

        # 如果距离小于当前最优解，那么更新当前最优解
        if current_distance < best_distance:
            best_solution = current_solution
            best_distance = current_distance

        # 退火
        temperature *= alpha
        if temperature < 1e-30:
            break
    # 返回最优解和最优距离
    return best_solution, best_distance


# 输出结果
def print_solution(solution):
    for i, route in enumerate(solution):
        print(f"车 {i+1}:", end=" ")
        for j in range(len(route) - 1):
            print(f"{route[j]+1} -> ", end=" ")
        print(f"{route[-1]+1}")


parts = input("请输入站点数量和车的数量（用空格隔开）:").split()
spot_num = int(parts[0])  # 站点数量
car_num = int(parts[1])  # 车的数量
capacity = int(input("请输入车的容量:"))
spots = []
# 读取每个客户的坐标，用spots列表存储坐标，spots[0]为配送中心
print("请输入每个客户的坐标（格式：客户编号 x坐标 y坐标，第一个为配送中心）:")
for i in range(spot_num):
    try:
        parts = input().split()
        if len(parts) != 3:
            raise ValueError("输入格式错误，应为：客户编号 x坐标 y坐标")
        x = int(parts[1])
        y = int(parts[2])
        spots.append((x, y))
    except ValueError as e:
        print(e)
        exit()

# 读取每个客户的需求量
print("请输入每个客户的需求量（格式：客户编号 需求量）:")
for i in range(spot_num):
    try:
        parts = input().split()
        if len(parts) != 2:
            raise ValueError("输入格式错误，应为：客户编号 需求量")
        demand = int(parts[1])
        spots[i] += (demand,)
    except ValueError as e:
        print(e)
        exit()


initial_temp = 10000  # 初始温度
alpha = 0.93  # 降温系数
max_iterations = 100000  # 最大迭代次数
solution, distance = simulated_annealing(
    spots, car_num, capacity, initial_temp, alpha, max_iterations
)
min_distance = distance  # 初始化最小距离为当前解的距离
best_solution = solution  # 记录最优解
total_time = 0  # 记录总时间
for i in range(10):
    start = time.time()  # 记录退火开始时间
    solution, distance = simulated_annealing(
        spots, car_num, capacity, initial_temp, alpha, max_iterations
    )
    end = time.time()  # 记录退火结束时间
    if distance < min_distance:
        min_distance = distance
        best_solution = solution
    total_time += end - start
# 输出结果
print_solution(best_solution)
print("最短距离:", min_distance)
print("平局花费时间:", total_time / 10)
