#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo
from typing import Union

def main(
    host: str = 'localhost',
    port: int = 27017,
    db_name: str = 'test',
    collection_name: str = 'test',
    data: dict = {},
    username: Union[str, None] = None,
    password: Union[str, None] = None,
    action: str = 'insert',
):
    client = pymongo.MongoClient(
        host,
        port,
        username=username,
        password=password,
        authMechanism="SCRAM-SHA-256" if username and password else "DEFAULT",
    )
    db = client[db_name]
    collection = db[collection_name]

    if action == 'insert':
        insert_result = collection.insert_one(data)
        print(f"Inserted id: {insert_result.inserted_id}")
        print(f"Success: {insert_result.acknowledged}")

    elif action == 'update':
        update_result = collection.update_one({'_id': data['_id']}, {'$set': data})
        print(f"Matched count: {update_result.matched_count}")
        print(f"Modified count: {update_result.modified_count}")
        print(f"Success: {update_result.acknowledged}")
    else:
        raise ValueError(f"Unknown action: {action}")


if __name__ == '__main__':
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=27017)
    parser.add_argument('--db', type=str, default='test')
    parser.add_argument('--collection', type=str, default='test')
    parser.add_argument('--data-file', type=str, default='')
    parser.add_argument('--action', type=str, default='insert')
    parser.add_argument('-u','--username', type=str, default=None)
    parser.add_argument('-p','--password', type=str, default=None)
    args = parser.parse_args()

    with open(args.data_file, 'r') as f:
        data = json.load(f)

    main(
        host=args.host,
        port=args.port,
        db_name=args.db,
        collection_name=args.collection,
        data=data,
        username=args.username,
        password=args.password,
        action=args.action,
    )