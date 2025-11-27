from typing import List, Optional

from .habit import Habit


class HabitManager:
    """
    Управляет списком привычек.
    """

    def __init__(self) -> None:
        self._habits: List[Habit] = []

    def add_habit(self, name: str, description: str = "") -> Habit:
        if self.find_habit(name):
            raise ValueError(f"Привычка '{name}' уже существует")

        habit = Habit(name=name, description=description)
        self._habits.append(habit)
        return habit

    def find_habit(self, name: str) -> Optional[Habit]:
        name = name.strip().lower()
        for habit in self._habits:
            if habit.name.lower() == name:
                return habit
        return None

    def mark_habit_done(self, name: str) -> Habit:
        habit = self.find_habit(name)
        if habit is None:
            raise ValueError(f"Привычка '{name}' не найдена")
        habit.mark_done()
        return habit

    def get_all_habits(self) -> List[Habit]:
        return list(self._habits)