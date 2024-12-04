#!/usr/bin/node
import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    redisClient.set(schoolName, value, print);
}

const displaySchoolValue = (schoolName) => {
    redisClient.get(schoolName, (err, data) => {
        if (!err)
            console.log(data);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');