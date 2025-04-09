from typing import Tuple

question_num=int(input("请输入问题的个数："))
questions=[]
def max_point(lst,current_point=0)->int:
    if len(lst)==1:#如果只有一个问题
        return current_point+lst[0][0]#直接回答这个问题，返回当前的分数加上这个问题的分数
    elif len(lst)==0:#如果没有问题
        return current_point#直接返回当前的分数
    else:#如果有多个问题
        point=lst[0][0]#这个问题的分数
        brain_power=lst[0][1]#这个问题的消耗的脑力
        #如果这个问题的消耗的脑力小于剩下的问题的数量，意味着回答完这个问题还能继续回答其他问题
        if brain_power<len(lst)-1:
            return max(max_point(lst[brain_power+1:],current_point+point),max_point(lst[1:],current_point))
        #如果这个问题的消耗的脑力大于剩下的问题的数量，意味着回答完这个问题不能继续回答其他问题
        else:return max(current_point+point,max_point(lst[1:],current_point))
#建立一个空列表，用来存储问题，每个问题是一个元组，元组的第一个元素是得分，第二个是消耗的脑力
for i in range(question_num):
    question=input()
    lst_question=question.split()
    tpl_question=(int(lst_question[0]),int(lst_question[1]))
    questions.append(tuple(tpl_question))
print(max_point(questions))



