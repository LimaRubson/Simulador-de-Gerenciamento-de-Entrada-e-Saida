import random

class DiskScheduler:
    def __init__(self, min_block, max_block, block_order):
        self.min_block = min_block
        self.max_block = max_block
        self.block_order = block_order
        self.total_seek_time = 0

    def fcfs(self):
        current_block = 0
        for block in self.block_order:
            seek_time = abs(current_block - block)
            self.total_seek_time += seek_time
            current_block = block
            print(f"Seek time for block {block}: {seek_time} time units")
        print(f"Total seek time: {self.total_seek_time} time units")

    def scan(self, start, end):
        current_block = start
        direction = 1  # 1 for moving towards end, -1 for moving towards start
        blocks_to_visit = sorted(self.block_order)
        blocks_to_visit.append(end) if direction == 1 else blocks_to_visit.append(0)
        while blocks_to_visit:
            next_block = blocks_to_visit.pop(0)
            seek_time = abs(current_block - next_block)
            self.total_seek_time += seek_time
            current_block = next_block
            print(f"Seek time for block {current_block}: {seek_time} time units")
        print(f"Total seek time: {self.total_seek_time} time units")

    def c_scan(self, start, end):
        current_block = start
        blocks_to_visit = sorted(self.block_order)
        blocks_to_visit.extend([end, 0])
        while blocks_to_visit:
            next_block = blocks_to_visit.pop(0)
            seek_time = abs(current_block - next_block)
            self.total_seek_time += seek_time
            current_block = next_block
            print(f"Seek time for block {current_block}: {seek_time} time units")
        print(f"Total seek time: {self.total_seek_time} time units")

def main():
    min_block = int(input("Enter the minimum block number: "))
    max_block = int(input("Enter the maximum block number: "))
    num_blocks = int(input("Enter the number of blocks to visit: "))
    block_order = random.sample(range(min_block, max_block + 1), num_blocks)

    scheduler = DiskScheduler(min_block, max_block, block_order)

    print("\nFCFS (First-Come, First-Served) Algorithm:")
    scheduler.fcfs()

    print("\nSCAN (Elevator) Algorithm:")
    scheduler.scan(min_block, max_block)

    print("\nC-SCAN Algorithm:")
    scheduler.c_scan(min_block, max_block)

if __name__ == "__main__":
    main()
