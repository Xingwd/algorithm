'''
冒泡排序
对序列进行遍历，遍历过程中如果发现相邻两个元素，满足比较条件，则进行交换，
一次遍历之后最大的元素被移动到对尾，然后进行第二次遍历，直到队列有序。
时间复杂度：O(n*n)
空间复杂度：O(1)
'''
def bubble_sort(list):
    # 获取list长度，用来指示循环多少轮
    length = len(list)

    # 循环 length-1 轮
    # range函数的范围包括0，不包括length，也就是说i的最大值是length-1-1
    # 循环轮数就是 0 到 length-2
    for i in range(0, length-1):
        # 设置标记，用来标记在本轮比较中是否进行了交换
        mark = 0
        # 每轮比较 length-1-i 次，因为每比较一轮，就可以固定一个元素，比较次数就会减少一次
        for j in range(0, length-1-i):
            # 从第一个元素开始，相邻两个元素进行比较，这里的条件是大元素向后移，最后结果是正排
            # 如果想要倒排，则将大于号换成小于号
            if list[j] > list[j+1]:
                # 满足条件，就进行交换
                list[j], list[j+1] = list[j+1], list[j]
                mark = 1
        # 如果没有进行交换，则说明已排序完成，结束循环
        if mark == 0:
            break

    # 返回排序后的list
    return list


'''
选择排序
先找到起始数组中最小的元素，将它交换到i=0；
然后寻找剩下元素中最小的元素，将它交换到i=1的位置…… 
直到找到第二大的元素，将它交换到n-2的位置。
这时，整个数组的排序完成。
时间复杂度：O(n*n)
空间复杂度：O(1)
'''
def selection_sort(list):
    # 获取list长度
    length = len(list)

    # 选择length-1轮
    for i in range(0, length-1):
        # 每轮中，第i个元素之后的每个元素都与第i个元素进行比较
        # 满足条件就交换，保证第i个元素在这轮比较过的元素中是最小的
        for j in range(i+1, length):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]

    return list


'''
快速排序
任意设置一个基准元素，一般是第一个或者最后一个，
将序列以该基准元素为基准，分割成比他小的一部分和比他大的一部分，
此时，该基准元素所在的位置就是排序终了之后的准确位置，
在对左右两边的序列继续执行同样的操作，直整个个序列有序。
时间复杂度：O(n*logn)
空间复杂度：O(n*logn)
'''
def quick_sort(list):
    if list == []:
        return []
    else:
        first = list[0]
        left_list = [i for i in list[1:] if i < first]
        right_list = [i for i in list[1:] if i > first]
        return quick_sort(left_list) + [first] + quick_sort(right_list)


'''
插入排序 
将序列的第一个元素当做已经排序好的序列，然后从后面的第二个元素开始，逐个元素进行插入，直到整个序列有序为止。
时间复杂度：O(n*n)
空间复杂度：O(1)
'''
def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        j = i
        while j > 0:
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]

            j = j-1

    return list


'''
堆排序 
它是选择排序的一种。
可以利用数组的特点快速定位指定索引的元素。
堆分为大根堆和小根堆，是完全二叉树。
大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
排序思想：以正排为例，
1）将堆排列成大根堆，这时，根就是数组中的最大值；
2）将根(最大值)与末位(堆的最后一个节点，也是数组的最后一个元素)，这时最大值就放在了最后；
3）将堆排除掉一个节点(也就是数组的最后一个元素)，继续1），2）步操作，这样就会将数组中第二大的元素放到倒数第二位；
4）如此循环，直到排序完成。
'''
def heap_sort(list):
    # 从最大长度依次递减循环，每次循环构建一个大根堆
    for i in range(len(list), 0, -1):
        # 从最后一个父节点向根节点遍历
        for p in range((i//2)-1, -1, -1):
            child = 2 * p + 1
            # i代表当前的数组长度
            # 判读是否有右子节点，如果有，比较左右子节点大小，切换到大的那个
            if child + 1 < i:
                if list[child + 1] > list[child]:
                    child = child + 1

            if list[child] > list[p]:
                list[p], list[child] = list[child], list[p]

        # 交换当前大根堆的根元素和最后一个元素
        list[0], list[i-1] = list[i-1], list[0]

    return list



