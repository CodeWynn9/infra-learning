from pydantic import BaseModel, ValidationError


class StudyPlan(BaseModel):
    goal: str
    days: int


raw_data = {
    "goal": "学习 AI Agent",
    "days": "3天"
}


try:
    plan = StudyPlan.model_validate(raw_data)

    print(plan)
    print(plan.goal)
    print(plan.days)
    print(type(plan))

except ValidationError as error:
    print("数据校验失败：")
    print(error)
