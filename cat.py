class Cat:
    def __init__(self,name,age,weight) -> None:
        self.name = name 
        self.age = age
        self.weight = weight

    def __str__(self) -> str:
        return f"Mieu, mieu. my name is {self.name}"    