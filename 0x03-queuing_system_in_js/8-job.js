const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

    for (let job of jobs) {
        job =  queue.create('push_notification_code_3', job);
        job.save((err) => {
            if (!err) console.log(`Notification job created: ${job.id}`);
        });
        job.on('complete', () => console.log(`Notification job ${job.id} completed`));
        job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% completed`));
        job.on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`));
    }
}

export default createPushNotificationsJobs;