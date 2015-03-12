import pstats
p=pstats.Stats('dijresults.txt')
p.sort_stats('cumulative').print_stats(35)
