#!/usr/bin/env python

from __future__ import print_function

import argparse
import glob
import multiprocessing
import subprocess
import os
import sys

def build_command(command, git_dir, work_tree=None):
    result = ['git', '--git-dir=' + git_dir]
    if work_tree:
        result.append('--work-tree=' + work_tree)
    result.extend(command)
    return result

def build_jobs(pattern, bare_repos, command):
    jobs = []
    for match in glob.glob(pattern):
        if bare_repos:
            command_args = build_command(command, match),
        else:
            command_args = build_command(command, match + '/.git', match)
        jobs.append({
            'dir':     match,
            'command': command_args,
        })
    return jobs

def get_executor(jobs):
    if jobs != 0:
        return multiprocessing.Pool(jobs).map
    else:
        return map

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bare-repos', action='store_true')
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('-j', '--jobs', type=int,
                                        default=multiprocessing.cpu_count())
    parser.add_argument('pattern', metavar='PATTERN', type=str)
    parser.add_argument('command', metavar='COMMAND', type=str,
                                   nargs=argparse.REMAINDER)

    return parser

def main():
    args     = build_argparser().parse_args()
    jobs     = build_jobs(args.pattern, args.bare_repos, args.command)
    executor = get_executor(args.jobs)

    results = executor(subprocess.check_output, (job['command'] for job in jobs))
    for job, result in zip(jobs, results):
        if not args.quiet:
            print(job['dir'])
        if result != '':
            print(result)

if __name__ == '__main__':
    main()

