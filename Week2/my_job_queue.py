# python3

from collections import namedtuple
from heapq import heapify, heappush, heappop

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = []
    heapify(next_free_time)

    # fill in the heap
    for w in range(n_workers):
        # node store tuple: (next free time, worker index)
        heappush(next_free_time, (0, w))

    # iterate jobs
    for job in jobs:
        # find the heap min / the worker to do the job next
        next_work = heappop(next_free_time) 
        # store the results
        result.append(AssignedJob(next_work[1], next_work[0]))
        # update the next free time for this worker
        heappush(next_free_time, (next_work[0]+job, next_work[1]))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
