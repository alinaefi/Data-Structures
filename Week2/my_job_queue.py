"""Parallel processing
Problem Introduction
In this problem you will simulate a program that processes a list of jobs in parallel. Operating systems such
as Linux, MacOS or Windows all have special programs in them called schedulers which do exactly this with
the programs on your computer.
Problem Description
Task. You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚
jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately
takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop
until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the
thread with smaller index takes the job. For each job you know exactly how long will it take any thread
to process this job, and this time is the same for all the threads. You need to determine for each job
which thread will process it and when will it start processing.
Input Format. The first line of the input contains integers 𝑛 and 𝑚.
The second line contains 𝑚 integers 𝑡𝑖 — the times in seconds it takes any thread to process 𝑖-th job.
The times are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting from 0.
Constraints. 1 ≤ 𝑛 ≤ 105; 1 ≤ 𝑚 ≤ 105; 0 ≤ 𝑡𝑖 ≤ 109.
Output Format. Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two spaceseparated integers — the 0-based index of the thread which will process the 𝑖-th job and the time
in seconds when it will start processing that job."""

from collections import namedtuple
from heapq import heapify, heappush, heappop

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
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
