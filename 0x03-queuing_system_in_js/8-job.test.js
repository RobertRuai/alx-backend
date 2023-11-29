import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  }
]

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

it('displays error mess if jobs is not array', () => {
  expect(() => createPushNotificationsJobs('yyo', queue)).to.throw(
    'Jobs is not an array');
});

it('create two new jobs', () => {
  createPushNotificationsJobs(jobs, queue);
  expect(queue.testMode.jobs.length).to.equal(2);
  expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
  expect(queue.testMode.jobs[1].data).to.equal(jobs[1]);
  expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
});
