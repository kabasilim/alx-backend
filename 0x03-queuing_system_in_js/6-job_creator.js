import kue from 'kue';

const queue = kue.createQueue();
const jobData = {
  phoneNumber: '091762612',
  message: 'data'
}
const job = queue.create('push_notification_code', jobData).save((err) => {
  if(!err) console.log( `Notification job created: ${job.id}`);
});
job.on('complete', (result) => {
  console.log('Notification job completed');
});
job.on('failed', (errorMessage) => {
  console.log('Notification job failed');
})
