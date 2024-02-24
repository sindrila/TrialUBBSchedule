from Domain.StudentClass import StudentClass


class GroupClasses:
    def __init__(self, group: str, classes: list[StudentClass]):
        self._group = group
        self._classes = classes

    @property
    def group(self):
        return self._group

    @property
    def classes(self):
        return self._classes