import pstats
p=pstats.Stats('dijresults.txt')
p.sort_stats('cumulative').print_stats(35)
p=pstats.Stats('bfordresults.txt')
p.sort_stats('cumulative').print_stats(35)
