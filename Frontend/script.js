document.getElementById('addStockForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const symbol = document.getElementById('symbol').value;
    const quantity = document.getElementById('quantity').value;
    const purchasePrice = document.getElementById('purchase_price').value;

    const response = await fetch('/add_stock', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symbol, quantity, purchase_price: purchasePrice })
    });

    const result = await response.json();
    alert(result.status);
});

document.getElementById('viewPortfolioBtn').addEventListener('click', async function() {
    const response = await fetch('/view_portfolio');
    const result = await response.json();
    const portfolioResult = document.getElementById('portfolioResult');

    portfolioResult.innerHTML = `
        <p><strong>Total Portfolio Value:</strong> $${result.total_value.toFixed(2)}</p>
        <p><strong>Gains/Losses:</strong></p>
        <ul>
            ${Object.keys(result.gains_losses).map(symbol => `
                <li>${symbol}: $${result.gains_losses[symbol].toFixed(2)}</li>
            `).join('')}
        </ul>
    `;
});
