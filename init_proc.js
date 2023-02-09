// Init a processing run

const address = 'mongodb://146.118.68.63'
const port = 27018;
const database = 'processing_test';
const collection = 'processing_runs';

use(database);

db.insertOne(
    {
        "sbid": 1234,
        "status": "todo",

    }
);




