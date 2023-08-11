---
layout: post
title: Algorithm Training Camp Day 2
subtitle: Array - Binary Search and Two Pointers
thumbnail-img: ""
share-img: 
tags: [Algorithm, LeetCode, Go]
---

> 2023-08-10

今天的主题仍然是数组。三道题分别是双指针、滑动窗口和模拟

都是很基础的算法题，但是仍然不可以掉以轻心。

### 977

> [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
>
> Easy
>
> Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
> 
> Example 1:
> Input: nums = [-4,-1,0,3,10]
> Output: [0,1,9,16,100]
> Explanation: After squaring, the array becomes [16,1,0,9,100].
> After sorting, it becomes [0,1,9,16,100].
>
> Example 2:
> Input: nums = [-7,-3,2,3,11]
> Output: [4,9,9,49,121]
> Explanation: After squaring, the array becomes [49,9,4,9,121].
> After sorting, it becomes [4,9,9,49,121].

读题可知，这道题是让我们对数组中的每个元素的平方进行排序。
不动脑子想呢，就是先对数组中的每个元素进行平方，然后再进行排序。

```go
func sortedSquares(nums []int) []int {
    for i := 0; i < len(nums); i++ {
        nums[i] = nums[i] * nums[i]
    }
    sort.Ints(nums)
    return nums
}
```

但是这样的时间复杂度是`O(nlogn)`，题目中要求我们的时间复杂度是`O(n)`。

这里我们可以利用数组的有序性，使用双指针的方法，从数组的两端开始遍历，比较两个指针指向的元素的平方的大小，将较大的元素放入结果数组的末尾并移动相应的指针。

当两个指针相遇时，说明遍历结束，返回结果数组即可。

于是我们可以很轻松地得到以下代码：

```go
func sortedSquares(nums []int) []int {
    var head, tail = 0, len(nums) - 1
    ans := make([]int, len(nums))
    for(head <= tail){
        i := tail-head
        if nums[head]*nums[head] > nums[tail]*nums[tail] {
            ans[i] = nums[head] * nums[head]
            head ++
        } else {
            ans[i] = nums[tail] * nums[tail]
            tail --
        }
    }
    return ans
}
```

这样这道题就解出来了，速度上击败93%。当然还可以更快:看到那句`i = tail-head`了吗？ 我们每次设置下表都是重新计算角标的，但是他其实只会稳定的每个循环-1，所以我们可以轻松地将其提出来放到循环中，这样就可以节省一些时间了。

```go
func sortedSquares(nums []int) []int {
    var head, tail, i = 0, len(nums) - 1, len(nums) - 1
    ans := make([]int, len(nums))
    for head <= tail {
        if nums[head]*nums[head] > nums[tail]*nums[tail] {
            ans[i] = nums[head] * nums[head]
            head ++
        } else {
            ans[i] = nums[tail] * nums[tail]
            tail --
        }
        i --
    }
    return ans
}
```

leetcode的用时与内存计算并不是很精确，并且会受到生成的测试用例之间的影响，两种算法的时间复杂度都是`O(n)`，空间复杂度都是`O(n)`，其实也不会有太大的差别。

后一种刷出了`Runtime 18 ms Beats99.5% Memory 7 MB Beats74.2%` 的成绩，但是这个成绩并不是很稳定，所以也不用太过于在意。

### 209 长度最小子数组

> [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

```text
209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
```

这道题是一道滑动窗口的题目。事实上，滑动窗口也是一种双指针的方法，只不过这里的双指针需要更多地根据情况不同进行移动。

题目的意思是给你一个数组和一个目标值，要求你找到数组中的一个连续子数组，使得这个子数组的和大于等于目标值，并且这个子数组的长度是所有满足条件的子数组中最小的。

第一想法是维护一个滑动窗口，当窗口内的元素和小于目标值时，窗口右边界向右移动，当窗口内的元素和大于等于目标值时，窗口左边界向右移动。在移动之中维护一个最小长度的变量，最后返回这个变量即可。

整个过程两个指针分别遍历了一遍数组，时间复杂度是`O(n)`，空间复杂度是`O(n)`。

```go
func minSubArrayLen(target int, nums []int) int {
    var left, right, sum, ans = 0, 0, 0, len(nums) + 1
    for right < len(nums) {
        sum += nums[right]
        for sum >= target {
            ans = min(ans, right - left + 1)
            sum -= nums[left]
            left ++
        }
        right ++
    }
    if ans == len(nums) + 1 {
        return 0
    }
    return ans
}
```

但是go 1.21.0才内置支持max和min函数，leetcode上的go还停留在1.18.1版本，所以我们需要改写一下min函数。

```go
func minSubArrayLen(target int, nums []int) int {
    var left, right, sum, ans = 0, 0, 0, len(nums) + 1
    for right < len(nums) {
        sum += nums[right]
        for sum >= target {
            if right - left + 1 < ans {
                ans = right - left + 1
            }
            sum -= nums[left]
            left ++
        }
        right ++
    }
    if ans == len(nums) + 1 {
        return 0
    }
    return ans
}
```

### 59 螺旋矩阵II

> [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

```text
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Example 1:
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]

    1 -> 2 -> 3
              |
    8 -> 9    4
    |         |
    7 <- 6 <- 5

Example 2:
    Input: n = 1
    Output: [[1]]
```

这道题是一道模拟题，目的是生成一个螺旋矩阵。我们可以先生成一个空的矩阵，然后按照螺旋的顺序填入数字即可。

```go
func generateMatrix(n int) [][]int {
    ans := make([][]int, n)
    for i := range ans {
        ans[i] = make([]int, n)
    }
```

接下来就只需要按顺序填入数字即可。这样看着容易，但是实际上就很容易维护出错。

有没有什么方法通过更数学一些的方法来生成呢？

通过观察我们发现，用左闭右开的区间来看的话，每一圈的边都是`n - 2 * l - 1`个元素，其中`l`是圈数，从0开始计数，一共有`n/2`圈，n是奇数的话最后中心会多一个n^2。

接下来我们需要知道每一圈的开始。我们可以发现，每一圈的开始都是`4 * (n - l) * l + 1`，其中`l`是圈数，从0开始计数。

```go
    for l := 0; l < n / 2; l ++ {
        max_len := n - 2 * l - 1
        start := 4 * (n - l) * l + 1
        for i := 0; i < max_len; i ++ {
            ans[l][i + l] = i + start
            ans[i + l][max_len + l] = i + max_len + start
            ans[max_len + l][max_len + l - i] = i + 2 * max_len + start
            ans[max_len + l - i][l] = i + 3 * max_len + start
        }
    }
    if n % 2 == 1 {
        ans[n / 2][n / 2] = n * n
    }
    return ans
}
```

> `n - 1`
> `(n-2*1) - 1`
> `(n-2*2) - 1`
> `(n-2*3) - 1`
>
> ==>
> `n -2l- 1`求和，l从0开始
> 计算第l圈的开始
> 首项：`n-1`
> 末项：`n - 2l + 1`
> 项数：`l`
> 和为`(n - l) * l`
> 所以每圈的开始是`4* (n - l) * l + 1`

最后leetcode的成绩是 0ms 2.1MB，时间复杂度是`O(n^2)`。击败百分百。

但是呢，我们可以从另一方面切入，通过维护二维数组的坐标来生成螺旋矩阵。

```go
func generateMatrix(n int) [][]int {
    func generateMatrix(n int) [][]int {
    left := 0
    right := n-1
    top := 0
    bot := n-1
    answer := make([][]int, n)
    k := 1
    for i:=0;i<n;i++{
        answer[i] = make([]int, n)
    }
    for left<right && top<bot{
        i := left
        for i < right{
            answer[top][i] = k
            i++
            k++
        }
        i = top
        for i < bot{
            answer[i][right]= k
            i++
            k++
        }
        i = right
        for i > left{
            answer[bot][i]  = k
            i--
            k++
        }
        i = bot
        for i > top{
            answer[i][left] = k
            i--
            k++
        }
        left++
        right--
        top++
        bot--
    }

    if left == right{
        i := top
        for i <= bot{
            answer[i][left] = k
            i++
            k++
        }
    }else if top == bot{
        i := left
        for i <= right{
            answer[top][i] = k
            i++
            k++
        }
    }
    return answer
}
```

但是这样就很蠢！写很久