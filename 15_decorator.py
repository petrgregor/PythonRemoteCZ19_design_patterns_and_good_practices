class FragStatistics:
    def increment_frag_count(self):
        pass

    def increment_death_count(self):
        pass

    def reset(self):
        pass


class FirstPersonShooterFragStatistics(FragStatistics):
    def __init__(self):
        self._frags_count = 0
        self._death_count = 0

    def increment_frag_count(self):
        self._frags_count += 1
        return self._frags_count

    def increment_death_count(self):
        self._death_count += 1
        return self._death_count

    def reset(self):
        self._frags_count = 0
        self._death_count = 0


class DeathCountInfoDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics

    def increment_frag_count(self):
        return self._frag_statistics.increment_frag_count()

    def increment_death_count(self):
        return self._frag_statistics.increment_death_count()

    def reset(self):
        self._frag_statistics.reset()


class DisplayCountersDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics

    def increment_frag_count(self):
        frag_count = self._frag_statistics.increment_frag_count()
        print(f"Your frag count is: {frag_count}")
        return frag_count

    def increment_death_count(self):
        death_count = self._frag_statistics.increment_death_count()
        print(f"Your death count is: {death_count}")
        return death_count

    def reset(self):
        self._frag_statistics.reset()
        print("Stats reset - KDR is equal to 0")


class FragDeathRatioDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics
        self._current_frag_count = None
        self._current_death_count = None

    def increment_frag_count(self):
        self._current_frag_count = self._frag_statistics.increment_frag_count()
        self._display_frag_deaths_ratio()
        return self._current_frag_count

    def increment_death_count(self):
        self._current_death_count = self._frag_statistics.increment_death_count()
        self._display_frag_deaths_ratio()
        return self._current_death_count

    def _display_frag_deaths_ratio(self):
        if self._current_frag_count and self._current_death_count:
            print(f"KDR is {self._current_frag_count/self._current_death_count}")

    def reset(self):
        self._frag_statistics.reset()


class FragInfoDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics

    def increment_frag_count(self):
        print("Enemy fragged")
        return self._frag_statistics.increment_frag_count()

    def increment_death_count(self):
        return self._frag_statistics.increment_death_count()

    def reset(self):
        self._frag_statistics.reset()


def main():
    statistics = FirstPersonShooterFragStatistics()

    statistics.increment_death_count()
    statistics.increment_frag_count()

    decorated_statistics = FragDeathRatioDecorator(FragInfoDecorator(DisplayCountersDecorator(DeathCountInfoDecorator(statistics))))

    decorated_statistics.increment_frag_count()
    decorated_statistics.increment_frag_count()
    decorated_statistics.increment_frag_count()
    decorated_statistics.increment_death_count()


if __name__ == '__main__':
    main()
