class SpacesModificationStrategy:
    def modify(self, inp):
        pass


class DoubleSpacesStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(' ', '  ')


class RemoveSpacesStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(' ', '')


class ReplaceWithUnderscoreStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(' ', '_')


class SpaceModificationStrategyProvider:
    def get(self, strategy_type):
        if strategy_type == 'DOUBLE':
            return DoubleSpacesStrategy()
        elif strategy_type == 'REMOVE':
            return RemoveSpacesStrategy()
        elif strategy_type == 'REPLACE':
            return ReplaceWithUnderscoreStrategy()


def main():
    strategy_type = input("Choose a strategy [DOUBLE|REMOVE|REPLACE]: ")
    inp = "hello from SDA knowledge base!"

    strategy = SpaceModificationStrategyProvider().get(strategy_type)
    output = strategy.modify(inp)

    print(output)


if __name__ == '__main__':
    main()
