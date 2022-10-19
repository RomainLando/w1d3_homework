tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
def to_do(tasks_list):
    jobs = [job for job in tasks_list if job["completed"]==False]
    return jobs

def done_jobs(tasks_list):
    jobs = [job for job in tasks_list if job["completed"]]
    return jobs

def descriptions(tasks_list):
    descs = [ job["description"] for job in tasks_list]
    return descs

def task_by_time(tasks_list, time):
    jobs = [job for job in tasks_list if job["time_taken"] < time]
    return jobs

def task_by_desc(desc):
    described_job = [job for job in tasks if job["description"] == desc]
    return described_job

def update_task(desc):
    for job in tasks:
        if job["description"] == desc:
            job["completed"] = True 

def add_task(task):
    tasks.append(task)

new_task = {
    "description" : "Mop floors",
    "completed" : False,
    "time_taken" : 25
}

add_task(new_task)
print(tasks)
