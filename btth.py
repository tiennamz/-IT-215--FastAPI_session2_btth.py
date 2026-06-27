from fastapi import FastAPI

app = FastAPI()

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    }
]


app.get('/health')
def check_system():
    return {
            "message": "API is running"
            }
    
app.get('/courses')
def get_courses():
    return {
        'data': courses
    }
    
app.get('/courses/{course_id}')
def find_course(course_id):
    if course_id <= 0:
        return {'status_code': 400}
        
    for course in courses:
        if course['id'] == course_id:
            return {
                'data': course
            }
            
    return {'status_code': 404}