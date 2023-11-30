#!/usr/bin/python3
"""Function finds peak in unsorted list of integers"""


def search_peak(low, high, nums):
    """Search algo for peak function"""
    mid = (low + high) // 2
    if low == high:
        return (nums[high])
    if nums[mid] < nums[mid + 1]:
        return (search_peak(mid + 1, high, nums))
    else:
        return (search_peak(low, mid, nums))


def find_peak(list_of_integers):
    """function entry point"""
    if not list_of_integers:
        return
    else:
        return (search_peak(0, len(list_of_integers) - 1, list_of_integers))
