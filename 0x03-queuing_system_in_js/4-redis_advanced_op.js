#!/usr/bin/node
import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
});

const multi = redisClient.multi();

multi
    .hSet('HolbertonSchools', 'Portland', 50, print)
    .hSet('HolbertonSchools', 'Seattle', 80, print)
    .hSet('HolbertonSchools', 'New York', 20, print)
    .hSet('HolbertonSchools', 'Bogota', 20, print)
    .hSet('HolbertonSchools', 'Cali', 40, print)
    .hSet('HolbertonSchools', 'Paris', 2, print);

multi.exec();

redisClient.hgetall('HolbertonSchools', (err, hashset) => {
    console.log(hashset);
});