from fastapi import FastAPI, Depends, HTTPException, status

blogs = {
    "1": "FastAPI Prerequisite",
    "2": "Building APIs with FastAPI",
    "3": "Background Tasks | Celery x FastAPI"
}

users = {
    "8": "Jamie",
    "9": "Roman",
}

app = FastAPI(title="Dependency Injection")


# Since we cannot pass any parameters to the dependency, we create an object
# Which is instantiated with the __call__ method. The method runs the validation.

# We can also use methods to do the same value. 
# Advantage: We can use this for instantiation at runtime for testing

class GetObjectOr404:
    def __init__(self, model) -> None:
        self.model = model
    
    def __call__(self, id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(detail=f"Object with id {id} does not exist", 
                            status_code=status.HTTP_404_NOT_FOUND)
        return obj


blog_dependency = GetObjectOr404(blogs)
#Whatever ID being called in the "get" request will be passed to the dependency method
@app.get("/blog/{id}")
def get_blogs(blog_name: str= Depends(blog_dependency)):
    return blog_name

user_dependency = GetObjectOr404(users)
@app.get("/user/{id}")
def get_blogs(blog_name: str= Depends(user_dependency)):
    return blog_name
