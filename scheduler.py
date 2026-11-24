import time
import random
import threading
import queue

job_queue = queue.Queue()

def runner(runner_id):
    while True:
        job = job_queue.get()

        if job is None:
            job_queue.task_done()
            break

        job_id, duration = job

        print(f"Runner {runner_id}: Starting Job {job_id}")

        time.sleep(duration)

        print(f"Runner {runner_id}: Finished Job {job_id}")

        job_queue.task_done()


# Create 3 runners
runners = []

for i in range(3):
    worker = threading.Thread(
        target=runner,
        args=(i + 1,)
    )

    worker.start()
    runners.append(worker)


# Submit 12 jobs
for job_id in range(1, 13):
    duration = random.randint(2, 5)

    job_queue.put((job_id, duration))

    print(
        f"Submitted Job {job_id}. "
        f"Jobs waiting: {job_queue.qsize()}"
    )


# Wait until all jobs finish
job_queue.join()

# Shut down runners
for _ in runners:
    job_queue.put(None)

for worker in runners:
    worker.join()

print("All jobs completed.")