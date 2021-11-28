import xml.etree.ElementTree as ET

from Types import DataType
from DataReader import DataReader


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()
        for student in root:
            self.key = student.tag
            self.students[self.key] = []
            for evaluations in student:
                subj = (evaluations.tag.strip(),
                        int((str(evaluations.text).strip())))
                self.students[self.key].append(subj)
        return self.students
