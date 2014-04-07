import pstats
p = pstats.Stats('profile.txt')

p.sort_stats('time').print_stats(20)
