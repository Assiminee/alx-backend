import {createQueue} from 'kue';
import {expect} from 'chai';
import {spy} from 'sinon';
import createPushNotificationsJobs from './8-job';

describe('createPushNotifications unit tests', () => {
    const queue = createQueue();

    before(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
    });

    after(() => {
        queue.testMode.exit();
    });

    it('Successfully adding jobs to queue', () => {
        const spyConsole = spy(console, 'log');
        const jobs = [
            {phoneNumber: '622718341', message: 'Message for phone number 622718341'},
            {phoneNumber: '637481999', message: 'Message for phone number 637481999'},
        ];

        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(spyConsole.calledTwice).to.be.true;
    });

    it('Successfully adds job with correct data to queue', () => {
        const jobs = [
            {phoneNumber: '622718341', message: 'Message for phone number 622718341'}
        ];

        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
    });

    it('Incorrect job type passed: throws an error', () => {
        const jobs = {
            phoneNumber: '622718341', message: 'Message for phone number 622718341'
        };

        expect(() => createPushNotificationsJobs(jobs, queue)).to.throw('Jobs is not an array');
    });
});