import React from "react"

function ProductCard({product}){

    return(

        <div className="product-card">

            <img src={product.image} alt={product.name} />

            <h3>{product.name}</h3>

            <p>{product.price} сом</p>

            <button>В корзину</button>

        </div>

    )

}

export default ProductCard