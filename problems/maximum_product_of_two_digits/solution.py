class Solution:
    def maxProduct(self, n: int) -> int:
            new_num = str(n)
            new_num = list(new_num)
            if len(new_num) == 2:
                return (int(new_num[0]) * int(new_num[1]))
            elif len(new_num) > 2:
                best_pair = 0
                current = 0
                previous = 0
                count = 0
                for i in new_num:
                    for j in range(len(new_num)):
                        ik = int(i)
                        if count == j:
                            continue
                        else:
                            current = ik * int(new_num[j])
                        if current > best_pair:
                            best_pair = current
                        current = previous
                    count += 1
                return best_pair
                