import copy


class GameState:
    def __init__(self, health=0, mana=0, items=None):
        self._health = health
        self._mana = mana
        if items is None:
            self._items = []
        else:
            self._items = items

    def __str__(self):
        return f"GameState[health={self._health}, mana={self._mana}, items={self._items}]"

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    @property
    def items(self):
        return self._items

    def heal(self):
        self._health = 100

    def take_damage(self, damage):
        self._health -= damage

    def add_item(self, item):
        self._items.append(item)

    def lose_all_items(self):
        self._items.clear()

    def restore_from_snapshot(self, snapshot):
        self._health = snapshot.health
        self._mana = snapshot.mana
        self._items = copy.deepcopy(snapshot.items)


class GameStateSnapshot:
    def __init__(self, game_state):
        self._health = game_state.health
        self._mana = game_state.mana
        self._items = copy.deepcopy(game_state.items)

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    @property
    def items(self):
        return self._items


class GameStateManager:
    def __init__(self):
        self._snapshots = []

    def save_game(self, game_state):
        self._snapshots.append(GameStateSnapshot(game_state))

    def restore_previous_checkpoint(self):
        return self._snapshots.pop()


def main():
    game_state = GameState(100, 80)

    game_state_manager = GameStateManager()
    game_state_manager.save_game(game_state)
    print(game_state)

    game_state.add_item('Basic Sword')
    game_state.take_damage(10)
    game_state_manager.save_game(game_state)
    print(game_state)

    game_state.take_damage(50)
    game_state.add_item('Shield')
    game_state_manager.save_game(game_state)
    print(game_state)

    game_state_manager.restore_previous_checkpoint()
    game_state_manager.restore_previous_checkpoint()
    game_state_snapshot = game_state_manager.restore_previous_checkpoint()
    game_state.restore_from_snapshot(game_state_snapshot)
    print(game_state)


if __name__ == '__main__':
    main()
