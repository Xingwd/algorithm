# 测试数据
l1 = [7, 9, 5, 1, 3]
l2 = [2, 7, 9, 8, 3, 6, 1, 5 ,4]

print("测试数据l1：{0}".format(l1))
print("测试数据l2：{0}".format(l2))
print("========================")



# 冒泡排序
from sort.some_sort import bubble_sort
new_l1 = bubble_sort(l1)
new_l2 = bubble_sort(l2)
print("冒泡排序：")
print("new_l1：{0}".format(new_l1))
print("new_l2：{0}".format(new_l2))


# 选择排序
from sort.some_sort import selection_sort
new_l1 = selection_sort(l1)
new_l2 = selection_sort(l2)
print("选择排序：")
print("new_l1：{0}".format(new_l1))
print("new_l2：{0}".format(new_l2))


# 快速排序
from sort.some_sort import quick_sort
new_l1 = quick_sort(l1)
new_l2 = quick_sort(l2)
print("快速排序：")
print("new_l1：{0}".format(new_l1))
print("new_l2：{0}".format(new_l2))


# 插入排序
from sort.some_sort import insert_sort
new_l1 = insert_sort(l1)
new_l2 = insert_sort(l2)
print("插入排序：")
print("new_l1：{0}".format(new_l1))
print("new_l2：{0}".format(new_l2))


# 堆排序
print("堆排序：")
from sort.some_sort import heap_sort
new_l1 = heap_sort(l1)
new_l2 = heap_sort(l2)

print("new_l1：{0}".format(new_l1))
print("new_l2：{0}".format(new_l2))