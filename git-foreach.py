#!/usr/bin/env python

import argparse
import glob
import multiprocessing
import subprocess
import os

def build_subcommand(git_dir, bare_repos, command):
    subcommand = ['git', '--git-dir=' + git_dir]
    if not bare_repos:
        work_tree = os.path.join(git_dir, '..')
        subcommand.append('--work-tree=' + work_tree)
    subcommand.extend(command)
    return subcommand

def build_subcommands(pattern, bare_repos, command):
    subcommands = []
    for git_dir in glob.glob(pattern):
        subcommands.append(build_subcommand(git_dir, bare_repos, command))
    return subcommands

def get_executor(jobs):
    if jobs != 0:
        return multiprocessing.Pool(jobs).map
    else:
        return map

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bare-repos', action='store_true')
    parser.add_argument('-j', '--jobs', type=int,
                                        default=multiprocessing.cpu_count())
    parser.add_argument('pattern', metavar='PATTERN', type=str)
    parser.add_argument('command', metavar='COMMAND', type=str,
                                   nargs=argparse.REMAINDER)

    return parser

def main():
    args        = build_argparser().parse_args()
    subcommands = build_subcommands(args.pattern,
                                    args.bare_repos,
                                    args.command)
    executor    = get_executor(args.jobs)

    executor(subprocess.call, subcommands)

if __name__ == '__main__':
    main()

