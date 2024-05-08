import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = createClient();

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  },
]

const getItemById = (id) => {
  const item = listProducts.find((product) => product.id === id);
  return item;
}

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
}

const getCurrentReservedStockById= async (itemId) => {
  const getValue = promisify(client.get).bind(client);
  try {
    const result = await getValue(`item.${itemId}`);
    return result;
  } catch (err) {
    throw err;
  }
}

app.get('/list_products', (req, res) => {
  const jsonList = listProducts.map((item) => {
    return {
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock
    }
  })
  res.send(JSON.stringify(jsonList));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));

  if (!item) {
    res.status(404).send({"status":"Product not found"});
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const result = {
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
      currentQuantity: item.stock - (parseInt(reservedStock) || 0)
    }
    res.json(result);
  }
})

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (item) {
    if (item.stock < 1) {
      res.send({"status":"Not enough stock available","itemId": itemId});
    } else {
      reserveStockById(itemId, 1);
      res.send({"status":"Reservation confirmed","itemId": itemId})
    }
  } else {
    res.send({"status":"Product not found"});
  }
})
app.listen(port);
