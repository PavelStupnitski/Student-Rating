from Types import DataType


class CalcDebtor:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.count: int = 0

    def calc(self) -> int:
        for fio, subjects in self.data.items():
            count = 0
            for subject in subjects:
                if int(subject[1]) < 61:
                    count += 1
            if count == 2:
                self.count += 1
        return self.count
