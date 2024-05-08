import { createClient, print} from 'redis';
import { promisify } from 'util';


const client = createClient();
client.on('connect', () =>  console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis client not connected to the server:', err));


const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
}

const displaySchoolValue = async (schoolName) => {
  const getValue = promisify(client.get).bind(client);
  try {
    const result = await getValue(schoolName);
    console.log(result);
  } catch (err) {
    throw err;
  }
  
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
