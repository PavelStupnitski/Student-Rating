from typing import Dict, Tuple
from Types import DataType
from CalcDebtor import CalcDebtor
import pytest


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич": [
                ("математика", 60),
                ("русский язык", 76),
                ("программирование", 100),
            ],
            "Петров Игорь Владимирович": [
                ("математика", 60),
                ("русский язык", 60),
                ("программирование", 78),
                ("литература", 97),
            ],
        }

        rating_scores: int = 1

        return data, rating_scores

    def test_init_calc_rating(self, input_data:
                              Tuple[DataType,
                                    int]) -> None:
        calc_rating = CalcDebtor(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data:
                  Tuple[DataType, int]) -> None:
        rating = CalcDebtor(input_data[0]).calc()
        assert pytest.approx(rating) == input_data[1]
