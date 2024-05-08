import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';


const app = express();
const port = 1245;
const client = createClient();
const queue = kue.createQueue();

let reservationEnabled = true;

const reserveSeat = (number) => {
  client.set(`available_seats`, number);
}

const getCurrentAvailableSeats = async() => {
  const getValue = promisify(client.get).bind(client);
  try {
    const value = await getValue('available_seats');
    return value;
  } catch(err) {
    throw err;
  }
}

app.get('/available_seats', async (req, res) => {
  const available_seats = await getCurrentAvailableSeats();
  res.json({"numberOfAvailableSeats": available_seats});
})

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({"status": "Reservation are blocked"})
  } else {
    const job = queue.create('reserve_seat');
    job.save((err) => {
      if (err) {
        res.json({ "status": "Reservation failed" });
      } else {
        res.json({ "status": "Reservation in process"});
      }
    })
    job.on('complete', (result) => {
      console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    })
  }
})

app.get('/process', (req, res) => {
  res.json({ "status": "Queue processing" });
  queue.process('reserve_seat', async (job, done) => {
    const available_seats = await getCurrentAvailableSeats();
    const current_seats = (parseInt(available_seats) || 0) - 1;
    reserveSeat(current_seats);

    if (current_seats === 0) {
      reservationEnabled = false;
    }
    if (current_seats > 0) {
      done();
    } else {
      done(new Error(`Not enough seats available`));
    }
  });
})

app.listen(port, () => {
  reserveSeat(50);
});
