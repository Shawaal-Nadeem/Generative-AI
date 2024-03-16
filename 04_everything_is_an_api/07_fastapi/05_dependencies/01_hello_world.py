# # Example 01 old way with helper function
# from fastapi import FastAPI, Depends, Query

# app : FastAPI = FastAPI()

# def login(username : str , password : str ):
#     if username == "admin" and password == "admin":
#         return {"message" : "Login Successful"}
#     else:
#         return {"message" : "Login Failed"}
    

# @app.get("/login")
# def login_api(user,password):
#     result = login(user,password) # custom calling
#     return result


# # Example 02 new way with Dependencies injection
# from fastapi import FastAPI, Depends, Query
# from typing import Annotated

# app : FastAPI = FastAPI()

# # depency function
# def dep_login(username : str = Query(None), password : str = Query(None)):
#     if username == "admin" and password == "admin":
#         return {"message" : "Login Successful"}
#     else:
#         return {"message" : "Login Failed"}
    
# @app.get("/signin")
# def login_api(user :  Annotated[dict,Depends(dep_login)]): # I call dependency function in custom function bcz function returns some value
#     return user  


# # Example 03 
# from fastapi import FastAPI, Depends, Query
# from typing import Annotated

# app : FastAPI = FastAPI()

# # depency function
# def dep_login(username : str = Query(None)):
#    if not username:
#        raise
    
# @app.get("/signin", dependencies=[Depends(dep_login)]) # I call dependency function in end point bcz function returns not any value
# def login_api():
#     return True

# # Example 4
# from fastapi import FastAPI, Depends, Query

# app=FastAPI()

# def dep_fun1(num:int):
#     num+=1
#     return num

# def dep_fun2(num:int):
#     num+=1
#     return num

# @app.get("/main/{num}")
# def mainFun(num:int,num1:int=Depends(dep_fun1),num2:int=Depends(dep_fun2)):
#     #        1      2     2
#     total = num + num1 + num2
#     return {"Pakistan":total}

# # Example 5
# from fastapi import FastAPI, Depends, HTTPException, status
# from typing import Annotated

# blogs = {
#     "1": "Generative AI Blog",
#     "2": "Machine Learning Blog",
#     "3": "Deep Learning Blog"
# }

# users = {
#     "8": "Ahmed",
#     "9": "Mohammed"
# }

# def get_blog_or_404(id: str):
#     name = blogs.get(id)
#     if not name:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog ID {id} not found")
#     return name

# app = FastAPI(title="Learn Dependency Injection")

# @app.get("/blog/{id}")
# def get_blog(blog_name: Annotated[str, Depends(get_blog_or_404)]):
#     return blog_name

# # Example 6
# from fastapi import FastAPI, Depends, HTTPException, status
# from typing import Annotated

# blogs = {
#     "1": "Generative AI Blog",
#     "2": "Machine Learning Blog",
#     "3": "Deep Learning Blog"
# }

# users = {
#     "8": "Ahmed",
#     "9": "Mohammed"
# }

# class GetObjectOr404():
#     def __init__(self, model)->None:
#         self.model = model

#     def __call__(self, id: str):
#         obj = self.model.get(id)
#         if not obj:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
#         return obj

# app = FastAPI(title="Learn Dependency Injection")

# blog_dependency = GetObjectOr404(blogs)

# @app.get("/blog/{id}")
# def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
#     return blog_name

# user_dependency = GetObjectOr404(users)

# @app.get("/user/{id}")
# def get_user(user_name: Annotated[str, Depends(user_dependency)]):
#     return user_name

# # Example 7
# from fastapi import FastAPI, Depends
# from typing import Annotated

# development_db = ["DB for Development"]

# def get_db_session():
#     return development_db 

# app = FastAPI()


# @app.get("/add-item/")
# def add_item(item:str, db :Annotated[list,Depends(get_db_session)]):
#     db.append(item)
#     print(db)
#     return {"message":f"added item {item}"}#, "all database": db}

# Remaining Examples which is imp . See on panaverse repo and remaining step are:
# test_dependency_injection
