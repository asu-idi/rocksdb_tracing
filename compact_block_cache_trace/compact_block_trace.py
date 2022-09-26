




compact_block_file_name = "/tmp/compact_block_trace/compact_block_trace_file"



compact_block_file = open(compact_block_file_name, 'r')
lines = compact_block_file.readlines()

print(len(lines))


compact_block_time_dict = {}

compact_blocks = []

for line in lines:
    # print(line)
    fields = line.split(',')
    block_id = fields[1]
    time = fields[0]
    compact_block_time_dict[block_id] =  time
    compact_blocks.append((time, 0))



evict_file_name = "/tmp/evict_block_human_file"

evict_file = open(evict_file_name, 'r')
evict_lines = evict_file.readlines()


print(len(evict_lines))


evict_count = 0
miss_count = 0

accessed = {}
for evict_line in evict_lines:
    fields = evict_line.split(',')
    block_id = fields[1]
    time = fields[0]
    if block_id in compact_block_time_dict:
        # print("block id: {}, cur time {}, orig time {}".format(block_id, time, compact_block_time_dict[block_id]))
        evict_count += 1
        compact_blocks.append((time, 1))
        if block_id in accessed:
            print("{} already visited, orig time {}, cur time {} ".format(block_id, compact_block_time_dict[block_id], time))
        accessed[block_id] = 1
    else:
        miss_count += 1

print("evict count %d, miss count %d, compact block count: %d" % (evict_count, miss_count,len(lines)))

exit
in_cache_count = 0

# sorter = lambda x: (x[0], x[1])
# sorted_compact_blocks = sorted(compact_blocks,  key=sorter)

# print(sorted_compact_blocks)
# sort(compact_blocks)
# print("len of results is %d" % len(sorted_compact_blocks))


