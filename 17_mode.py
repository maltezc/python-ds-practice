def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    nums_freqs = {}

    for num in nums:
        nums_freqs[num] = nums_freqs.get(num, 0) + 1

    max_freq = 0
    mode_num = None

    for num in nums_freqs.keys():
        if nums_freqs.get(num, 0) > max_freq:
            max_freq = nums_freqs.get(num, 0)
            mode_num = num

    return mode_num
