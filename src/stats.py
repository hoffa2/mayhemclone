import pstats
import os
p = pstats.Stats(os.path.join("../", "profile.txt"))

p.sort_stats('time').print_stats(20)
