import math

num_of_ppl = int(input())
elev_cpst = int(input())

courses = math.ceil(num_of_ppl / elev_cpst)
print(courses)