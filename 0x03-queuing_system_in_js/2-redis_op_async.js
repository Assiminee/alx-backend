#!/usr/bin/node
import {createClient, print} from 'redis';
import {promisify} from 'util';

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

const displaySchoolValue = async (schoolName) => {
    const get = promisify(redisClient.get).bind(redisClient);

    try {
        const val = await get(schoolName);
        console.log(val);
    } catch (err) {
        console.log(err);
    }
}

(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();