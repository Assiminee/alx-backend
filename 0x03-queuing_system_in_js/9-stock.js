import {promisify} from 'util';
import {createClient} from 'redis';
import express from 'express';

const redisClient = createClient();

redisClient.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});

const listProducts = [
    {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];

const getItemById = (id) => {
    for (const product of listProducts) {
        if (product.Id === id)
            return product;
    }
}

const reserveStockById = (itemId, stock) => {
    const set = promisify(redisClient.SET).bind(redisClient);

    return set(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
    const GET = promisify(redisClient.GET).bind(redisClient);
    const resStock = await GET(`item.${itemId}`);

    return resStock !== null ? resStock : 0;
}

const formatJson = (item, currentQuantity) => {
    const formattedItem = {}

    formattedItem.itemId = item.id;
    formattedItem.itemName = item.name;
    formattedItem.price = item.price;
    formattedItem.initialAvailableQuantity = item.stock;

    if (currentQuantity !== undefined)
        formattedItem.currentQuantity = currentQuantity;

    return formattedItem;
}

const app = express();

app.get('/list_products', (req, res) => {
    res.json(listProducts.map((product) => formatJson(product)));
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);

    if (item === undefined) {
        res.statusCode = 404;
        res.send({status: 'Product not found'});
        return;
    }

    const reservedStock = await getCurrentReservedStockById(itemId);

    return res.json(formatJson(item, item.stock - reservedStock));
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);

    if (item === undefined)
        return res.json({status: 'Product not found'});

    const reservedStock = await getCurrentReservedStockById(itemId);
    const formattedItem = formatJson(item);

    if (reservedStock >= formattedItem.initialAvailableQuantity)
        return res.json({status: 'Not enough stock available', itemId});

    await reserveStockById(itemId, Number(reservedStock) + 1);

    return res.json({status: 'Reservation confirmed', itemId});
});

const clearRedisStock = () => {
    const SET = promisify(redisClient.SET).bind(redisClient);
    return Promise.all(listProducts.map((item) => SET(`item.${item.Id}`, 0)));
}

app.listen(1245, async () => {
    await clearRedisStock();
    console.log('API available on localhost via port 1245');
});