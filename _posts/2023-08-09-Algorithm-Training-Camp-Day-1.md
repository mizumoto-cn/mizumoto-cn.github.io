# Algorithm Training Camp Day 1

> 2023-08-09

> 大学毕业之后好久没有好好去刷一下算法题了。这次基于某些原因，决定开始刷一下算法题，希望能够坚持下去。
> 为了鞭策自己，决定每天都写一篇博客，记录一下自己的学习过程。

## Day1 数列1

数组算是比较基础的题目类型了。每次刷题都是从数组开始然后不了了之（笑）。基础的数组题用的比较多的是二分查找、双指针滑动这些方法，熟练之后切起题来也是比较顺手的。

第一天的题目比较简单，是[704](<https://leetcode.com/problems/binary-search/>)和[27](<https://leetcode.com/problems/remove-element/>)。第一题是二分查找，第二题是双指针。

### 704. Binary Search

> Easy
>
> Given an array of integers nums which is sorted in ascending order, and an integer target,
> write a function to search target in nums.
>
> If target exists, then return its index. Otherwise, return -1.
>
> You must write an algorithm with O(log n) runtime complexity.
>
> Example 1:
>
> Input: nums = [-1,0,3,5,9,12], target = 9
> Output: 4
> Explanation: 9 exists in nums and its index is 4
>
> Example 2:
>
> Input: nums = [-1,0,3,5,9,12], target = 2
> Output: -1
> Explanation: 2 does not exist in nums so return -1
>
> Constraints:
>
> 1 <= nums.length <= 10^4
> -10^4 < nums[i], target < 10^4
> All the integers in nums are unique.
> nums is sorted in ascending order.

[题解](<https://github.com/mizumoto-cn/leetcode-go/blob/main/q704/ans.go>)：

从一个比较简单易懂的写法开始吧：

```go
func search(nums []int, target int) int {
    if len(nums) == 0 {
        return -1
    }
    return binarySearch(nums, target, 0, len(nums)-1)
}

func binarySearch(nums []int, target int, left int, right int) int {
    if left > right {
        return -1
    }
    mid := (left + right) / 2
    if nums[mid] == target {
        return mid
    }
    if nums[mid] > target {
        return binarySearch(nums, target, left, mid-1)
    }
    return binarySearch(nums, target, mid+1, right)
}
```

这个写法比较容易看懂，如果要追求更加简洁的写法，可以这样：

```go
func search(nums []int, target int) int {
    l, r := 0, len(nums)-1
    for l <= r {
        mid := l + (r-l)>>1 // avoid overflow
        if nums[mid] == target {
            return mid
        } else if nums[mid] > target {
            r = mid - 1 // mid is bigger than target, so r = mid - 1
        } else {
            l = mid + 1 // mid is smaller than target, so l = mid + 1
        }
    }
    return -1
}
```

第二种写法有一些旧时代oi的常用写法的影子，比如`l + (r-l)>>1`这种写法，避免了`l + r`的溢出问题。另外，`l = mid + 1`和`r = mid - 1`这种写法也是比较常见的。

二分查找的关键在于找到中间值，然后根据中间值和目标值的大小关系来缩小查找范围。这里有一个小技巧，就是`l = mid + 1`和`r = mid - 1`这种写法，可以避免死循环。如果写成`l = mid`和`r = mid`，那么当`l == r`的时候，如果`nums[mid]`不等于`target`，那么就会陷入死循环。

### 27. Remove Element

> Easy

[题解](<https://github.com/mizumoto-cn/leetcode-go/blob/main/q27/ans.go>)：

```go
func removeElement(nums []int, val int) int {
    k := 0
    for _, n := range nums {
        if n != val {
            nums[k] = n
            k++
        }
    }
    return k
}
```

这道题用暴力方法遍历两次也可以做，因为leetcode给的n比较小，时间和内存都比较富裕。但是这道题的考点应该是双指针，所以还是用双指针来做吧。

乍一看代码，有的朋友可能会感到惊讶：第二个指针在哪里呢？其实在这个循环中，省略掉的_下标指针才是第一个指针，而`k`才是第二个指针。

这道题的思路是，用一个指针`k`来记录当前不等于`val`的元素的个数，然后遍历数组，如果当前元素不等于`val`，那么就把当前元素放到`nums[k]`的位置，然后`k++`。这样遍历完一遍之后，`k`就是不等于`val`的元素的个数，而且`nums[0:k]`就是不等于`val`的元素。

### 拓展

二分查找和双指针是两种比较泛用的算法，因而也有许多题目。
现拓展如下:

#### Binary Search

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
|704|[Binary Search](https://leetcode.com/problems/binary-search/)|[Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q704/ans.go)|Easy|
| 35| [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q35/ans.go) | Easy |
| 69| [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | [Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q69/ans.go) | Easy |
|367| [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)|[Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q367/ans.go)|Easy|

二分法核心在于两点：

- 找到中值
- 缩小查找范围

上面的题目中间，平方根一题比较有趣。
出去最基础的朴素二分法，还可以用牛顿法进行近似计算。
不知道你们大学时候数学分析老师有没有教你们这些呢？

```go
// Newton's method: https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_Newton's_method
// One way of calculating √n and isqrt(n) is to use Heron's method, which is a special case of Newton's method,
// to find a solution of the equation x^2 − n = 0, giving the iterative formula:
// x[k+1] = (x[k] + n/x[k]) / 2 , k ≥ 0, x[0] > 0
// The sequence x[k] converges quadratically to √n, as k → ∞.
func mySqrt(x int) int {
    // if x == 0 {
    //     return 0
    // }
    if x == 1 {
        return 1
    }
    mid := x >> 1
    for mid*mid > x {
        mid = (mid + x/mid) >> 1
    }
    return mid
}
```

#### Two Pointers

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
| 27| [Remove Element](https://leetcode.com/problems/remove-element/) | [Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q27/ans.go) | Easy |
| 26| [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q26/ans.go) | Easy |
|283|[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|[Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q283/ans.go)|Easy|
|844|[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)|[Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q844/ans.go)|Easy|
|977|[Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)|[Go](https://github.com/mizumoto-cn/leetcode-go/blob/main/q977/ans.go)|Easy|
