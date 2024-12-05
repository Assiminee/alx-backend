#!/usr/bin/node
import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
});

redisClient.SUBSCRIBE('holberton school channel');

redisClient.on('message', (channel, msg) => {
    if (channel === 'holberton school channel') {
        if (msg === 'KILL_SERVER') {
            redisClient.UNSUBSCRIBE();
            redisClient.QUIT();
        }
        console.log(msg);
    }
});