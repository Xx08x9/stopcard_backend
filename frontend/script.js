let cartCount = 0;

function addToCart() {
    cartCount++;
    document.getElementById("cart-count").innerText = cartCount;
}

const API = "http://127.0.0.1:5000";

// 📦 загрузка товаров с backend
async function loadProducts() {
    const res = await fetch(`${API}/products`);
    const data = await res.json();

    const grid = document.querySelector(".grid");
    grid.innerHTML = "";

    data.forEach(product => {
        grid.innerHTML += `
        <div class="card">
            <h3>${product.name}</h3>
            <p>Профессиональная техника</p>
            <span>${product.price}$</span>
            <button onclick="addToCart(${product.id})">В корзину</button>
        </div>
        `;
    });
}

// 🛒 добавить в корзину
async function addToCart(id) {
    await fetch(`${API}/cart/add`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({id})
    });

    alert("Добавлено в корзину");
}

// загрузка при старте
loadProducts();