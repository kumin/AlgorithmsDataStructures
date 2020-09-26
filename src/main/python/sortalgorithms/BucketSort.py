from typing import List

from src.main.python.sortalgorithms.AbstractSorting import AbstractSorting


class BucketSort(AbstractSorting):
    def sort(self, nums: List) -> List:
        buckets = []
        buckets_size = 10
        for i in range(buckets_size):
            buckets.append([])
        for i in range(len(nums)):
            self.insert_sorted_bucket(nums[i], int(nums[i] * buckets_size), buckets)

        return self.concat_bucket(buckets)

    def insert_sorted_bucket(self, x: int, bucket_index: int, buckets: List):
        bucket = buckets[bucket_index]
        for i in range(len(bucket)):
            if bucket[i] >= x:
                bucket.insert(i, x)
                return
        buckets[bucket_index].append(x)

    def concat_bucket(self, buckets: List) -> List:
        result = []
        print(buckets)
        for i in range(len(buckets)):
            result += buckets[i]

        return result


if __name__ == '__main__':
    sort = BucketSort()
    print(sort.sort([0.120, 0.29, 0.43, 0.36, 0.39, 0.27]))
