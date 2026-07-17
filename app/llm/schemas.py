from pydantic import BaseModel


class TestCase(BaseModel):
    title: str
    steps: list[str]
    expected_result: str
class TestCaseList(BaseModel):
    test_cases: list[TestCase]