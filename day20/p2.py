from decrypt import *
     

numbers = parse_input()
decription_key = 811589153
mix_times = 10
mix_numbers(numbers, mix_times, decription_key)

zero = [x for x in numbers if x.val == 0][0]
zero_idx = numbers.index(zero)
num_sum = sum(numbers[(zero_idx + i) % len(numbers)].val for i in range(1000,4000,1000))

print(num_sum) # 8798438007673