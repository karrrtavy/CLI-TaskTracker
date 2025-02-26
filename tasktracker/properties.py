class Task:
    def __init__(self, name, id, description, status, createdAt, updatedAt):
        self.name = name
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __str__(self):
        return f"ID: {self.id}\nTask: {self.name}{self.status}"
    
    def update(self, name=None, description=None, status=None, updatedAt=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if status:
            self.status = status
        if updatedAt:
            self.updatedAt = updatedAt