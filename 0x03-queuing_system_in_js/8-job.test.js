import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';


const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit()
  });
  it('display a error message if jobs is not an array', () => {
    const list = 'Hello world';
    expect(function(){createPushNotificationsJobs(list, queue);}).to.throw('Jobs is not an array');
    expect(queue.testMode.jobs.length).to.equal(0);
  })
  it('create two new jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4109875780',
        message: 'This is the code 2457 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(list[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data.message).to.equal('This is the code 2457 to verify your account');
  })
});
