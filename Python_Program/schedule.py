#! /usr/bin/env python3

from __future__ import print_function
import sys
from optparse import OptionParser
import random


# to make Python2 and Python3 act the same -- how dumb
def random_seed(seed):
    try:
        random.seed(seed, version=1)
    except:
        random.seed(seed)
    return


parser = OptionParser()
parser.add_option("-s", "--seed", default=0, help="the random seed", action="store", type="int", dest="seed")
parser.add_option("-j", "--jobs", default=3, help="number of jobs in the system", action="store", type="int",
                  dest="jobs")
parser.add_option("-l", "--jlist", default="",
                  help="instead of random jobs, provide a comma-separated list of run times", action="store",
                  type="string", dest="jlist")
parser.add_option("-m", "--maxlen", default=10, help="max length of job", action="store", type="int", dest="maxlen")
parser.add_option("-p", "--policy", default="FIFO", help="sched policy to use: SJF, FIFO, RR", action="store",
                  type="string", dest="policy")
parser.add_option("-q", "--quantum", help="length of time slice for RR policy", default=1, action="store", type="int",
                  dest="quantum")
parser.add_option("-c", help="compute answers for me", action="store_true", default=False, dest="solve")
parser.add_option("-a", help="set arrival time for each process", default="", 
                  action="store", type="string", dest="arrival") # arrival time 옵션 생성 및 파싱
(options, args) = parser.parse_args()

random_seed(options.seed)

arrival_time = [] # arrival time을 담을 list
print('ARG policy', options.policy)
if options.jlist == '':
    print('ARG jobs', options.jobs)
    print('ARG maxlen', options.maxlen)
    print('ARG seed', options.seed)
    if options.arrival == "": # 만약 사용자가 job list를 입력하지 않았는데 arrival time도 입력하지 않았다면 arrival time을 각각 0으로 할당
        arrival_time = [0,0,0]
        print('ARG arrival time 0,0,0') # 사용자가 job list를 입력하지 않았다면 default arrival time인 0,0,0 콘솔창 출력
    else:
        if(len(options.arrival.split(',')) != 3): # 만약 사용자가 job list를 입력하지 않았는데 arrival time을 입력했다면 개수가 맞을 경우 해당 arrival time을 각각 할당
            sys.exit('job의 개수와 arrival time의 개수를 맞춰주세요.')
        for time in options.arrival.split(','): # 만약 사용자가 arrival time을 입력했을 경우 각 job에 입력받은 arrival time 각각 할당
            arrival_time.append(time)
        print('ARG arrival time',','.join(map(str,arrival_time)))
    
    
else:
    print('ARG jlist', options.jlist)
    if options.arrival == "": # 만약 사용자가 job list를 입력했는데 arrival time을 입력하지 않았을 경우 각 job에 기본값 0 할당
        for i in options.jlist.split(','): 
            arrival_time.append(0) # 입력받은 job list의 개수만큼 0 할당
    else:
        if(len(options.jlist) != len(options.arrival)): # 만약 입력받은 job의 개수와 arrival time의 개수가 맞지 않을 경우 프로그램 종료
            sys.exit('job의 개수와 arrival time의 개수를 맞춰주세요.')
        for time in options.arrival.split(','): # 만약 사용자가 arrival time을 입력했을 경우 각 job에 입력받은 arrival time 각각 할당
            arrival_time.append(time)
    print('ARG arrival time',','.join(map(str,arrival_time)))

print('')

print('Here is the job list, with the run time of each job: ')

import operator

joblist = []
if options.jlist == '':
    for jobnum in range(0, options.jobs):
        runtime = int(options.maxlen * random.random()) + 1
        joblist.append([jobnum, runtime, arrival_time[jobnum]])
        print('  Job', jobnum, '( length = ' + str(runtime) + ', arrival time = ' + str(arrival_time[jobnum]) + ' )')
else:
    jobnum = 0
    for runtime in options.jlist.split(','):
        joblist.append([jobnum, float(runtime), arrival_time[jobnum]])
        jobnum += 1
    for job in joblist:
        print('  Job', job[0], '( length = ' + str(job[1]) + ', arrival time = ' + str(job[2]) + ' )')
print('\n')

if options.solve == True:
    print('** Solutions **\n')
    if options.policy == 'SJF':
        joblist = sorted(joblist, key=operator.itemgetter(1))
        options.policy = 'FIFO'

    if options.policy == 'FIFO':
        thetime = 0
        print('Execution trace:')
        if(arrival_time[-1] != 0): # 만약 arrival time이 존재하는 경우 arrival time 순으로 정렬 후 FIFO 실행
            joblist = sorted(joblist, key=operator.itemgetter(2))
        for job in joblist:
            print('  [ time %3d ] Run job %d for %.2f secs ( DONE at %.2f )' % (
                thetime, job[0], job[1], thetime + job[1]))
            thetime += job[1]

        print('\nFinal statistics:')
        t = 0.0
        count = 0
        turnaroundSum = 0.0
        waitSum = 0.0
        responseSum = 0.0
        for tmp in joblist:
            jobnum = tmp[0]
            runtime = tmp[1]

            response = t
            turnaround = t + runtime
            wait = t
            print('  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (jobnum, response, turnaround, wait))
            responseSum += response
            turnaroundSum += turnaround
            waitSum += wait
            t += runtime
            count = count + 1
        print('\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (
            responseSum / count, turnaroundSum / count, waitSum / count))

    if options.policy == 'RR':
        print('Execution trace:')
        turnaround = {}
        response = {}
        lastran = {}
        wait = {}
        quantum = float(options.quantum)
        jobcount = len(joblist)
        for i in range(0, jobcount):
            lastran[i] = 0.0
            wait[i] = 0.0
            turnaround[i] = 0.0
            response[i] = -1

        runlist = []
        for e in joblist:
            runlist.append(e)

        thetime = 0.0
        while jobcount > 0:
            job = runlist.pop(0)
            jobnum = job[0]
            runtime = float(job[1])
            if response[jobnum] == -1:
                response[jobnum] = thetime
            currwait = thetime - lastran[jobnum]
            wait[jobnum] += currwait
            if runtime > quantum:
                runtime -= quantum
                ranfor = quantum
                print('  [ time %3d ] Run job %3d for %.2f secs' % (thetime, jobnum, ranfor))
                runlist.append([jobnum, runtime])
            else:
                ranfor = runtime;
                print('  [ time %3d ] Run job %3d for %.2f secs ( DONE at %.2f )' % (
                    thetime, jobnum, ranfor, thetime + ranfor))
                turnaround[jobnum] = thetime + ranfor
                jobcount -= 1
            thetime += ranfor
            lastran[jobnum] = thetime

        print('\nFinal statistics:')
        turnaroundSum = 0.0
        waitSum = 0.0
        responseSum = 0.0
        for i in range(0, len(joblist)):
            turnaroundSum += turnaround[i]
            responseSum += response[i]
            waitSum += wait[i]
            print(
                '  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (i, response[i], turnaround[i], wait[i]))
        count = len(joblist)

        print('\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (
            responseSum / count, turnaroundSum / count, waitSum / count))

    if options.policy != 'FIFO' and options.policy != 'SJF' and options.policy != 'RR':
        print('Error: Policy', options.policy, 'is not available.')
        sys.exit(0)
else:
    print('Compute the turnaround time, response time, and wait time for each job.')
    print('When you are done, run this program again, with the same arguments,')
    print('but with -c, which will thus provide you with the answers. You can use')
    print('-s <somenumber> or your own job list (-l 10,15,20 for example)')
    print('to generate different problems for yourself.')
    print('')