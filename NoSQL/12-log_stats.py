#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs stored in Mongo
"""
from pymongo import MongoClient


def log_stats():
    """returns the list of school having a specific topic"""
    client = MongoClient("mongodb://localhost:27017/")
    logs = client.logs.nginx.count_documents({})
    print(f"{logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = client.logs.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status = client.logs.nginx.count_documents({"method": "GET", "path":
                                                "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()
