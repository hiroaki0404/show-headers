#!/usr/bin/env python3

def app(environment, start_response):

    res = ""
    for k in environment:
        res += f"{k}={environment[k]}\n"

    start_response('200 OK', [('Content-Type', 'text/plain')])

    return [bytes(res, encoding='utf-8', errors='replace')]