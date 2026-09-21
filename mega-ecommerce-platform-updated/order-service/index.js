const express = require('express');
const app = express();
const PORT = 8082;
app.get('/api/orders', (req, res) => {
    res.json([{ id: 1, item: 'Laptop', status: 'Shipped' }]);
});
app.listen(PORT, () => console.log(`Order service running on port ${PORT}`));