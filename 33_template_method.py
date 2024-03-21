import time
import random


class PerformanceTestTemplate:
    def get_warmup_iterations_num(self):
        pass

    def get_iterations_num(self):
        pass

    def iteration(self):
        pass

    def run(self):
        for i in range(self.get_warmup_iterations_num()):
            self.iteration()

        iteration_execution_times = []

        for i in range(self.get_iterations_num()):
            start_timestamp = time.time()
            self.iteration()
            end_timestamp = time.time()
            iteration_execution_times.append(end_timestamp-start_timestamp)

        self.show_statistics(iteration_execution_times)

    def show_statistics(self, iteration_execution_times):
        print(f"Shortest iteration took: {min(iteration_execution_times)} s")
        print(f"Longest iteration took: {max(iteration_execution_times)} s")
        print(f"All iterations took: {sum(iteration_execution_times)} s")


class RandomListSortingPerformanceTest(PerformanceTestTemplate):
    NUMBERS_NUM = 100000

    def get_warmup_iterations_num(self):
        return 2

    def get_iterations_num(self):
        return 100

    def iteration(self):
        integers = []
        for i in range(RandomListSortingPerformanceTest.NUMBERS_NUM):
            integers.append(random.randint(0, 1000000000))

        integers.sort()


class StringAppendPerformanceTest(PerformanceTestTemplate):
    CHARS_NUM = 100000

    def get_warmup_iterations_num(self):
        return 2

    def get_iterations_num(self):
        return 100

    def iteration(self):
        str_ = ''
        for i in range(StringAppendPerformanceTest.CHARS_NUM):
            str_ += chr(random.randint(1, 128))


def main():
    test_template = RandomListSortingPerformanceTest()
    test_template.run()

    test_template = StringAppendPerformanceTest()
    test_template.run()


if __name__ == '__main__':
    main()
