class CountingValleys:
    def main(n, s):
        sealevel = 0
        begin = 0
        count = 0
        for i in s:
            if i == 'D':
                if begin == sealevel:
                    count = count + 1
                begin = begin - 1
            else:
                begin = begin + 1

        return count


CountingValleys.main(5, "UUDDDDDUU")